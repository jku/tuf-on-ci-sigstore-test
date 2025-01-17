# A tuf-on-ci test repo using sigstore signing 

A completely keyless TUF repository:
* Repository signs online roles with sigstore using the ambient GitHub workflow identity
* offline signers use interactive sigstore identities

A typical client is not at the moment compatible with the repository but python-tuf/securesystemslib
has an experimental feature that does. See client.py for an example