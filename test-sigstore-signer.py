from sigstore.oidc import IdentityToken
from securesystemslib.signer import (
    Signer,
    Key,
    SigstoreSigner,
    SigstoreKey,
    SIGNER_FOR_URI_SCHEME,
    KEY_FOR_TYPE_AND_SCHEME
)

# enable unstable sigstore signer
SIGNER_FOR_URI_SCHEME[SigstoreSigner.SCHEME] = SigstoreSigner
KEY_FOR_TYPE_AND_SCHEME[("sigstore-oidc", "Fulcio")] = SigstoreKey


key = Key.from_dict(
   "abcd",
   {
    "keytype": "sigstore-oidc",
    "keyval": {
     "identity": "https://github.com/jku/tuf-on-ci-sigstore-test/.github/workflows/online-sign.yml@refs/heads/main",
     "issuer": "https://token.actions.githubusercontent.com"
    },
    "scheme": "Fulcio"
   }
)


# ambient param is true by default so not needed
signer = Signer.from_priv_key_uri("sigstore:", key)


sig = signer.sign(b"")
print(sig)
