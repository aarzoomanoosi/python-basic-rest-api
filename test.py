import requests

base = "http://127.0.0.1:5000/"

# run default endpoint
response = requests.get(base)
print(response.json())

#run helloworld endpoint
response = requests.get(base + "helloworld") 
print(response.json())

