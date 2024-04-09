from brownie import FundMe, accounts, network, config, MockV3Aggregator
from scripts.helpful import get_accounts


def deploy_fund_me():
    # account = get_accounts()
    account = accounts[0]
    # fund_me = FundMe.deploy("0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e",{"from": account}, publish_source=True)
    # pass the price feed
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        print(f"The active network is {network.show_active()}")
        print("Deploying mocks")
        mock_aggregator = MockV3Aggregator.deploy(18, 2000000000000000000, {"from": account})
        price_feed_address = mock_aggregator.address
        print("Mock deployed")

    fund_me = FundMe.deploy(price_feed_address, {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))


def main():
    deploy_fund_me()
