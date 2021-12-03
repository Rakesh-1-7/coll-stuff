import re 

text = "myema-ialid123@gmail.com , some more random text myemailid@gmail.com"
pattern = re.compile("[a-zA-Z0-9-]+@[a-zA-Z0-9.]+[a-zA-Z]+")
 
result = pattern.findall(text)

print(result)
