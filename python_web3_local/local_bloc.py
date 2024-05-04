import json
from web3 import Web3
from icecream import ic


url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(url))

ic(web3.is_connected())

account_1 = "0xbB4eB1BCcf31cb9aad39c50089b4C0849eeC3383"
account_2 = "0xb6613a52D93954722CD1fDAF8F64e299f7Ee03C8"
p_key_2 = "0x295aae2bc2d8cd049af68694ecb9b88220ddc722dcbb5d74ca9da99590662fe6"
p_key_1 = "0x676af057cca490e3edf125b3f1c53c6276ad6122aeb96fc7424c8942cb3d3cf8"

# get the nonce
nonce = web3.eth.get_transaction_count(account_1)
# build a trans action
tx = {
    'nonce': nonce,
    'to': account_2,
    "value": web3.to_wei(1, 'ether'),
    'gas': 5000000,
    'gasPrice': web3.to_wei('50', 'gwei')
}
#  sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, p_key_1)
# send the transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
# get the tx has
ic(tx_hash)
