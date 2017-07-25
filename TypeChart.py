typeChart = [
			 [1,1,1,1,1,1,1,1,1,1,1,1,.5,0,1,1,.5,1],
			 [1,.5,.5,1,2,2,1,1,1,1,1,2,.5,1,.5,1,2,1],
			 [1,2,.5,1,.5,1,1,1,2,1,1,1,2,1,.5,1,1,1],
			 [1,1,2,.5,.5,1,1,1,0,2,1,1,1,1,.5,1,1,1],
			 [1,.5,2,1,.5,1,1,.5,2,.5,1,.5,2,1,.5,1,.5,1],
			 [1,.5,.5,1,2,.5,1,1,2,2,1,1,1,1,2,1,.5,1],
			 [2,1,1,1,1,2,1,.5,1,.5,.5,.5,2,0,1,2,2,.5],
			 [1,1,1,1,2,1,1,.5,.5,1,1,1,.5,.5,1,1,0,2],
			 [1,2,1,2,.5,1,1,2,1,0,1,.5,2,1,1,1,2,1],
			 [1,1,1,.5,2,1,2,1,1,1,1,2,.5,1,1,1,.5,1],
			 [1,1,1,1,1,1,2,2,1,1,.5,1,1,1,1,0,.5,1],
			 [1,.5,1,1,2,1,.5,.5,1,.5,2,1,1,.5,1,2,.5,.5],
			 [1,2,1,1,1,2,.5,1,.5,2,1,2,1,1,1,1,.5,1],
			 [0,1,1,1,1,1,1,1,1,1,2,1,1,2,1,.5,1,1],
			 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,.5,0],
			 [1,1,1,1,1,1,.5,1,1,1,2,1,1,2,1,.5,1,.5],
			 [1,.5,.5,.5,1,2,1,1,1,1,1,1,2,1,1,1,.5,2],
			 [1,.5,1,1,1,1,2,.5,1,1,1,1,1,1,2,2,.5,1]
			 ]

def atkType(type):
	if type.lower() == "normal":
		return 0
	elif type.lower() == "fire":
		return 1
	elif type.lower() == "water":
		return 2
	elif type.lower() == "electric":
		return 3
	elif type.lower() == "grass":
		return 4
	elif type.lower() == "ice":
		return 5
	elif type.lower() == "fighting":
		return 6
	elif type.lower() == "poison":
		return 7
	elif type.lower() == "ground":
		return 8
	elif type.lower() == "flying":
		return 9
	elif type.lower() == "psychic":
		return 10
	elif type.lower() == "bug":
		return 11
	elif type.lower() == "rock":
		return 12
	elif type.lower() == "ghost":
		return 13
	elif type.lower() == "dragon":
		return 14
	elif type.lower() == "dark":
		return 15
	elif type.lower() == "steel":
		return 16
	elif type.lower() == "fairy":
		return 17
	elif type.lower() == "none":
		return 18
	else:
		return 19
		
def defType(type):
	if type.lower() == "normal":
		return 0
	elif type.lower() == "fire":
		return 1
	elif type.lower() == "water":
		return 2
	elif type.lower() == "electric":
		return 3
	elif type.lower() == "grass":
		return 4
	elif type.lower() == "ice":
		return 5
	elif type.lower() == "fighting":
		return 6
	elif type.lower() == "poison":
		return 7
	elif type.lower() == "ground":
		return 8
	elif type.lower() == "flying":
		return 9
	elif type.lower() == "psychic":
		return 10
	elif type.lower() == "bug":
		return 11
	elif type.lower() == "rock":
		return 12
	elif type.lower() == "ghost":
		return 13
	elif type.lower() == "dragon":
		return 14
	elif type.lower() == "dark":
		return 15
	elif type.lower() == "steel":
		return 16
	elif type.lower() == "fairy":
		return 17
	elif type.lower() == "none":
		return 18
	else:
		return 19
		
def effect(atk,dfd):
	if atk == 19 or dfd == 19:
		return "You did not enter a valid type."
	elif typeChart[atk][dfd] == 1:
		return "Normal effectiveness."
	elif typeChart[atk][dfd] == 2:
		return "Super effective!"
	elif typeChart[atk][dfd] == .5:
		return "Not very effective..."
	elif typeChart[atk][dfd] == 0:
		return "No effect..."
	else:
		return "I don't know how effective that is..."