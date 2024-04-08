from brownie import accounts, SimpleStorage, network, config


def test_deploy():
    # Arrange
    # account = accounts[0]
    account = get_account()
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def get_account():
    if network.show_active() == "development":
        return accounts[0];
    else:
        return accounts.add(config["wallets"]["from_key"])


def test_updating_storage():
    account = accounts[0]  # Arrange
    simple_storage = SimpleStorage.deploy({"from": account})  # Arrange
    transaction = simple_storage.store(15, {"from": account})  # Act
    transaction.wait(1)
    starting_value = simple_storage.retrieve()
    assert simple_storage.retrieve() == 15  # Assert
