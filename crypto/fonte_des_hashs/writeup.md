Cipher flag : 18f2048f7d4de5caabd2d0a3d23f4015af8033d46736a2e2d747b777a4d4d205

hash.py poorly obfuscates a python hash algorithm

We print it to orig.py and study it.

It's really poorly designed :

The algorithm is destructive if the input has a length greater than 30
And if it's greater than 62, it also ignores some part of the input (rendering
it vulnerable to collisions as well)

Analysing the hash produced by the script, we see that, for most inputs, it shows a padding of "7c" followed by multiple "63" at the end. This is the sign of a fundamentally broken algorithm

We also remark that our cipher doesn't have such padding
Looking at the padding function, it can mean only one thing :
(len(flag) + 32) % 30 == 0

As said above, if the flag is of len 30, we should be good to go.
If it's 62 or more, we would need to bruteforce it (and good luck at those lengths)

Let's pray that the phase 1 function was never called.

We reverse the sbox and p2 functions quite easily (and add an unpad to ignore trailing
null bytes)

Then we cross fingers and launch our script (reverse.py) on the given cipher

`404CTF{yJ7dhDm35pLoJcbQkUygIJ}`

Hurray.
