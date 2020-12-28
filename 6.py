# http://www.pythonchallenge.com/pc/def/channel.zip
# open readme.txt

import re
from zipfile import ZipFile

def run(nothing_value):
    with ZipFile('channel.zip') as z:
        k = 0
        content = ""
        comment = ""
        
        print(f"Iteration {k} nothing={nothing_value}")
        
        content = z.read(f"{nothing_value}.txt").decode('utf-8')
        
        while "Next nothing is" in content:
            comment += z.getinfo(f"{nothing_value}.txt").comment.decode('utf-8')
            
            k += 1
            nothing_value = re.search("Next nothing is ([0-9]+)", content).group(1)
            print(f"Iteration {k} nothing={nothing_value}")
            
            content = z.read(f"{nothing_value}.txt").decode('utf-8')
    return comment

result = run('90052')
print(result)
