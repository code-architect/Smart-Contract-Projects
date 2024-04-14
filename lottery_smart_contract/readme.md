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

### Testing Options
1. `mainnet-fork`
2. with mocks
3. `testnet`