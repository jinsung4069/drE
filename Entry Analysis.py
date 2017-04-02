import urllib.request
import json

URL = input("URL을 입력하세요: ")
print(URL)
oldURL = URL[:27]
newURL = URL.replace(oldURL[:27], "https://playentry.org/api/project/")
print(newURL)

with urllib.request.urlopen(newURL) as url:
    File = json.loads(url.read())
    print(File)
    print(str(File).count('when_message_cast'))
    print(str(File).count('끝'))