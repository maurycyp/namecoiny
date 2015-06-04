import skiff

from .exceptions import LockedRegionError
from .utils import get_fingerprint_for_rsa_key_path


class DigitalOceanDroplet(object):
    LOCKED_REGIONS = ['nyc1', 'ams1']

    DEFAULT_REGION = 'nyc3'
    DEFAULT_SIZE   = '512mb'
    DEFAULT_IMAGE  = 'ubuntu-14-04-x64'

    s          = None
    token      = None
    droplet    = None
    public_key = None

    def __init__(self, token):
        self.token = token
        self.s = skiff.rig(token)

    def __repr__(self):
        return '<Droplet: %s>' % self.ip_address

    @property
    def ip_address(self):
        return self.droplet.v4[0].ip_address

    def create(self, name, public_key_path, private_key_path, region=None):
        if region in self.LOCKED_REGIONS:
            raise LockedRegionError(region)

        with open(public_key_path, 'r') as f:
            self.public_key = f.read()

        key_name = '%s key' % name
        try:
            key = self.s.Key.create(name=key_name, public_key=self.public_key)
        except ValueError:
            fp = get_fingerprint_for_rsa_key_path(private_key_path)
            key = self.s.Key.get(fp)

        # create droplet
        opts = {
            'name':     name,
            'region':   region or self.DEFAULT_REGION,
            'size':     self.DEFAULT_SIZE,
            'image':    self.DEFAULT_IMAGE,
            'ssh_keys': [key],
        }

        self.droplet = self.s.Droplet.create(**opts)
        self.droplet.wait_till_done()
        self.droplet = self.droplet.refresh()
