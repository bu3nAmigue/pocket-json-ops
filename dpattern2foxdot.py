
lista_instrumentos = {
    'BD': 'x',
    'SN': 'u',
    'LT': 'm',
    'RS': 'i',
    'MT': 'c',
    'CB': 'r',
    'HT': 'p',
    'CY': '#',
    'CL': '*',
    'OH': '=',
    'SH': 's',
    'CH': '-',
    'AC': 'o'
}

import json
with open('ritmos.json','r') as f:
	patterns = json.load(f)
	
# Opcion online
#import requests
#r = requests.get('https://raw.githubusercontent.com/bu3nAmigue/pocket-json-ops/master/ritmos.json')
#patterns = r.json()

# drumPattern2FoxdotSyntax([5,9,11,13,15,16],"X") -> '     X   X X X XX'
def drumPattern2FoxdotSyntax(pattern,value):
	total_length = 16
	result = " "*total_length
	for index in pattern:
		result = result[:index-1] + value + result[index:]
	return result


import numbers
def pattern(id=None):
	if isinstance(id,str):
		name = id
		spec = patterns[id]
	elif isinstance(id, numbers.Number):
		name, spec = list(patterns.items())[id]
	else:
		id = random.randint(0, len(patterns))
		name, spec = list(patterns.items())[id]
	print("Playing "+name)
	print(spec)
	players = [d1,d2,d3,d4,d5,d6,d7,d8]
	player_index = 0
	for instrument, pattern in spec.items():
		foxdotPattern = drumPattern2FoxdotSyntax(pattern,lista_instrumentos[instrument])
		print(foxdotPattern)
		players[player_index].reset() >> play(foxdotPattern)
		player_index += 1
	# Pauso los players que no se usen
	for player in players[player_index:]:
	    player.stop()

# Intercalar patterns
def var_pattern(patterns,dur):
    pattern(patterns[0])
    if len(patterns) > 1:
        Clock.future(dur,lambda: var_pattern(patterns[1:],dur))
    else:
        pass

# Reproduciendo el segundo patron de la lista
pattern(2)

# Reproduciendo el patron que se llama "AMEN BREAK - A"
pattern("AMEN BREAK - A")

# Reproduciendo un patron al azar
pattern()

# Reproducir patterns que varian cada 16 beats
var_pattern([5,6,7,5],16)
