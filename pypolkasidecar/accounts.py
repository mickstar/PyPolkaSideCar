import requests, json

class Accounts:
    def __init__(self, api):
        self.api = api

    def get_balance_info(self, address):
        endpoint = "{url}/accounts/{address}/balance-info".format(url=self.api.address, address=address)
        response = requests.get(endpoint)
        if response.ok:
            return BalanceInfo(json.loads(response.text))
        else:
            print("error Code:{code} Message:{message}".format(code=response.code, message=response.text))
            return None

    def get_staking_info(self, address):
        endpoint = "{url}/accounts/{address}/staking-info".format(url=self.api.address, address=address)
        response = requests.get(endpoint)
        if response.ok:
            return StakingInfo(json.loads(response.text))
        else:
            print("error Code:{code} Message:{message}".format(code=response.code, message=response.text))
            return None

class BalanceInfo:
    def __init__(self, accountBalanceObject):
        self.raw_data = accountBalanceObject
        self.at = accountBalanceObject["at"]
        self.nonce = accountBalanceObject["nonce"]
        self.tokenSymbol = accountBalanceObject["tokenSymbol"]
        self.free = int(accountBalanceObject["free"])
        self.reserved = accountBalanceObject["reserved"]
        self.miscFrozen = accountBalanceObject["miscFrozen"]
        self.feeFrozen = accountBalanceObject["feeFrozen"]
        self.locks = [BalanceLock(x) for x in accountBalanceObject["locks"]]

class BalanceLock:
    def __init__(self, lockObject):
        self.raw_data = lockObject
        self.id = lockObject["id"]
        self.amount = lockObject["amount"]
        self.reasons = lockObject["reasons"]


class StakingInfo:
    def __init__(self, stakingInfoObject):
        self.raw_data = stakingInfoObject
        self.at = stakingInfoObject["at"]
        self.controller = stakingInfoObject["controller"]
        self.rewardDestination = stakingInfoObject["rewardDestination"]
        self.numSlashingSpans = stakingInfoObject["numSlashingSpans"]
        self.staking = stakingInfoObject["staking"]

class StakingObject:
    def __init__(self, stakingObject):
        self.raw_data = stakingObject
        self.stash = stakingObject["stash"]
        self.total = stakingObject["total"]
        self.active = stakingObject["active"]
        self.unlocking = stakingObject["unlocking"]
        self.claimedRewards = stakingObject["claimedRewards"]