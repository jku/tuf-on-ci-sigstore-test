# A keyless TUF repository using Sigstore 

A completely keyless TUF repository:
* Repository signs online roles with sigstore using the ambient GitHub workflow identity
* Offline signers use their (interactive) sigstore identities

Clients should access the repository at https://jku.github.io/tuf-on-ci-sigstore-test/metadata/

A typical TUF client is not at the moment compatible with this repository (as sigstore identities as keys is not a
commonly supported feature) but python-tuf + securesystemslib has an experimental feature for this: See client.py
for an example.
