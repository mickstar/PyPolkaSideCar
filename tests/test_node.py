import pytest
import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
from pypolkasidecar.pypolkasidecar import PyPolkaSideCar

class TestNode:
    def test_version(self):
    
        self.api = PyPolkaSideCar("http://127.0.0.1:8080")

        version = self.api.node.get_version()
        print(version)
        assert version["chain"] == "Polkadot"
        assert version["clientImplName"] == "parity-polkadot"

# if __name__ == "__main__":
#     test_version(api)