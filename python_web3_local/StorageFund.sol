// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.8.2 <0.9.0;

/**
 * @title Storage
 * @dev Store & retrieve value in a variable
 * @custom:dev-run-script ./scripts/deploy_with_ethers.ts
 */
contract StorageFund {

    address public owner;
    uint public balance;
    mapping(address => uint) public deposits;

    constructor(address _owner)
    {
        owner = _owner;
    }

    // Function to deposit funds into the contract
    function deposit() public payable {
        require(msg.value > 0, "amount has to be greater then 0" );
        deposits[msg.sender] += msg.value;
        balance += msg.value;
    }

    // Function to withdraw funds from the contract
    function withdraw(address payable _to, uint _amount) public {
        require(msg.sender == owner, "Only owner can withdraw");
        require(_amount <= balance, "Insufficient balance");

        _to.transfer(_amount);
        balance -= _amount;
    }

    // Function to allow owner to withdraw all funds from the contract
    function withdrawAll() public {
        require(msg.sender == owner, "Only owner can withdraw");

        payable(owner).transfer(balance);
        balance = 0;
    }
}
