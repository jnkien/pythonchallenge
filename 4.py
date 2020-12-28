import requests
proxies = {"http": "http://localhost:3128"}

def run(nothing_value):
    k = 1
    print(f"Iteration {k} nothing={nothing_value}")
    
    url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing_value}"
    r = requests.get(url, proxies = proxies)
    
    while "and the next nothing is" in r.text:
        k += 1
        nothing_value = re.search("the next nothing is ([0-9]+)", r.text).group(1)
        print(f"Iteration {k} nothing={nothing_value}")
        
        url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing_value}"
        r = requests.get(url, proxies = proxies)

run('12345')
#run('8022')
