import json

f = open('jsonForScript.json', 'r', encoding='utf8')
file = json.load(f)

for item in file:
    print(item)
    if (2020 - item["ano"]) == 10:
        prec = 'A'
    elif (2020 - item["ano"]) == 11:
        prec = 'B'
    else:
        prec = (2020 - item["ano"])
    arq_name = (str(item["ano"]) + '/' + str(prec) + '-' + 'artigos' + '-' + str(item["ano"]) + '-' + str(item["nome"]).replace(':', '').replace('/', '-').replace('?', '') + '.json')
    if(len(arq_name) > 64):
        arq_name = arq_name[:64] + '.json'
    with open(arq_name, 'w', encoding='utf8') as file:
        json.dump(item, file, ensure_ascii=False)