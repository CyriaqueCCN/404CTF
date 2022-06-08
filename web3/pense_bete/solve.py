#!/usr/bin/env python3

from web3 import Web3
from solcx import compile_source

PID = "af9b1a98447e4354bbb472d5dde82d6b"
PSEC = "81bd2e4ddc524088a980fe7e90b28c0e"
PROV_WSS = "wss://ropsten.infura.io/ws/v3/af9b1a98447e4354bbb472d5dde82d6b"

C_ADDR = "0xB65E30DeD2cD7d5C4758082BACE737976F8b214B"
ABI_FILE = "intro.sol"

w3 = Web3(Web3.WebsocketProvider(PROV_WSS))


def main():
    with open(ABI_FILE, "r") as sol:
        src = sol.read()
        cpl = compile_source(src, ["abi"])
        cid, citf = cpl.popitem()
        abi = citf['abi']
    ctr = w3.eth.contract(address=C_ADDR, abi=abi)
    print(ctr.functions.password().call())
    
main()

