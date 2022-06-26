from bs4 import BeautifulSoup
import json

html = """
    <ul type="disc">
        <li>
            DE SOUZA, PRISCILLA ; SILVESTER, LISHIL ; DA SILVA, ANDERSON ; FERNANDES, CIBELE ; RODRIGUES, THENNER ; PAUL, SEBASTIEN ; CAMARGO, PEDRO ; WOJCIESZAK, ROBERT . Exploiting the Synergetic Behavior of PtPd Bimetallic Catalysts in the Selective Hydrogenation of Glucose and Furfural.<strong> Catalysts,</strong> v. 9, p. 132, 2019.
            <a href="http://dx.doi.org/10.3390/catal9020132"><strong>Clique aqui</strong></a>
        </li>
    </ul>

    <ul type="disc">                                v Lembrar que a separação é feita a partir do ' . '
        <li> ADÃO, R.; BAI, G.; LOH, W.; BASTOS, M. . Chemical calibration of Isothermal Titration Calorimeters: An evaluation of the dilution of propan-1-ol into water as a test reaction using different calorimeters, concentrations and temperatures. <strong>Journal of Chemical Thermodynamics</strong>, v. 52, p. 57-63, 2012. </li>
    </ul>
    <ul type="disc">
        <li> AGUIAR, A. C. C.; SANTOS, R. M.; FIGUEIREDO, F. J. B.; CORTOPASSI, W. A.; PIMENTEL, A. S.; FRANÇA, T. C. C.; MENEGHETTI, M. R.; KRETTLI, A. U. . Antimalarial activity and mechanisms of action of two novel 4-aminoquinolines against chloroquine-resistant parasites. <strong>Plos One</strong>, v. 7, p. e37259, 2012. </li>
    </ul>
"""

soup = BeautifulSoup(html, "html.parser")
text_list = soup.find_all('li')
link_list = soup.find_all('a')

json_file = []

while len(link_list) < len(text_list):
    link_list.append(BeautifulSoup('<a href="">Clique aqui</a>', "html.parser").find_all('a')[0])

for text, link in list(zip(text_list, link_list)):
    artigo = {}
    text = text.text
    link = link.get('href')
    #print("TEXTO: %s\nLINK: %s\n" % (text, link))

    pesq, info = text.split(" . ")   
    #print("pesq: %s\ninfo: %s\n" % (pesq, info)) 

    pesq_list = pesq.split(" ; ")
    cont = 0
    for i in pesq_list:
        i = i.strip()
        pesq_list[cont] = i
        pesq_list[cont] = pesq_list[cont].split(', ')
        pesq_list[cont] = (pesq_list[cont][1] + ' ' + pesq_list[cont][0]).title().strip()
        cont = cont + 1
        #print("pesq: %s\n" % (i))
    artigo["autores"] = pesq_list

    title = info.split(".")[0]
    info = info.replace(title, '')
    info = info[1:].strip()
    #print(info)
    artigo["nome"] = title

    info = info.split(".\n")[0]  #ignora "Cique aqui"
    #print(info)
    info = info.split(", ")
    artigo["publicador"] = info[0].title()
    artigo["versao"] = info[1][3:]
    artigo["paginas"] = info[2][3:]
    artigo["ano"] = int(info[3].replace('.', ''))
    artigo["link"] = link

    for key in artigo:
        print(key, "=", artigo[key])

    #inp = input("Ok?")
    #entrei = 0
    #if(inp != ''):
    #    entrei = 1
    #    break

    json_file.append(artigo)

#if not entrei:
with open('jsonForScript.json', 'w', encoding='utf8') as file:
    json.dump(json_file, file, ensure_ascii=False)