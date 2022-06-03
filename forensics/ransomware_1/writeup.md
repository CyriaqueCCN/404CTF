An interesting pcap file.

There are only 2 types of packets present : classic ARP requests between 2 IPs and the broadcast, and TCP between those 2 IPs

`172.17.0.1 20`
 =>
`172.17.0.2 1337`


None of these 40k+ packets have any data, but around 3500 TCP sessions are opened.

1 from 1337 to 20 then 3596 from 20 to 1337

20 is an FTP port (and 1337 the C2, obv)

The data exfiltration should be somewhere in the TCP header.

The flags part changes, apparently randomly. Other than that, the rest seems OK

Let's write a little python script to extract all the flags bytes and write them to extracted

It's a pdf file with the flag in it. And a cool wordplay at that.

`404CTF{L3s_fL4gS_TCP_Pr1S_3n_fL4G}`
