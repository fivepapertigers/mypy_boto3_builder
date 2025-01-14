import asyncio
from types import TracebackType
from typing import IO, Any, Dict, Mapping, Optional, Tuple, Type, TypeVar, Union

from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey

_R = TypeVar("_R")

RANGE_REGEX: Any
AES_BLOCK_SIZE: int
AES_BLOCK_SIZE_BYTES: int
JAVA_LONG_MAX_VALUE: int

class DummyAIOFile:
    file: IO[Any]
    def __init__(self, data: bytes) -> None: ...
    async def read(self, n: int = ...) -> bytes: ...
    async def readany(self) -> bytes: ...
    async def readexactly(self, n: int) -> bytes: ...
    async def readchunk(self) -> bytes: ...

class DecryptError(Exception): ...

class CryptoContext:
    async def setup(self) -> None: ...
    async def close(self) -> None: ...
    async def get_decryption_aes_key(
        self, key: bytes, material_description: Dict[str, Any]
    ) -> bytes: ...
    async def get_encryption_aes_key(self) -> Tuple[bytes, Dict[str, str], str]: ...

class AsymmetricCryptoContext(CryptoContext):
    public_key: RSAPublicKey
    private_key: RSAPrivateKey
    def __init__(
        self,
        public_key: Optional[RSAPublicKey] = ...,
        private_key: Optional[RSAPrivateKey] = ...,
        loop: Optional[asyncio.AbstractEventLoop] = ...,
    ) -> None: ...
    async def get_decryption_aes_key(
        self, key: bytes, material_description: Dict[str, Any]
    ) -> bytes: ...
    async def get_encryption_aes_key(self) -> Tuple[bytes, Dict[str, str], str]: ...
    @staticmethod
    def from_der_public_key(data: bytes) -> RSAPublicKey: ...
    @staticmethod
    def from_der_private_key(data: bytes, password: Optional[str] = ...) -> RSAPrivateKey: ...

class SymmetricCryptoContext(CryptoContext):
    key: bytes
    def __init__(self, key: bytes, loop: Optional[asyncio.AbstractEventLoop] = ...) -> None: ...
    async def get_decryption_aes_key(
        self, key: bytes, material_description: Dict[str, Any]
    ) -> bytes: ...
    async def get_encryption_aes_key(self) -> Tuple[bytes, Dict[str, str], str]: ...

class KMSCryptoContext(CryptoContext):
    kms_key: str
    authenticated_encryption: bool
    def __init__(
        self,
        keyid: Optional[str] = ...,
        kms_client_args: Optional[Dict[str, Any]] = ...,
        authenticated_encryption: bool = ...,
    ) -> None: ...
    async def setup(self) -> None: ...
    async def close(self) -> None: ...
    async def get_decryption_aes_key(
        self, key: bytes, material_description: Dict[str, Any]
    ) -> bytes: ...
    async def get_encryption_aes_key(self) -> Tuple[bytes, Dict[str, str], str]: ...

class MockKMSCryptoContext(KMSCryptoContext):
    aes_key: bytes
    material_description: Dict[str, Any]
    encrypted_key: bytes
    authenticated_encryption: bool
    def __init__(
        self,
        aes_key: bytes,
        material_description: Dict[str, Any],
        encrypted_key: bytes,
        authenticated_encryption: bool = ...,
    ) -> None: ...
    async def setup(self) -> None: ...
    async def close(self) -> None: ...
    async def get_decryption_aes_key(
        self, key: bytes, material_description: Dict[str, Any]
    ) -> bytes: ...
    async def get_encryption_aes_key(self) -> Tuple[bytes, Dict[str, str], str]: ...

class S3CSE:
    def __init__(
        self, crypto_context: CryptoContext, s3_client_args: Optional[Dict[str, Any]] = ...
    ) -> None: ...
    async def setup(self) -> None: ...
    async def close(self) -> None: ...
    async def __aenter__(self: _R) -> _R: ...
    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> None: ...
    async def get_object(self, Bucket: str, Key: str, **kwargs: Any) -> Dict[str, Any]: ...
    async def put_object(
        self,
        Body: Union[bytes, IO[Any]],
        Bucket: str,
        Key: str,
        Metadata: Optional[Mapping[str, Any]] = ...,
        **kwargs: Any,
    ) -> Any: ...
