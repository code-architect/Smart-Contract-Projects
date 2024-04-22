from brownie import Lottery, accounts, config, network, exceptions
from web3 import Web3
from scripts.deploy import deploy_lottery
from scripts.helper import LOCAL_BLOCKCHAIN_ENVIRONMENT, get_accounts, fund_with_link, get_contract
import pytest


def test_get_entrance_fee():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        pytest.skip()
    # Arrange
    lottery = deploy_lottery()
    # Act
    expected_entrance_fee = Web3.to_wei(0, "ether")
    entrance_fee = lottery.getEntranceFee()
    # Assert
    assert expected_entrance_fee == entrance_fee


def test_cant_enter_unless_started():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        pytest.skip()
    # Arrange
    lottery = deploy_lottery()
    # Act / Assert
    with pytest.raises(exceptions.VirtualMachineError):
        lottery.enter({"from": get_accounts(), "value": lottery.getEntranceFee()})
        

def test_can_start_enter_unless_started():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        pytest.skip()
    # Arrange
    lottery = deploy_lottery()
    account = get_accounts()
    lottery.startLottery({"from": account})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    assert lottery.players(0) == account
    
    
def test_can_end_lottery():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        pytest.skip()
    # Arrange
    lottery = deploy_lottery()
    account = get_accounts()
    lottery.startLottery({"from": account})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    fund_with_link(lottery)
    lottery.endLottery({"from": account})
    assert lottery.lottery_state() == 2


def test_can_pick_lottery_winner():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        pytest.skip()
    # Arrange
    lottery = deploy_lottery()
    account = get_accounts()
    lottery.startLottery({"from": account})
    for n in range(1, 5):
        lottery.enter({"from": get_accounts(index=n), "value": lottery.getEntranceFee()})
        print(f"The accoutn is {get_accounts(index=n)} and the number is {n}\n")
    fund_with_link(lottery)
    transaction = lottery.endLottery({"from": account})
    request_id = transaction.events["RequestedRandomness"]["requestId"]
    get_contract("vrf_coordinator").callBackWithRandomness(request_id, 777, lottery.address, {"from": account})
    print(lottery.recentWinner())
    starting_account_balance = get_accounts(2).balance()
    balance_of_lottery = lottery.balance()
    assert lottery.recentWinner() == get_accounts(2)
    assert lottery.balance() == 0
    assert get_accounts(2).balance == starting_account_balance + balance_of_lottery


