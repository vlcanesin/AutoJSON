import json

f = open('jsonForScript.json', 'r', encoding='utf8')
file = json.load(f)

for item in file:
    print(item)
    arq = []
    arq.append(item)
    arq_name = (str(item["ano"]) + '/' + 'artigos' + '-' + str(item["ano"]) + '-' + str(item["nome"]).replace(':', '').replace('/', '-').replace('?', '') + '.json')
    if(len(arq_name) > 64):
        arq_name = arq_name[:64] + '.json'
    with open(arq_name, 'w', encoding='utf8') as file:
        json.dump(arq, file, ensure_ascii=False)