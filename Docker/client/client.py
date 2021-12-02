import urllib.request

fp = urllib.request.urlopen("http://localhost:7777/")

encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")

print(decodedContent)

fp.close()
