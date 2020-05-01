import urllib.request
import urllib.parse

"""
HTTP: HyperText Transport Protocol
port 80
foloseste in spate TCP
http://google.com:8000
data nu pui :port e default :80
/routa
parametri /link?p=v&x=y
protocol stateless

Request:
HTTP v Metode(get put post delete) R
HEADERS:
Content-Type: application/json
allow control...
User-Agent: pe un browser o sa araate diferit (de ex poate detecta daca intri pe mobil)
O linie goala
Eventual Body


URLLIB
.request - Request, urlopen
.parse - urlparse, urlencode
.errors

"""
h = {
    'User-Agent': 'google',
    'X-Custom': 'xyz'
}

# prin conventie headerele custom se pun cu X in fata

# 'http://httpbin.org/get?x=y&x=z'
r = urllib.request.Request('http://httpbin.org/get', headers=h)

# daca vrem sa facem POST punem si param data= care o sa primeasca bytes - si schimbat si in /post altfel primim 405 -METHOD NOT ALLOWED


response = urllib.request.urlopen(r)

print(response.read().decode())
print(response.getcode())


"""
'de recomandat sa folosim requests, nu urllib
"""

"""
 URL Encoding - cheie valoare si concatenate cu &, nu vrem sa-l facem de mana asa ca vom folosi:
"""

"""
urllib.parse.urlenmode({
'x':'y',
.... })
"""

"""
p = urlparse(link)
p.netloc()
metode sa ne scoata domeniul, protocolul, resursele etc
!!!!!!!
"""

