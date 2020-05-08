
# More Out of Site

## Challenge
* Category: Web Security
* Points: 10

Well that was embarrassing... Who knew there was more to a web site then what the browser showed? Not to worry, we're back with a new and improved Javascript version! http://challenge.acictf.com:19888

### Hints
* The Javascript code in an onInput gets called anytime you interact with a text field.
* Is there anyway to view the Javascript definition of this function? It should just be text and your browser has it somewhere (it is running it after all).


## Solution

Ok. This time we Right-Click > Inspect the page. We see the form input has `oninput="check_flag()"` which is a reference to the script at the bottom of the html. So right-click on the script at the bottom and select "open in a new tab"

In the new tab we see the following:

```
function check_flag() { var flag = document.forms["flagChecker"]["flag"].value; var submit_button = document.forms["flagChecker"]["submit"]; var status_field = document.getElementById("status"); if (flag == "ACI{client_side_fail_845ce5f8}") { submit_button.disabled=false; status_field.innerHTML = ""; } else { submit_button.disabled=true; status_field.innerHTML = "error: does not match flag"; } }
```

Our flag is: **ACI{client_side_fail_845ce5f8}**
