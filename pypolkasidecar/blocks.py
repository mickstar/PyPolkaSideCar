import requests
import json

class Blocks:
    def __init__(self, api):
        self.__api = api

    def get_block(self, blockNumber):
        req = requests.get(self.__api.address + "/blocks/{blockNumber}".format(blockNumber=blockNumber))
        if (req.ok):
            return Block(json.loads(req.text))
        else:
            print("error Code:{code} Message:{message}".format(code=req.code, message=req.text))
            return []

    def get_head(self):
        req = requests.get(self.__api.address + "/blocks/head")
        if (req.ok):
            return Block(req.text)
        else:
            print("error Code:{code} Message:{message}".format(code=req.code, message=req.text))
            return None

class Block:
    def __init__(self, blockJson):
        self.raw_data = blockJson
        self.number = self.raw_data["number"]
        self.hash = self.raw_data["hash"]
        self.parentHash = self.raw_data["parentHash"]
        self.stateRoot = self.raw_data["stateRoot"]
        self.extrinsicsRoot = self.raw_data["extrinsicsRoot"]

        self.authorId = None
        if "authorId" in blockJson:
            self.authorId = self.raw_data["authorId"]
        self.logs = [Log(log) for log in self.raw_data["logs"]]
        self.onInitialize = self.raw_data["onInitialize"]

        self.extrinsics = [Extrinsic(extrinsic) for extrinsic in self.raw_data["extrinsics"]]
        self.onFinalize = self.raw_data["onFinalize"]
        self.finalized = self.raw_data["finalized"]

    def get_events(self):
        return [event for extrinsic in self.extrinsics for event in extrinsic.events]

class Extrinsic:
    def __init__(self, extrinsicObject):
        self.raw_data = extrinsicObject
        self.method = ExtrinsicMethod(extrinsicObject["method"])
        self.signature = extrinsicObject["signature"]
        self.nonce = extrinsicObject["nonce"]
        self.args = extrinsicObject["args"]
        self.tip = extrinsicObject["tip"]
        self.hash = extrinsicObject["hash"]
        self.info = extrinsicObject["info"]
        self.events = [Extrinsic.__makeEvent(event) for event in extrinsicObject["events"]]
        self.success = extrinsicObject["success"]
        self.paysFee = extrinsicObject["paysFee"]


    def __makeEvent(eventObject):
        if eventObject["method"]["pallet"] == "balances" and eventObject["method"]["method"] == "Transfer":
            return BalanceTranferEvent(eventObject)
        elif eventObject["method"]["pallet"] == "balances" and eventObject["method"]["method"] == "Endowed":
            return BalanceEndowedEvent(eventObject)
        elif eventObject["method"]["pallet"] == "balances" and eventObject["method"]["method"] == "Deposit":
            return BalanceDepositEvent(eventObject)
        elif eventObject["method"]["pallet"] == "system" and eventObject["method"]["method"] == "NewAccount":
            return SystemNewAccountEvent(eventObject)
        elif eventObject["method"]["pallet"] == "staking" and eventObject["method"]["method"] == "Reward":
            return stakingRewardEvent(eventObject)
        else:
            return Event(eventObject)

# TODO
# EVENT TYPES SUBCLASSES

class ExtrinsicMethod:
    def __init__(self, methodObject):
        self.pallet = methodObject["pallet"]
        self.method = methodObject["method"]

    def __str__(self):
        return "{pallet}({method})".format(pallet=self.pallet, method=self.method)


class Event:
    def __init__(self, eventObject):
        self.raw_data = eventObject
        self.method = ExtrinsicMethod(eventObject["method"])
        self.data = eventObject["data"]

    def __str__(self):
        return str(self.method)

    def getAction(self):
        return str(self.method)

class BalanceTranferEvent (Event):
    def __init__ (self, eventObject):
        super().__init__(eventObject)
        self.source = self.data[0]
        self.destination = self.data[1]
        self.amount = self.data[2]

class BalanceEndowedEvent (Event):
    def __init__ (self, eventObject):
        super().__init__(eventObject)
        self.address = self.data[0]
        self.amount = self.data[1]

class BalanceDepositEvent (Event):
    def __init__ (self, eventObject):
        super().__init__(eventObject)
        self.address = self.data[0]
        self.amount = self.data[1]

class SystemNewAccountEvent (Event):
    def __init__ (self, eventObject):
        super().__init__(eventObject)
        self.address = self.data[0]

class stakingRewardEvent (Event):
    def __init__ (self, eventObject):
        super().__init__(eventObject)
        self.address = self.data[0]
        self.amount = self.data[1]

class stakingBondedEvent (Event):
    def __init__ (self, eventObject):
        super().__init__(eventObject)
        self.address = self.data[0]
        self.amount = self.data[1]   

class Log:
    def __init__(self, logObject):
        self.type = logObject["type"]
        self.index = logObject["index"]
        self.value = logObject["value"]