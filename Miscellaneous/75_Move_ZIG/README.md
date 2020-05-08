
# Move ZIG

## Challenge
* Category: Miscellaneous
* Points: 75

CATS is back at it on challenge.acictf.com:21191. Only this time he's throwing 500 problems at you. If you didn't use a program to solve the last one, you'll probably want this...

### Hints
* We'll be impressed if you solve this without writing code. The hints on 'All Your Base Are Belong to Us' are still relevant here as well.

## Solution

### Tools
* starter_code.py
* score.py


```
$ python3 starter_code.py ichallenge.acictf.com 45713

This program is going to ask you to convert among 6 different bases a total
of 5 times.  Each question is placed inside of lines delimited by 78
'-' characters.  The first line of each question indicates the base we are
giving to you as well as the base we expect the result in and looks like:
[src_base] -> [answer base]
The next line of the question is the source text that we want you to convert
into the new base. Your answer should be followed by a newline character.

All of the encodings treat an underlying printable ASCII string as a
big-endian number.  If that doesn't make a lot of sense, don't worry about
it: most of the tools you'd look to use (Python, websites, etc.) generally
assume this anyways.  Except for 'raw' and 'b64', there will never be
leading 0s at the start of the answer.

Formatting key:
raw = the unencoded ASCII string (contains only printable characters
that are not whitespace)
b64 = standard base64 encoding (see 'base64' unix command)
hex = hex (base 16) encoding (case insensitive)
dec = decimal (base 10) encoding
oct = octal (base 8) encoding
bin = binary (base 2) encoding (should consist of ASCII '0' and '1')

------------------------------------------------------------------------------
b64 -> hex
RjNNb0UicWF7Lmd8e2RofG5aMU1JdVByZHxVQyctUSJ5fF9AOy9aRWN0VVpbXXVgbns5WG9waHNZTGtaNnUsXA==
------------------------------------------------------------------------------
answer: That is incorrect.  I was expecting:
46334d6f452271617b2e677c7b64687c6e5a314d49755072647c5543272d5122797c5f403b2f5a456374555a5b5d75606e7b39586f706873594c6b5a36752c5c

Goodbye
```
Ok. So this is just like `All Your Base Are Belong to Us`, except we will need to perform the conversion 500 times. A word of caution, my initial script included a `time.sleep(5)`, which paused the script for 5 seconds. The challenge would fail because they had a server-side time limitation setup. So I changed it to .2 and it worked just fine.


See score.py for how to conduct each conversion. The output below is truncated since it contained 500 translations.

FYI, The script score.py may not terminate properly, so ctl-c once the output is blank lines.


```
Correct!  You've solved 499/500 problems so far
------------------------------------------------------------------------------
raw -> dec
------------------------------------------------------------------------------
answer:
Correct!  You've solved 500/500 problems so far
That's all for now!  Here's your flag: ACI{for_great_justice_80c6b165}
```

**ACI{for_great_justice_80c6b165}**
