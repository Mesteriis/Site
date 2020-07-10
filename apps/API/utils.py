import requests
from time import sleep

from ipware import get_client_ip
 # client_ip, is_routable = get_client_ip(request)
 # if client_ip is None:
 #    Unable to get the client's IP address
 # else:
 #     We got the client's IP address
     # if is_routable:
     #     The client's IP address is publicly routable on the Internet
     # else:
     #     The client's IP address is private



 # Order of precedence is (Public, Private, Loopback, None)
def getWialonToken(login, password):
    url1 = 'http://online.wialon.center/login.html'
    url2 = 'http://online.wialon.center/oauth.html'
    jn1 = {
        'login': login,
        'password': password,
        'Content-Language': 'ru',
        'response_type': 'token',
    }
    html = requests.get(url1, json=jn1).text
    sign = html[html.find('sign') + 13:html.find('sign') + 13 + 44]
    sleep(3)
    jn2 = {
        'content-type': 'application/x-www-form-urlencoded',
        'response_type': 'token',
        'client_id': 'wialon.center ГЛОНАСС мониторинг транспорта',
        'redirect_uri': 'http://online.wialon.center/login.html',
        'access_type': '0x100',
        'activation_time': '0',
        'duration': '0',
        'flags': '6',
        'sign': sign,
        'login': login,
        'passw': password,
        'Content-Language': 'ru'
    }
    res = requests.post(url2, data=jn2)

    tokenWialon: str
    code_error: int

    tokenWialon = res.url[res.url.find('access_token=') + 13:res.url.find('&svc_error')]
    code_error = int(res.url[res.url.find('error=') + 6:len(res.url)])

    if code_error != 0:
        return code_error
    else:
        return tokenWialon


def getOmniCommToken(login, password):
    tokenOmnicomm = requests.post('https://online.omnicomm.ru/auth/login?jwt=1',
                                  json={
                                      'login': login,
                                      'password': password
                                  }).json()['jwt']
    return tokenOmnicomm
