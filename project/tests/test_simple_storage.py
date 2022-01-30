from brownie import SimpleStorage, accounts

def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    assert(starting_value == expected)
    # Asserting

def test_update():
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    simple_storage.store(22, {"from": account})
    expected = 22
    assert(simple_storage.retrieve() == expected)