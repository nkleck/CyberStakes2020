# Rotate Me

## Challenge
* Category: Cryptography
* Points: 5

Our security manager, Julius, is confident nobody can break his encryption and so left the flag for everyone to see. [ciphered_flag.txt](https://challenge.acictf.com/static/eaeae1399e23536dc5b2b2aeca8e0c52/ciphered_flag.txt)

### Hints
* Does knowing the flag format give you any information about how the flag was encrypted?
* When in [Rome](https://en.wikipedia.org/wiki/Caesar_cipher)?
* Julius is notorious for playing games with the problem names...


## Solution

Ok. so the ciphered flag reads: IKQ{KzGxBw_NcV_nWz_ItT_WHQRfViZ}

We know all flags start with ACI, So this is just a matter of rotating a few positions. Counting from A -> I is 8 positions.

Go to https://www.dcode.fr/caesar-cipher, enter the ciphered flag above, select know the shift: `8` and click Decrypt Caesar Code. The decrypted flag is on the left side of the page.

**ACI{CrYpTo_FuN_fOr_AlL_OZIJxNaR}**
