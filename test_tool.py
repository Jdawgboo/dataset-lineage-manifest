import tempfile, unittest
from pathlib import Path
from tool import build, compare

class ManifestTests(unittest.TestCase):
    def test_build_and_compare(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory); (path/'a.txt').write_text('a'); first=build(directory); (path/'a.txt').write_text('b'); (path/'b.txt').write_text('x'); second=build(directory)
            self.assertEqual(compare(first, second), {"added":["b.txt"], "removed":[], "changed":["a.txt"]})

if __name__ == "__main__": unittest.main()
