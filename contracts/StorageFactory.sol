// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0 <0.9.0;

import "./SimpleTask.sol";
contract StorageFactory 
{
    SimpleTask[] public simpleStorageArray;

    function createSimpleTaskContract() public 
    {        
        SimpleTask simpleTask = new SimpleTask();
        simpleStorageArray.push(simpleTask);
    }

    function sfaddPeople(uint _simpleStorageIndex, uint _age, string memory _name, string memory _city) public 
    {
        SimpleTask simpleTask = SimpleTask(address(simpleStorageArray[_simpleStorageIndex]));
        simpleTask.addPeople(_age, _name, _city);
    }

    function sfRetrive(uint _simpleStorageIndex, uint _index) public view returns (uint, string memory, string memory)
    {
         SimpleTask simpleTask = SimpleTask(address(simpleStorageArray[_simpleStorageIndex]));
         return simpleTask.getPeopleDetails(_index);
    }



    // function storageFactoryStore(uint _simpleStorageIndex, uint _simpleStorageNumber) public
    // {
    //     SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
    //     simpleStorage.store(_simpleStorageNumber);
    // }

    // function retreiveFactoryGet(uint _simpleStorageIndex) public view returns (uint)
    // {
    //     SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
    //     return simpleStorage.retrieve();
    // }
}