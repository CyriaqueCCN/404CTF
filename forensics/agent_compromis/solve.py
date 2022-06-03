#!/usr/bin/env python3

import dpkt
import binascii

# for an unknown reason, dpkt didnt want to work with the pcapng file
# so I had to run `editcap -F pcap capture-reseau.pcapng res.pcap` and work with that
#CAP_FILE = "capture-reseau.pcapng"
CAP_FILE = "res.pcap"

RES_SRC = "./exfiltration/" # make sure that folder exists
BAD_VALUE = ""
SEARCHED_DNS = ".hallebarde.404ctf.fr"
START_EXFIL = "never-gonna-give-you-up"
START_FILE = "626567696E"
END_FILE = "656E64"

def dns_value(p):
    eth = dpkt.ethernet.Ethernet(p)
    if not isinstance(eth.data, dpkt.ip.IP):
        return BAD_VALUE
    ip = eth.data
    if isinstance(ip.data, dpkt.udp.UDP):
        rd = ip.data
    elif isinstance(ip.data, dpkt.tcp.TCP):
        rd = ip.data
    else:
        return BAD_VALUE
    if len(rd.data) < 12: # min len for a dns buffer is 12
        return BAD_VALUE
    try:
        dns = dpkt.dns.DNS()
        dns.unpack(rd.data)
    except:
        return BAD_VALUE
    if len(dns.qd) < 1:
        return BAD_VALUE
    q = dns.qd[0]
    if len(dns.an) > 0:
        if SEARCHED_DNS in q.name:
            return q.name.removesuffix(SEARCHED_DNS)
    return BAD_VALUE

def add_to_file(fname, r):
    with open(RES_SRC + fname, "ab") as f:
        f.write(binascii.unhexlify(r))

def get_fname(r):
    return binascii.unhexlify(r).decode()

def extract_dns(pcap):
    cfname = ""
    is_fname = False
    for _, p in pcap:
        res = dns_value(p)
        if res == BAD_VALUE:
            continue
        print(res)
        if res == START_EXFIL:
            is_fname = True
            continue
        if is_fname:
            cfname = get_fname(res)
            is_fname = False
        else:
            if res == START_FILE or res == END_FILE:
                continue
            add_to_file(cfname, res)

def main():
    with open(CAP_FILE, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        extract_dns(pcap)

main()
