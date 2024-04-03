import json
import os
from rich import print
from rich.console import Console
from solcx import compile_standard, install_solc
from web3 import Web3
from dotenv import load_dotenv

console = Console()
load_dotenv()

install_solc('0.8.0')
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# Compile Our Solidity
compile_sole = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.8.0",
)
with open("compiled_code.json", "w") as file:
    json.dump(compile_sole, file)

# get bytecode
bytecode = compile_sole["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get ABI
abi = compile_sole["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

#  connecting to ganache
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
chain_id = 1337
my_address = os.getenv("MY_ADDRESS")

# # create contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# get the latest transaction
nonce = w3.eth.get_transaction_count(my_address)

# build a transaction start --->
transaction = SimpleStorage.constructor().build_transaction({
    "chainId": chain_id,
    "from": my_address,
    "nonce": nonce})

# sign a transaction
signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=os.getenv("PRIVATE_KEY"))

# send a transaction
console.print("Deploying Contract!", style="bold red")
tx_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
console.print("Deployed", style="bold red")
# <--- ends
# working with contract
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# just calling a function, not changing any state
console.print(simple_storage.functions.retrieve().call())

console.print("Updating Contract", style="bold blue")
store_transaction = simple_storage.functions.store(15).build_transaction({
    "chainId": chain_id,
    "from": my_address,
    "nonce": nonce+1
})
signed_store_tx = w3.eth.account.sign_transaction(store_transaction, private_key=os.getenv("PRIVATE_KEY"))
transaction_hash = w3.eth.send_raw_transaction(signed_store_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
console.print("Updated", style="bold blue")
console.print("Result:", style="bold blue")
console.print(simple_storage.functions.retrieve().call())

print(tx_receipt)
