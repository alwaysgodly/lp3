// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// C3: Customer Bank Account
// Functions: deposit, withdraw and display balance.
contract BankAccount {
    address public owner;
    uint256 private balance;

    event Deposited(address indexed account, uint256 amount);
    event Withdrawn(address indexed account, uint256 amount);

    constructor() {
        owner = msg.sender;
    }

    function deposit() external payable {
        require(msg.value > 0, "Deposit must be greater than zero");
        balance += msg.value;
        emit Deposited(msg.sender, msg.value);
    }

    function withdraw(uint256 amount) external {
        require(msg.sender == owner, "Only account owner can withdraw");
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= balance, "Insufficient balance");

        balance -= amount;
        (bool success, ) = payable(owner).call{value: amount}("");
        require(success, "Transfer failed");

        emit Withdrawn(owner, amount);
    }

    function displayBalance() external view returns (uint256) {
        return balance;
    }
}
