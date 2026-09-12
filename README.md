# Dataset Lineage Manifest

Create deterministic file manifests containing relative paths, sizes, and SHA-256 hashes, then compare two manifests.

```bash
python tool.py data_directory
python -m unittest -v
```

The utility reads local files only. Hashing large directories can be expensive and should be scheduled accordingly.
