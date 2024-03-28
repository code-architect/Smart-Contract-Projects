// SPDX-License-Identifier: MIT
pragma solidity >=0.6.6 <0.9.0;

import {AggregatorV3Interface} from "@chainlink/contracts@1.0.0/src/v0.8/shared/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract FundMe 
{
    using SafeMath for uint;
    address owner;
    
    mapping(address => uint) public addressToAmountFunded;
    address[] public funders;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner()
    {
        require(msg.sender == owner);
        _;
    }

    function fund() public payable 
    {
        //uint minimumUSD = 50 * 10 ** 18;
        //require(getConversionRate(msg.value) >= minimumUSD, "Please meet the minimum amount");
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    function getVersion() public view returns(uint256)
    {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0xB0C712f98daE15264c8E26132BCC91C40aD4d5F9);
        return priceFeed.version();
    }

    function getPrice() public view returns(uint256)
    {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0xB0C712f98daE15264c8E26132BCC91C40aD4d5F9);
        (,int256 answer, , ,) = priceFeed.latestRoundData();
        return uint256(answer);
    }

    function getConversionRate(uint256 ethAmount) public view returns(uint256)
    {
        uint256 ethPrice = getPrice();        
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;
        return ethAmountInUsd;
    }

    function withdrwl() payable public onlyOwner
    {        
        payable(msg.sender).transfer(address(this).balance);
        for(uint funderIndex = 0; funderIndex < funders.length; funderIndex++)
        {
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0);
    }

     

}