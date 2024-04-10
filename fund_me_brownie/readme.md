# Brownie Commands
1. To compile smart contract `brownie compile`
2. Run scripts or deploy code `brownie run`
3. Add accounts natively `brownie accounts new testAcc`
4. Account list `brownie accounts list`
5. Delete account `brownie accounts delete testAcc`
6. Run Deploy script `brownie run scripts\deploy.py`
7. For test files add `test` at the beginning
8. OK! Don't do this in a production environment. Please Don't: `brownie test -W ignore` This is to ignore the warnings from python 3.12
9. Get all the network list `brownie networks list`
10. If you want to test just one function `brownie test -k  function_name`
11. Use `brownie test -s -W ignore` to get moe information. All of this is from PyTest so just go through docs
12. Deploy to testnet, just add the project key to `.env` file, and run `brownie run scripts\deploy.py --network rinkeby` [rinkeby for me]
13. To use brownie console use `brownie console`
14. Pull monks from chainlink mix `https://github.com/smartcontractkit/chainlink-mix/tree/main/contracts/test`
15. To add a new network `brownie networks add Ethereum ganache-local host=http://127.0.0.1:7545 chainid=1337`