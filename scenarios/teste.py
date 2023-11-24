from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['DB_WorkLink']
collection = db['usuario']

data = {
    "email": "teste@email.com",
    "senha": "1222212121",
    "telefone": "212323224002",
    "nome": "Usuario Teste Connect",
    "genero": "Feminino",
    "data_nascimento": "30/10/2001",
    "cpf": "01234567811",
    "habilidades": ["JavaScript", "Python"],
    "experiencia": "10 anos",
    "tag_desenvolvedor": ["backend", "IA"],
    "status": True}

result = collection.insert_one(data)
print(f'Inserted document id: {result.inserted_id}')