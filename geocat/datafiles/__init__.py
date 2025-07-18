import hashlib
import os
import pooch
import requests

# get version from pyproject.toml
from importlib.metadata import version as _version

try:
    __version__ = _version("geocat.datafiles")
except Exception:
    # Local copy or not installed with setuptools.
    # Disable minimum version checks on downstream libraries.
    __version__ = "9999"

# code for pooch
POOCH = pooch.create(
    path=pooch.os_cache('geocat'),
    base_url='https://github.com/NCAR/geocat-datafiles/raw/main/',
    registry={'registry.txt': None},
    retry_if_failed=10)

def _update_registry(p):
    """
    Updates pooch registry.txt
    """
    old_sha256 = p.registry["registry.txt"]
    new_sha256 = hashlib.sha256(requests.get(p.get_url("registry.txt")).content).hexdigest()
    if old_sha256 != new_sha256:
        p.registry["registry.txt"] = new_sha256
        p.load_registry(p.fetch("registry.txt"))

dev_data_path = os.environ.get('GEOCAT_DATA_DIR')

if dev_data_path is not None and os.path.exists(dev_data_path):
    POOCH.path = dev_data_path

_update_registry(POOCH)

def get(fname):
    return POOCH.fetch(fname)
