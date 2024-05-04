import json
from solcx import compile_standard, install_solc
from icecream import ic
from web3 import Web3

contract_path = 'StorageFund.sol'
install_solc('0.8.12')
with open(contract_path, 'r') as file:
    contract_file = file.read()

compiled_solidity = compile_standard({
    "language": "Solidity",
    "sources": {
        "StorageFund.sol": {  # Use string as key, dictionary as value
            "content": contract_file
        }
    },
    "settings": {
        "outputSelection": {
            "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
        }
    }
}, solc_version="0.8.12")

with open("compiled_contract.json", "w") as file:
    json.dump(compiled_solidity, file)

url = "http://127.0.0.1:7545"
# url = "http://localhost:8545"
w3 = Web3(Web3.HTTPProvider(url))

abi = compiled_solidity['contracts']['StorageFund.sol']['StorageFund']['abi']
bytecode = compiled_solidity['contracts']['StorageFund.sol']['StorageFund']['evm']['bytecode']['object']

StorageFund = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get Ganache account (assuming you have at least one account unlocked)
account = w3.eth.account.from_key("0xac848186453a72650841062f55cbc5daa03be133803e292fef0ccc3f71162345")
private_key = "0xac848186453a72650841062f55cbc5daa03be133803e292fef0ccc3f71162345"
# deploy it
txn_params = {
    'from': account.address,
    'gas': 1000000,  # Adjust gas limit if needed
    'gasPrice': w3.eth.gas_price,
    'nonce': w3.eth.get_transaction_count(account.address)
}


tx = StorageFund.constructor(account.address).build_transaction(txn_params)
tx_signed = w3.eth.account.sign_transaction(tx, private_key=private_key)
sent_tx = w3.eth.send_raw_transaction(tx_signed.rawTransaction)
ic(sent_tx)
