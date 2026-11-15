// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// C4: Student Information using structure, array and fallback function.
contract StudentInformation {
    struct Student {
        uint256 rollNo;
        string name;
        uint256 age;
        string department;
    }

    Student[] private students;

    event StudentAdded(uint256 indexed rollNo, string name);
    event EtherReceived(address indexed sender, uint256 amount);

    function addStudent(
        uint256 _rollNo,
        string calldata _name,
        uint256 _age,
        string calldata _department
    ) external {
        require(bytes(_name).length > 0, "Name cannot be empty");

        students.push(Student({
            rollNo: _rollNo,
            name: _name,
            age: _age,
            department: _department
        }));

        emit StudentAdded(_rollNo, _name);
    }

    function getStudent(uint256 index)
        external
        view
        returns (uint256 rollNo, string memory name, uint256 age, string memory department)
    {
        require(index < students.length, "Invalid student index");
        Student storage s = students[index];
        return (s.rollNo, s.name, s.age, s.department);
    }

    function getStudentCount() external view returns (uint256) {
        return students.length;
    }

    // Fallback executes when calldata does not match any function selector.
    // It is payable so the contract can receive Ether with unmatched calldata.
    fallback() external payable {
        emit EtherReceived(msg.sender, msg.value);
    }

    // Receive executes when Ether is sent with empty calldata.
    receive() external payable {
        emit EtherReceived(msg.sender, msg.value);
    }
}
