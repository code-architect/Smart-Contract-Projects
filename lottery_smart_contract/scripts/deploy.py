from brownie import Lottery, network, config
from scripts.helper import get_accounts,get_contract


def deploy_lottery():
    account = get_accounts()
    lottery = Lottery.deploy(
        get_contract(),
        {"from": account}
    )

   


def main():
    pass
