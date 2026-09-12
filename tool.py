"""Build and compare SHA-256 file manifests."""
from __future__ import annotations
import hashlib
from pathlib import Path


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""): hasher.update(block)
    return hasher.hexdigest()

def build(root: str) -> dict[str, dict[str, int | str]]:
    base = Path(root)
    return {str(path.relative_to(base)): {"bytes": path.stat().st_size, "sha256": digest(path)} for path in sorted(base.rglob("*")) if path.is_file()}

def compare(left: dict, right: dict) -> dict[str, list[str]]:
    return {"added": sorted(set(right)-set(left)), "removed": sorted(set(left)-set(right)), "changed": sorted(key for key in set(left)&set(right) if left[key] != right[key])}

if __name__ == "__main__":
    import argparse, json
    parser=argparse.ArgumentParser(); parser.add_argument("directory"); args=parser.parse_args(); print(json.dumps(build(args.directory), indent=2, sort_keys=True))
