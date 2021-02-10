import requests
import json

class Node:
    def __init__(self, api):
        self.__api = api

    def get_version(self):
        req = requests.get(self.__api.address + "/node/version")
        if (req.ok):
            return json.loads(req.text)
        else:
            print("error Code:{code} Message:{message}".format(code=req.code, message=req.text))
            return {}

    def get_transaction_pool(self):
        req = requests.get(self.__api.address + "/node/transaction-pool")
        if (req.ok):
            return json.loads(req.text)
        else:
            print("error Code:{code} Message:{message}".format(code=req.code, message=req.text))
            return {}

    def get_network(self):
        req = requests.get(self.__api.address + "/node/network")
        if (req.ok):
            return json.loads(req.text)
        else:
            print("error Code:{code} Message:{message}".format(code=req.code, message=req.text))
            return {}