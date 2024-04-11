from brownie import FundMe, network, config,MockV3Aggregator
from scripts.helpful import get_accounts, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENT


def test_can_fund_and_withdraw():
    account = get_accounts()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks(account)
        print(MockV3Aggregator[-1].address)
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(price_feed_address, {"from": account},
                            publish_source=config["networks"][network.show_active()].get("verify"))
    entrance_fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0
