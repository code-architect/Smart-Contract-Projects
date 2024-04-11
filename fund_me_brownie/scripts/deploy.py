from brownie import FundMe, accounts, network, config, MockV3Aggregator
from scripts.helpful import get_accounts, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENT
# from icecream import ic



def deploy_fund_me():
    account = get_accounts()
    # account = accounts[0]
    # fund_me = FundMe.deploy("0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e",{"from": account}, publish_source=True)
    # pass the price feed

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks(account)
        print(MockV3Aggregator[-1].address)
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(price_feed_address, {"from": account},
                            publish_source=config["networks"][network.show_active()].get("verify"))
    return fund_me


def main():
    deploy_fund_me()
