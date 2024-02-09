// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0 <0.9.0;

import "./SImpleStorage.sol";
contract StorageFactory 
{
    SimpleStorage[] public simpleStorageArray;

    function createSimpleTaskContract() public 
    {        
        SimpleStorage simpleTask = new SimpleStorage();
        simpleStorageArray.push(simpleTask);
    }

    function storageFactoryStore(uint _simpleStorageIndex, uint _simpleStorageNumber) public
    {
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        simpleStorage.store(_simpleStorageNumber);
    }

    function retreiveFactoryGet(uint _simpleStorageIndex) public view returns (uint)
    {
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        return simpleStorage.retrieve();
    }
}