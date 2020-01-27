import hashlib
import os
import pooch
import requests

from ._version import __version__

POOCH = pooch.create(
    path=pooch.os_cache('geocat'),
    base_url='https://github.com/NCAR/GeoCAT-datafiles/raw/master/',
    version='v' + __version__,
    version_dev='master',
    registry={'registry.txt': None})

dev_data_path = os.environ.get('GEOCAT_DATA_DIR')

if dev_data_path is not None and os.path.exists(dev_data_path):
    POOCH.path = dev_data_path

POOCH.registry["registry.txt"] = hashlib.sha256(requests.get(POOCH.get_url("registry.txt")).content).hexdigest()
POOCH.load_registry(POOCH.fetch('registry.txt'))

def get(fname):
    return POOCH.fetch(fname)
