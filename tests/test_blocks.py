import pytest
import os,sys
testdir = os.path.dirname(__file__)
srcdir = '../'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
from pypolkasidecar.pypolkasidecar import PyPolkaSideCar

class TestBlock:
    def test_get_events(self):
    
        self.api = PyPolkaSideCar("http://127.0.0.1:8080")

        block = self.api.blocks.get_block(2759346)
        events = block.get_events()
        for event in events:
            print(event)
            if (event.method.method == "Transfer"):
                print(event.source)

        assert len(block.get_events()) == 21
        print(block.get_events())

if __name__ == "__main__":
    TestBlock().test_get_events()