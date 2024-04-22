from brownie import Lottery, accounts, config, network, exceptions
from web3 import Web3
from scripts.deploy import deploy_lottery
from scripts.helper import LOCAL_BLOCKCHAIN_ENVIRONMENT, get_accounts, fund_with_link, get_contract
import pytest
import time

def test_can_pick_winner(lottery_contract):
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        pytest.skip()
    account = get_accounts()
    lottery_contract.startLottery({"from": account})
    lottery_contract.enter(
        {"from": account, "value": lottery_contract.getEntranceFee()}
    )
    lottery_contract.enter(
        {"from": account, "value": lottery_contract.getEntranceFee()}
    )
    fund_with_link(lottery_contract)
    lottery_contract.endLottery({"from": account})
    time.sleep(180)
    assert lottery_contract.recentWinner() == account
    assert lottery_contract.balance() == 0