import pytest
import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from pypolkasidecar.pypolkasidecar import PyPolkaSideCar

class TestNode:
    def test_balance(self):
        self.api = PyPolkaSideCar("http://127.0.0.1:8080")

        balance = self.api.accounts.get_balance_info("121H8X5fK3ovF4PdyYfXpgE3BtN5VHRdYSALpznMPCP9YMq5")
        print(balance.free)
        assert(balance != None)

    def test_accounts(self):
        self.api = PyPolkaSideCar("http://127.0.0.1:8080")
        stakingInfo = self.api.accounts.get_staking_info("121H8X5fK3ovF4PdyYfXpgE3BtN5VHRdYSALpznMPCP9YMq5")
        print("controller", stakingInfo.controller)
        assert(stakingInfo != None)

if __name__ == "__main__":
    TestNode().test_balance()
    TestNode().test_accounts()