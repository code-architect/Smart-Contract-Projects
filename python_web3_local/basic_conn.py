from web3 import Web3
from icecream import ic

url = "https://mainnet.infura.io/v3/41a2320fc92f4bd2b228ff5d754e5040"
web3 = Web3(Web3.HTTPProvider(url))
#  check if connected
# ic(w3.is_connected())

# block number
# ic(w3.eth.block_number)

balance = web3.eth.get_balance("0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5")
we_bal = web3.from_wei(balance, "ether")
ic(we_bal)