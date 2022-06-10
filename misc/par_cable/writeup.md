We replace the -1 by zeroes and eliminate spaces with
`cat Cable.txt | sed -e "s/-1/0/g" | tr -d ' ' > stripped.txt`

The result has 329 bits. Not a multiple of anything interesting.

Since it's a signal, we try to XOR every value with the next one (I don't know if it's common in signal processing but it is in filtering)

Welp, got a flag\*. Still don't have any clue about signals whatsoever.

`404CTF{N0n3_R3tUrn_Z3r0_InV3rtEd_f0r3v3r}`


\* This writeup doesn't say anything about the hour I spent roughing up that data : multiplication, addition, xors, averages, inversions, grouping by 7, by 8, adding LSBs or MSBs... We won't talk about that.
