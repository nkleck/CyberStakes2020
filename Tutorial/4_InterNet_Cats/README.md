
# InterNet Cats

## Challenge
* Category: Tutorial
* Points: 4

It looks like some crazy cat-lady stole our last tutorial flag and is handing it out to anything that 'sounds' like a cat. Her server is challenge.acictf.com, and she is listening on port 35523.

### Hints
* There is a useful program called netcat that sends the input it receives locally to a remote host and port and puts the data it receives from there onto the command line.
* The cat-lady does not care about capitalization.
* There are numerous ways to connect to the server to solve this problems, here are two we know of (replace the parts with braces, to include the braces, with the information from the problem description):
  * With netcat: nc {{server}} {{port}}
  * With telnet: telnet {{server}} {{port}}

## Solution
```
$ nc challenge.acictf.com 35523
```

Flag: **ACI{ab9ca2fa70a4718184269f94572}**
