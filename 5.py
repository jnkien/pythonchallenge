import requests
proxies = {"http": "http://localhost:3128"}
url = "http://www.pythonchallenge.com/pc/def/banner.p"
r = requests.get(url, proxies = proxies)

import pickle
data = pickle.loads(str.encode(r.text))

s = '\n'.join(''.join([x[0]*x[1] for x in l]) for l in data)
print(s)
