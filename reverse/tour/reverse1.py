00000000: 6465 6620 746f 7572 3128 7061 7373 776f  def tour1(passwo
00000010: 7264 293a 0a20 2020 2073 7472 696e 6720  rd):.    string 
00000020: 3d20 7374 7228 2222 2e6a 6f69 6e28 2022  = str("".join( "
00000030: 222e 6a6f 696e 2870 6173 7377 6f72 645b  ".join(password[
00000040: 3a3a 2d31 5d29 5b3a 3a2d 315d 295b 3a3a  ::-1])[::-1])[::
00000050: 2d31 5d29 0a20 2020 2072 6574 7572 6e20  -1]).    return 
00000060: 5b6f 7264 2863 2920 666f 7220 6320 696e  [ord(c) for c in
00000070: 2073 7472 696e 675d 0a0a 0a64 6566 2074   string]...def t
00000080: 6f75 7232 2870 6173 7377 6f72 6429 3a0a  our2(password):.
00000090: 2020 2020 6e65 7720 3d20 5b5d 0a20 2020      new = [].   
000000a0: 2069 203d 2030 0a20 2020 2077 6869 6c65   i = 0.    while
000000b0: 2070 6173 7377 6f72 6420 213d 205b 5d3a   password != []:
000000c0: 0a20 2020 2020 2020 206e 6577 2e61 7070  .        new.app
000000d0: 656e 6428 7061 7373 776f 7264 5b70 6173  end(password[pas
000000e0: 7377 6f72 642e 696e 6465 7828 7061 7373  sword.index(pass
000000f0: 776f 7264 5b69 5d29 5d29 0a20 2020 2020  word[i])]).     
00000100: 2020 206e 6577 2e61 7070 656e 6428 7061     new.append(pa
00000110: 7373 776f 7264 5b70 6173 7377 6f72 642e  ssword[password.
00000120: 696e 6465 7828 7061 7373 776f 7264 5b69  index(password[i
00000130: 5d29 5d20 2b20 7061 7373 776f 7264 5b70  ])] + password[p
00000140: 6173 7377 6f72 642e 696e 6465 7828 7061  assword.index(pa
00000150: 7373 776f 7264 5b20 6920 2b20 3120 256c  ssword[ i + 1 %l
00000160: 656e 2870 6173 7377 6f72 6429 5d29 5d29  en(password)])])
00000170: 0a20 2020 2020 2020 2070 6173 7377 6f72  .        passwor
00000180: 642e 706f 7028 7061 7373 776f 7264 2e69  d.pop(password.i
00000190: 6e64 6578 2870 6173 7377 6f72 645b 695d  ndex(password[i]
000001a0: 2929 0a20 2020 2020 2020 2069 202b 3d20  )).        i += 
000001b0: 696e 7428 2771 6b64 6a27 2c20 6261 7365  int('qkdj', base
000001c0: 3d32 3729 202d 2069 6e74 2827 514b 444a  =27) - int('QKDJ
000001d0: 272c 2062 6173 653d 3331 2920 2b20 3236  ', base=31) + 26
000001e0: 3735 3030 0a20 2020 2072 6574 7572 6e20  7500.    return 
000001f0: 6e65 770a 0a64 6566 2074 6f75 7233 2870  new..def tour3(p
00000200: 6173 7377 6f72 6429 3a0a 2020 2020 6d64  assword):.    md
00000210: 7020 3d5b 276c 272c 2027 7827 2c20 2769  p =['l', 'x', 'i
00000220: 272c 2027 6227 2c20 2769 272c 2027 6927  ', 'b', 'i', 'i'
00000230: 2c20 2771 272c 2027 7527 2c20 2764 272c  , 'q', 'u', 'd',
00000240: 2027 7627 2c20 2761 272c 2027 7627 2c20   'v', 'a', 'v', 
00000250: 2762 272c 2027 6e27 2c20 276c 272c 2027  'b', 'n', 'l', '
00000260: 7627 2c20 2776 272c 2027 6c27 2c20 2767  v', 'v', 'l', 'g
00000270: 272c 2027 7a27 2c20 2771 272c 2027 6727  ', 'z', 'q', 'g'
00000280: 2c20 2769 272c 2027 7527 2c20 2764 272c  , 'i', 'u', 'd',
00000290: 2027 7527 2c20 2764 272c 2027 6a27 2c20   'u', 'd', 'j', 
000002a0: 276f 272c 2027 7227 2c20 2779 272c 2027  'o', 'r', 'y', '
000002b0: 7227 2c20 2775 272c 2027 6127 5d0a 2020  r', 'u', 'a'].  
000002c0: 2020 666f 7220 6920 696e 2072 616e 6765    for i in range
000002d0: 286c 656e 2870 6173 7377 6f72 6429 293a  (len(password)):
000002e0: 0a20 2020 2020 2020 206d 6470 5b69 5d2c  .        mdp[i],
000002f0: 206d 6470 5b6c 656e 2870 6173 7377 6f72   mdp[len(passwor
00000300: 6429 202d 2069 202d 3120 5d20 3d20 6368  d) - i -1 ] = ch
00000310: 7228 7061 7373 776f 7264 5b6c 656e 2870  r(password[len(p
00000320: 6173 7377 6f72 6429 202d 2069 202d 3120  assword) - i -1 
00000330: 5d20 2b20 6920 2520 3429 2c20 2063 6872  ] + i % 4),  chr
00000340: 2870 6173 7377 6f72 645b 695d 202b 2069  (password[i] + i
00000350: 2025 2034 290a 2020 2020 7265 7475 726e   % 4).    return
00000360: 2022 222e 6a6f 696e 286d 6470 290a 0a0a   "".join(mdp)...
00000370: 0a0a 6d64 7020 3d20 696e 7075 7428 224d  ..mdp = input("M
00000380: 6f74 2064 6520 7061 7373 6520 3a20 2229  ot de passe : ")
00000390: 0a0a 6966 2074 6f75 7233 2874 6f75 7232  ..if tour3(tour2
000003a0: 2874 6f75 7231 286d 6470 2929 2920 3d3d  (tour1(mdp))) ==
000003b0: 2022 c2a1 50c2 8736 c2a8 73c3 8955 c285   "..P..6..s..U..
000003c0: 31c2 8654 c283 30c2 9564 c2b8 56c3 8a76  1..T..0..d..V..v
000003d0: c3a7 75c2 a936 c284 52c3 8878 c2a8 3478  ..u..6..R..x..4x
000003e0: 4677 3522 3a0a 2020 2020 7072 696e 7428  Fw5":.    print(
000003f0: 2242 7261 766f 2021 204c 6520 666c 6167  "Bravo ! Le flag
00000400: 2065 7374 2034 3034 4354 467b 2220 2b20   est 404CTF{" + 
00000410: 6d64 7020 2b20 227d 2229 0a65 6c73 6520  mdp + "}").else 
00000420: 3a0a 2020 2020 7072 696e 7428 2244 c3a9  :.    print("D..
00000430: 736f 6cc3 a92c 206c 6520 6d6f 742d 6465  sol.., le mot-de
00000440: 2d70 6173 7365 206e 2765 7374 2070 6173  -passe n'est pas
00000450: 2063 6f72 7265 6374 2229 0a0a 0a0a 0a     correct").....
