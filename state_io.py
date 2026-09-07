"""Read owned state without hiding corruption; replace complete files atomically."""

import json
import os
import tempfile
from pathlib import Path
from typing import Any


def read_json(path: Path, default: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
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
