# ergasia 10
import urllib.request
import re
a=input("Δωστε ενα link: ")
page=urllib.request.urlopen(a)
con=page.read()
con=str(con,'utf-8')
links=len(re.findall("<a",con))+len(re.findall("<link",con))
changeline=len(re.findall("<br>",con))+len(re.findall("</p>",con))
print("Οι συνδεσμοι μεσα στον κωδικα ειναι ",links," και οι αλλαγες γραμμης ειναι ",changeline)
