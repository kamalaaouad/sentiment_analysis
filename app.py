import requests

url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

payload = "text=great%20value%20in%20its%20price%20range!"
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Host": "twinword-sentiment-analysis.p.rapidapi.com",
    "X-RapidAPI-Key": "e232384e17msh42c0678ce852e02p154a46jsn8ffd8f66029c"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.json())
