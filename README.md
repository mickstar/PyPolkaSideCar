
# PyPolkaSideCar

## Python Wrapper for Substrate Side Car

  

A very simple python wrapper for the substrate side car api

All calls are syncronous and mostly return POJOs.

Note - package is experimental and may change at any time.

## Usage

    from pypolkasidecar import PyPolkaSideCar
	
	api = PyPolkaSideCar("http://127.0.0.1:8080")
	
	print (api.blocks.get_head().hash)

### use case 1 - finding transactions in certain blocks

    api = PyPolkaSideCar("http://127.0.0.1:8080")
    for blockNumber in range(2759170, 2759180):
	    block = api.blocks.get_block(blockNumber)
	    transactions = [event for event in block.get_events() if event.getAction()=="balances(Transfer)"]
	    for transaction in transactions:
		    print("sent {amount} from {sender} to {receiver}"
			    .format(amount=transaction.amount, sender=transaction.source, receiver=transaction.destination)

## Licence
Released under GPLv3

## Credits
Michael Johnston <michael.johnston29@gmail.com>
2021
