import json
import os
from rich import print
from solcx import compile_standard, install_solc
from web3 import Web3
from dotenv import load_dotenv

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
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 1337
my_address = os.getenv("MY_ADDRESS")

# # create contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# get the latest transaction
nonce = w3.eth.get_transaction_count(my_address)

# build a transaction
transaction = SimpleStorage.constructor().build_transaction({
    "chainId": chain_id,
    "from": my_address,
    "nonce": nonce})

# sign a transaction
signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=os.getenv("PRIVATE_KEY"))

# send a transaction
tx_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
