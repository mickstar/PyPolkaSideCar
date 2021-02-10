from .node import Node
from .blocks import Blocks
from .accounts import Accounts

class PyPolkaSideCar:
    def __init__(self, address):
        self.address = address
        # just in case the user gives "http://127.0.0.1:8080/"
        if (self.address[-1] == "/"):
            self.address = self.address[:-1]

        self.node = Node(self)
        self.blocks = Blocks(self)
        self.accounts = Accounts(self)

    def get_client_version(self):
        return self.node.get_version()["clientVersion"]

    def get_chain(self):
        return self.node.get_version()["chain"]
    