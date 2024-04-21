## Lottery Project Explained
1. Users can enter the lottery ETH based USD feed
2. An admin will choose when the lottery is over
3. The lottery will select a random winner

### Way to do it
1. write contract
2. write a brownie config file and declare dependencies
3. add to `networks` in `brownie-config.yaml` file
4. add `mainnet-for` as `brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork="https://eth-mainnet.g.alchemy.com/v2/$ALCHEMY_PROJECT_ID" accounts=10 mnemonic=brownie port=8545`
5. run `brownie test -s --network mainnet-fork -W ignore` to test
6. create the `deploy.py` file
7. create the `helper.py` file
8. add the `get_accounts` function to get the accounts
9. declare `contract_to_mock` which is defined in the yaml file
10 create `get_contract` function in the `helper` which we will call from `deploy`
11. create `deploy_mocks` function to deply the mocks which is being called from `get_contract` fucntion
    a. the `get_contract` function work flow, if we are on test or development mode, it will deploy and get the latest contract
       else, it will get the contract from the address
12. add all the mocks to `contract_to_mock` in helper.py
13. run `brownie compile` to check everything is all right or not
14. add all the files into `contracts/test`
15 in `deploy.py` add the fee and keyhash
16. If you want tot publish this add the last bit of line `publish_source=config["networks"][network.show_active()].get("verify", False),` this says
get that verify key, not not there pass false
17. in `deploy.py` write `start_lottery` function to start the lottery, this will be tratsaction so add `wait(1)`. and write the rest of the lottery functions
18. to end the lottery we need few things, one is link token to fund the contract
19. in `helper.py` write `fund_with_link` 
20. when we call the `endLottery` function it will make a request to a chaninlink node and the chainlink node willr esponse by calling `fulfillRandomness`, we we have to wait for it to response



### Testing Options
1. `mainnet-fork`
2. with mocks
3. `testnet`