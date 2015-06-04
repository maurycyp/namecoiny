from paramiko.rsakey import RSAKey


def get_fingerprint_for_rsa_key_path(path):
    key = RSAKey(filename=path)
    fp = key.get_fingerprint().encode('hex')
    return add_colons_to_fingerprint(fp)


def add_colons_to_fingerprint(fp):
    new_fp = ''
    for i, b in enumerate(fp):
        if i % 2 == 0 and i > 0:
            new_fp += ':'
        new_fp += b
    return new_fp
