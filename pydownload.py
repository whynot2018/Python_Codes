#
#   PyThon Lerning  @Faymaz
#       @programirez
#
import requests

r = requests.get("http://some/url.zip")
with open("my_data.zip", "wb") as code:
    code.write(r.content)
