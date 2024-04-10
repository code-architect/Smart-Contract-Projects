from brownie import FundMe
from scripts.helpful import get_accounts


def fund():
    fun_me = FundMe[-1]
    account = get_accounts()
    entrance_fee = fun_me.getEntranceFee()
    print(entrance_fee)
    fun_me.fund({"from": account, "value": entrance_fee})


def main():
    fund()
