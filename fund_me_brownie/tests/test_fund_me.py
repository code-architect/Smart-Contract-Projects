from brownie import FundMe, network, config,MockV3Aggregator, accounts, exceptions
from scripts.helpful import get_accounts, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENT
import pytest
from scripts.deploy import deploy_fund_me


def test_can_fund_and_withdraw():
    account = get_accounts()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        pytest.skip("only for local network")
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
