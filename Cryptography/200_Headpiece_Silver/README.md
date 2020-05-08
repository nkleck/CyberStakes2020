# Headpiece Silver

## Challenge
* Category: Cryptography
* Points: 200

Can you break our unbreakable crypto? challenge.acictf.com:30315

### Hints
* How large is the N that you receieved?
* The password is alphanumeric
* telnet is known to interact poorly with the challenge instance. We recommend using 'netcat' to connect to the challenge.


## Solution

### Tools
* netcat


Lets see what we are dealing with.
```
$ nc challenge.acictf.com 30315
Welcome to Headpiece Silver.
We have employed the greatest cryptographers to develop out new cryptosystem.
Let's see if you can find a way to break it.

Choose an option:
1. Print public key
2. Get password ciphertext
3. Enter password
4. Test ciphertext
5. Exit
1

Here is our public key information
N: 122298190177919866881639090045815514691491489519639425496178483984084352945237
e: 65537

Choose an option:
1. Print public key
2. Get password ciphertext
3. Enter password
4. Test ciphertext
5. Exit
2

If you can decrypt the password you will get a reward.
36ba8ba886491c919aad9b2c15d2a464f368c112562944d19b24b22914f5a54a

```

So they gave us a number of components

components
* N - modulus
* e - encryption exponent
* public key consists of modulus N = p*q
* q = N/p
* d = password_ciphertext

We have N,e,d. We need to solve for p and q and then we can then get plaintext using a site like this: https://www.cryptool.org/en/cto-highlights/rsa-step-by-step


However, instead of that approach, optino 4 lets us give it ciphertext and it will return a decrypted string. So lets try sending it the ciphertext it gives us in response 2.

```
$ nc challenge.acictf.com 30315
Welcome to Headpiece Silver.
We have employed the greatest cryptographers to develop out new cryptosystem.
Let's see if you can find a way to break it.

Choose an option:
1. Print public key
2. Get password ciphertext
3. Enter password
4. Test ciphertext
5. Exit
1

Here is our public key information
N: 122298190177919866881639090045815514691491489519639425496178483984084352945237
e: 65537

Choose an option:
1. Print public key
2. Get password ciphertext
3. Enter password
4. Test ciphertext
5. Exit
2

If you can decrypt the password you will get a reward.
36ba8ba886491c919aad9b2c15d2a464f368c112562944d19b24b22914f5a54a

Choose an option:
1. Print public key
2. Get password ciphertext
3. Enter password
4. Test ciphertext
5. Exit
4

Please send in a ciphertext as a hex string:
36ba8ba886491c919aad9b2c15d2a464f368c112562944d19b24b22914f5a54a
Your ciphertext decrypted to:
586a333173376656757153574975526c
```

Now decode that hex on rapidtables: HEX TO ASCII

https://www.rapidtables.com/convert/number/hex-to-ascii.html

586a333173376656757153574975526c -> `Xj31s7fVuqSWIuRl`

```
Choose an option:
1. Print public key
2. Get password ciphertext
3. Enter password
4. Test ciphertext
5. Exit
3

Please enter password:
Xj31s7fVuqSWIuRl
You beat our crypto, here is your reward!
ACI{0b5393d8035c553e5c350ed451a}
```

**ACI{0b5393d8035c553e5c350ed451a}**
