from brownie import Lottery, network, config
from scripts.helper import get_accounts,get_contract


def deploy_lottery():
    account = get_accounts()
    lottery = Lottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deloyed Lottery!")

      


def main():
    deploy_lottery()
