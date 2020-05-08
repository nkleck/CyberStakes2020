# Binary Exploitation 101

## Challenge
* Category: Binary Exploitation
* Points: 50

Exploiting bugs in programs can definitely be difficult. Not only do you need a certain amount of reverse engineering required to identify vulnerabilities, but you also need to weaponize that vulnerability somehow. To get new hackers started, we included our annotated source code along with the compiled program.
If you don't know where to start, download the source code and open it in a program with syntax highlighting such as notepad++ or gedit. If you don't have the ability to use either of those, you can always use vim.

You can connect to the problem at telnet challenge.acictf.com 12095 or nc challenge.acictf.com 12095

### Hints
* Signed integers on modern computers generally use something called "Two's Complement" for representing them. If this is your first time dealing with integers at this level, it is probably worth taking some time to get a basic understanding of them. In particular, you will need to understand what the largest positive number looks like, what -1 looks like, and how overflow is generally "handled".
* We've also included debug symbols in the binary and disabled compiler optimizations. Once you understand how the C code works from the source code, it is probably worth opening the compiled binary in something like Ghidra to see both what the assembly looks like and how the recovered C code compares to the source code. Most of the other binary exploitation problems do not give you access to the raw source code.
* While many binary exploitation situations involve "non-standard" inputs (such as feeding shellcode as input to the name of something), this challenge does not. Once you understand the vulnerability, you can trigger it through normal interaction with the challenge. If you are having trouble on the math side, treating the binary representation of your 'target' number as an unsigned integer may be helpful.
* If you are new to binary exploitation (or C code), we really recommend reading the source file in its entirety as the comments try to explain many of the key concepts for this category of problems. For this specific problem, anyone not familiar C should definitely read the source file because the behavior of s.numbers[-1] is very different between C and some other popular languages (e.g. Python).


## Solution

Ok. Lets see what we are working with
```
$ nc challenge.acictf.com 12095
Give me a number:
2147483647
Give me another number:
1
2147483647 * 1 = 2147483647 which ends in a 'seven'
```

Start by reading the notes in BinExe101.c. It explains each section of code. Pay particular interest to the portion labeled `Vulnerable Code`. So we need to multiple two numbers that will result in a negative number becasuse it wraps past 2147483647. Here are some resources on integer overflow:
* https://en.wikipedia.org/wiki/Two%27s_complement
* https://en.wikipedia.org/wiki/Integer_overflow
* https://www.cs.utah.edu/~germain/PPS/Topics/unsigned_integer.html


We are going to flip a the leading bit on twos component to cause an interger overflow and get -1

Start by getting the binary representation of our number
* https://www.rapidtables.com/convert/number/decimal-to-binary.html
* Enter: `2147483647`
* which gives us:
  * binary signed 2's component: `01111111111111111111111111111111`

Lets flip the leading bit and convert back to decimal
* https://www.rapidtables.com/convert/number/binary-to-decimal.html
* Enter: `11111111111111111111111111111111`
  * Which gives us: `4294967295`

Now lets get the factors for `4294967295`
* https://www.calculatorsoup.com/calculators/math/factors.php
* factor 4294967295
  * pick something smaller like:
    * 51 × 84215045

```
$ nc challenge.acictf.com 12095
Give me a number:
84215045
Give me another number:
51
84215045 * 51 = -1 which ends in a 'ACI{25d99e015cd93139ecc52aba33e}'
```

**ACI{25d99e015cd93139ecc52aba33e}**
