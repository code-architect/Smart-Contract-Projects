// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0 <0.9.0;

contract SimpleTask
{
    struct Person{
        uint age;
        string name;
        string city;
    }

    Person[] internal people;

    function addPeople(uint _age, string memory _name, string memory _city) public
    {
       // Create a new Person struct with the provided parameters 
       Person memory newPerson = Person(_age, _name, _city);
       people.push(newPerson);
    }

    function getPeopleDetails(uint _index) public view returns (uint, string memory, string memory)
    {
        require(_index < people.length, "Index is invalid");
        return (people[_index].age, people[_index].name, people[_index].city);
    }

}