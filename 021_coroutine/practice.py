import urllib.request

req = urllib.request.urlopen('https://www.google.com')
res = req.read()
print(res.decode('utf-8'))
