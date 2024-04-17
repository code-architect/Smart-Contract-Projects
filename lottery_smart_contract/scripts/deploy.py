from brownie import Lottery, network, config
from scripts.helper import get_accounts,get_contract


def deploy_lottery():
    account = get_accounts()
    lottery = Lottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
        {"from": account}
    )

   


def main():
    pass
