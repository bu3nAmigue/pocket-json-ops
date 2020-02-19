from bs4 import BeautifulSoup
import json

with open('libro.html') as fp:
    soup = BeautifulSoup(fp)

#titulos = soup.find_all('span', class_='cls_007')
#texto_titulos = []
#for each in titulos:
#    texto_titulos.append(each.text)

#primer_div = titulos[0].find_parent().find_next_sibling()

def get_ritmos():
    ritmos = soup.find_all('span', class_='cls_007')
    return ritmos

ritmos = get_ritmos()

dict_ritmos = {}
for each in ritmos:
    dict_ritmos[each.text] = {}
    actual = each.find_parent()
    while 'cls_007' not in actual.find_next_sibling()['class']:
        if 'cls_008' in actual.find_next_sibling()['class']:
            if actual.find_next_sibling().find('span').text != '^' and actual.find_next_sibling().find('span').text != 'AC':
                instrumento = actual.find_next_sibling().find('span').text
                dict_ritmos[each.text][instrumento] = []
                actual = actual.find_next_sibling()
                print(instrumento)
                print(actual)
            else:
                actual = actual.find_next_sibling()
        elif 'cls_009' in actual.find_next_sibling()['class']:
            print(dict_ritmos[each.text])
            dict_ritmos[each.text][instrumento].append(int(actual.find_next_sibling().find('span').text))
            actual = actual.find_next_sibling()
        else:
            break





# instrumentos = []
# actual = ritmos[1].find_parent()
# while 'cls_007' not in actual.find_next_sibling()['class']:
#     if 'cls_008' in actual.find_next_sibling()['class']:
#         instrumentos.append(actual.find_next_sibling().find('span').text)
#         actual = actual.find_next_sibling()
#         print(instrumentos)
#         print(actual)
#     elif 'cls_009' in actual.find_next_sibling()['class']:
#         actual = actual.find_next_sibling()
#     else:
#         break

print(dict_ritmos)

with open('data.json','w') as json_file:
    json.dump(dict_ritmos, json_file, sort_keys=True,indent=4)

#     actual = ritmo.find_parent().find_next_sibling()
#     while actual.class != 'cls_007':
#         if actual.class == 'cls_008':
#             instrumentos.append()
    



