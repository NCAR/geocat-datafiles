import os
import pooch

from ._version import __version__

POOCH = pooch.create(
    path=pooch.os_cache('geocat'),
    base_url='https://github.com/NCAR/GeoCAT-datafiles/raw/{version}/',
    version='v' + __version__,
    version_dev='master')

dev_data_path = os.environ.get('GEOCAT_DATA_DIR')

if dev_data_path is not None and os.path.exists(dev_data_path):
    POOCH.path = dev_data_path

POOCH.load_registry(os.path.join(os.path.dirname(__file__), 'registry.txt'))

def get(fname):
    return POOCH.fetch(fname)
