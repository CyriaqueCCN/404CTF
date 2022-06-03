We need to extract a file 2500+ times

Bash is a good tool for this, let's write a script leveraging 7z's capability to extract about anything.
We just isolate any file starting by "flag" and ending in a compressed suffix, then extract it (and delete the previous one because disk space is expensive)

At the end, we get a cool flag.txt file (and some junk @Paxheader from a misformat of tar files, but we wont be bothered with them)

`404CTF{C0mPr3Ssi0n_m4X1m4L3_m41S_p4S_3ff1C4c3}`
