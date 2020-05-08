
# All Your Base Are Belong to Us

## Challenge
* Category: Miscellaneous
* Points: 50

In honor of 30 years of terrible translations, we figured we'd give you a try at a series of (easier) translation problems. All you have to do is to translate bases by connecting to challenge.acictf.com:21195. In case you're new to network programs, we even have some Python starter code you can use.

### Hints
* You could do this by hand, but is it really worth that much effort?
* While we only want the final encoding, it's probably easier to break that into separate decode and encode steps for each question.
* Don't overthink 'raw' encoding...
* Your code for encoding/decoding will probably be very similar for 4 out of 6 encodings.

## Solution

### Tools
* starter_code.py
* score.py


Lets start by running `starter_code.py` and connecting to the server to see what we are dealing with. See the output below:


```
$ python3 starter_code.py ichallenge.acictf.com 32264

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

Ok. So the output informs us we will need to convert from a starting format to a desired format six times. There are a lot of possible combinations that the conversion can be. We do not need to figure out each combination. We can simply pick 1 standard converstion to for every starting format, and then convert to the desired answer format from there.

For Example:
```
b64 to raw
hex to raw
dec to raw
oct to raw
bin to raw

```
then we can convert from raw to the desired answer format
```
raw to b64
raw to hex
raw to dec
raw to oct
raw to bin
```

At this point, I ran the `starter_code.py` script just to get enough of a sample set for each encoding type to play with.

See score.py for how to conduct each conversion.

FYI, The script score.py may not terminate properly, so ctl-c once the output is blank lines.

```
$ python3 score.py

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
oct -> raw
['oct', 'raw']
Translate SRC oct 111234724573303513217246441342605151467006023463063366431231405052226275522156245003527606434044172256355153705051512422562166624431725457025440540124671072762047030433145 to raw
Answer: INu/l:Z=M!qaM3p0Nf3{FS0QRY{R7)@u|4pHzW;M|QM*%r;e#=YxVA`*nG_!8b6e
------------------------------------------------------------------------------
answer:
Correct!  You've solved 1/5 problems so far
------------------------------------------------------------------------------
dec -> hex
['dec', 'hex']
Translate SRC dec 2948191231588092552725713798951919222495892301119679103652651103708307292009691356435219886509063090559645502383261125059954338981241143648461113636774997 to hex
Answer: 384a75642e445d5e755f46545841506e55555d3a5c3d7458313739783e2f2d68476d444f3e4956633e6b7543664f41352269612f3772364c4d6e5a2853756455
------------------------------------------------------------------------------
answer:
Correct!  You've solved 2/5 problems so far
------------------------------------------------------------------------------
oct -> hex
['oct', 'hex']
Translate SRC oct 46354311612343314420270447250274453263315016027103120405053365256014240546366721123147555223224055370424763465317114627525106571603524012434450103150410572567611117075170 to hex
Answer: 267632714e3664417127542f256b3668382e432841456f55703141667b744a667b6a4d282d7c453e735679332f55235e7075405472504334422f577c493c7a78
------------------------------------------------------------------------------
answer:
Correct!  You've solved 3/5 problems so far
------------------------------------------------------------------------------
oct -> hex
['oct', 'hex']
Translate SRC oct 136264205612046404327221557256555333624511524440162152335452044644126072153154441112224416034266520256261002063046137030505364661413546645416065535232624431367351620074466 to hex
Answer: 5e5a21714268235d236f575b5b794a4d524072353765424d2158746b364849494870716d50572c404331317c31457a6c61766d2c386b5d4d65232f774e407936
------------------------------------------------------------------------------
answer:
Correct!  You've solved 4/5 problems so far
------------------------------------------------------------------------------
raw -> oct
['raw', 'oct']
Translate SRC raw 17b-98'u"O88Y@iqxp]1s.G'D@dmswj&q(oGXS%V=%'qZEOR2oP:RK!)<fm65.!P to oct
Answer: 61156610551623404735221117160341312006456136070135142714562162350420062155346735521147045033643530246225261722244734255105236510623365007224445441122361463323306513420520
------------------------------------------------------------------------------
answer:
Correct!  You've solved 5/5 problems so far
That's all for now!  Here's your flag: ACI{Somebody_set_up_us_the_bomb_d9b3d0de}

```

**ACI{Somebody_set_up_us_the_bomb_d9b3d0de}**
