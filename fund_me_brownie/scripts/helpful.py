from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3


DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]


def get_accounts():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks(account):
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, Web3.to_wei(STARTING_PRICE, "ether"), {"from": account})
    print("Mock deployed")

