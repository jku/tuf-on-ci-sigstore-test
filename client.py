# Example client for keyless TUF repo maintained in
# https://github.com/jku/tuf-on-ci-sigstore-test

# requirements: 
#   pip install tuf securesystemslib[crypto] sigstore

# Usage example:
#   python3 client.py testfile

import os
import requests
import sys
from securesystemslib.signer import KEY_FOR_TYPE_AND_SCHEME, SigstoreKey
from tuf.ngclient import Updater

# Enable experimental sigstore support 
KEY_FOR_TYPE_AND_SCHEME[("sigstore-oidc", "Fulcio")] = SigstoreKey

url = "https://jku.github.io/tuf-on-ci-sigstore-test"
metadata_dir = "/tmp/tuf-on-ci-sigstore-test/"

if len (sys.argv) != 2:
    sys.exit(f"Usage:  {sys.argv[0]} <targetpath>")

# Trust-on-first-use: Download initial root metadata if it's not available
if not os.path.exists(f"{metadata_dir}/root.json"):
    os.makedirs(metadata_dir, exist_ok=True)
    with open(f"{metadata_dir}/root.json", "wb") as f:
        f.write(requests.get(f"{url}/metadata/1.root.json").content)

# Download target securely using python-tuf
updater = Updater(
    metadata_dir=metadata_dir,
    metadata_base_url=f"{url}/metadata/",
    target_dir="./",
    target_base_url=f"{url}/targets/"
)
info = updater.get_targetinfo(sys.argv[1])
if not info:
    print(f"'{sys.argv[1]}' not found")
    sys.exit()

path = updater.find_cached_target(info)
if path:
    print(f"'{path}' is already up-to-date")
    sys.exit()

path = updater.download_target(info)
print(f"Downloaded '{path}'")
