import json

###---------------------------###
###-------- SEPARADOR --------###
###---------------------------###

### Como utilizar:
### 1. Gerar lista de artigos usando script.py
### 2. Verificar se os artigos gerados estão no arquivo jsonForScript.json
### 3. Rodar programa
### 4. Copiar artigos gerados para a pasta de artigos do site

f = open('jsonForScript.json', 'r', encoding='utf8')
file = json.load(f)

for item in file:
    print(item)
    arq_name = (str(item["ano"]) + '/' + 'artigo' + '-' + str(item["ano"]) + '-' + str(item["nome"]).replace(':', '').replace('/', '-').replace('?', '') + '.json')
    if(len(arq_name) > 64):
        arq_name = arq_name[:64] + '.json'
    with open(arq_name, 'w', encoding='utf8') as file:
        json.dump(item, file, ensure_ascii=False)