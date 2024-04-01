import json
from rich import print
from solcx import compile_standard, install_solc
from web3 import Web3

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
chain_id = 5777
my_address = "0xb6613a52D93954722CD1fDAF8F64e299f7Ee03C8"
private_key = "0x295aae2bc2d8cd049af68694ecb9b88220ddc722dcbb5d74ca9da99590662fe6"
#
# # create contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# get the latest transaction
nonce = w3.eth.get_transaction_count(my_address)
print(abi)
# build a transaction
# sign a transaction
# send a transaction
