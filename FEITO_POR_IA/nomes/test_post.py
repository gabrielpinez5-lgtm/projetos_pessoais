import requests

r = requests.post('http://127.0.0.1:5000/cadastrar', json={'nome':'Teste','cpf':'123'})
print(r.status_code, r.text)