pragma solidity 0.8.14;

contract Password {

  string public password;

  constructor(string memory _password) public {
    password = _password;
  }

  function isPassword(string memory _password) external view returns (bool) {
    return (keccak256(abi.encodePacked((password))) == keccak256(abi.encodePacked((_password))));
  }

}
