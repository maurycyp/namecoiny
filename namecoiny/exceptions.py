class NamecoinyError(Exception):
    pass


class LockedRegionError(NamecoinyError):
    region = None

    def __init__(self, region):
        self.region = region
