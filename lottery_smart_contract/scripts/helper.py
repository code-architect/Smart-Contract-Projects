from brownie import accounts, network, config, MockV3Aggregator, Contract, VRFCoordinatorMock, LinkToken
from web3 import Web3


FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = 200000000000


def get_accounts(index=None, id=None):
    if index:
        return accounts[index]    
    if id:
        return accounts.load(id)    
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT or network.show_active() in FORKED_LOCAL_ENVIRONMENT:
        return accounts[0]    
    
    return accounts.add(config["wallets"]["from_key"])


contract_to_mock = {
    "eth_usd_price_feed": MockV3Aggregator,
    "vrf_coordinator": VRFCoordinatorMock,
    "link_token": LinkToken,
}


def get_contract(contract_name):
    """
    This will grab the contract addresses from the brownie config if defiend, 
    otherwise it will deploy a mock version of the contract and return that mock contract
    
    Args:
        contarct_name (strings): name of the contract
    Returns:
        brownie.network.contract.ProjectContract: The most recently deployed version of this contract
    """
    contract_type = contract_to_mock[contract_name];
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        if len(contract_type) <= 0:
            deploy_mocks()
        contract = contract_type[-1] # this somier to saying MockV3Aggregator[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        contract = Contract.from_abi(contract_type._name, contract_address, contract_type.abi)
    return contract


def deploy_mocks(decimals=DECIMALS, initial_value=STARTING_PRICE):
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks")
    account = get_accounts()
    MockV3Aggregator.deploy(DECIMALS, Web3.to_wei(STARTING_PRICE, "ether"), {"from": account})
    print("Mock deployed")