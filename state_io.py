"""Read owned state without hiding corruption; replace complete files atomically."""

import gzip
import json
import os
import tempfile
from pathlib import Path
from typing import Any


def decode_json_bytes(raw: bytes) -> Any:
    """Parse JSON, including gzip-compressed job stores."""
    if raw.startswith(b"\x1f\x8b"):
        raw = gzip.decompress(raw)
    return json.loads(raw)


def encode_json_gzip(payload: Any) -> bytes:
    """Compact JSON plus gzip, so large job stores stay under GitHub's 100MB blob limit."""
    body = (json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")
    return gzip.compress(body, mtime=0)


def read_json(path: Path, default: Any) -> Any:
    try:
        return decode_json_bytes(path.read_bytes())
    except FileNotFoundError:
        return default


def atomic_write(path: Path, data: bytes) -> None:
    """Keep the previous file intact if serialization or writing fails.

    Unique sibling files prevent temp-name collisions; pipeline scheduling
    still owns serialization of read/modify/write operations.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=f".{path.name}.", delete=False) as pending:
        temporary = Path(pending.name)
        try:
            pending.write(data)
            pending.flush()
            os.fsync(pending.fileno())
            pending.close()
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)
