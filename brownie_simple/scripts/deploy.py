from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    account = accounts[0]
    # deploy contract
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    print(simple_storage.retrieve())


def main():
    deploy_simple_storage()
