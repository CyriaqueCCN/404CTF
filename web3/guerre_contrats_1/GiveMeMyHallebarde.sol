pragma solidity ^0.7.6;

import "./FreeMoney.sol";

contract GiveMeMyHallebarde {

    FreeMoney public fm;
    address me;

    constructor(address _fm, address _me) {
	fm = FreeMoney(_fm);
	me = _me;
    }
    
    receive() external payable {
	fm.enterHallebarde();
    }
}
