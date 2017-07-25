from random import randint
# Attack Stats key:
#	[Base Power,Accuracy,Physical/Special,Secondary Effect]
#	Secondary Effect Key:
#		0 - None
#		1 - Foe Stat Change
#		2 - User Stat Change
#		3 - Critical Hit Chance
#		4 - Flinch Chance
#		5 - Restore HP
#		6 - Multiple Hits
#		7 - Priority
#		8 - Status Condition
#		9 - Other
atkStats = {
			"Absorb" : [20,100,2,5],
			"Acid" : [40,100,2,1],
			"Acid Spray" : [40,100,2,1],
			"Acrobatics" : [55,100,1,9],
			"Aerial Ace" : [60,0,1,0],
			"Aeroblast" : [100,95,2,3],
			"Air Cutter" : [60,95,2,3],
			"Air Slash" : [75,95,2,4],
			"Ancient Power" : [60,100,2,2],
			"Aqua Jet" : [40,100,1,7],
			"Aqua Tail" : [90,90,1,0],
			"Arm Thrust" : [15,100,1,6],
			"Assurance" : [60,100,1,9],
			"Astonish" : [30,100,1,4],
			"Attack Order" : [90,100,1,3],
			"Aura Sphere" : [80,0,2,0],
			"Aurora Beam" : [65,100,2,1],
			"Avalanche" : [60,100,1,9]
			}
			
def accRoll(atk)
	if atk in atkStats:
		acc = atkStats[atk.title()][1]
	elif atk in staStats:
		acc = staStats[atk.title()][1]
	else:
		acc = 1000
	if acc == 0:
		return "Hits"
	elif acc == 1000:
		return "Error"
	else:
		roll = randint(1,100)
		if roll <= acc:
			return "Hits"
		else:
			return "Misses"
			
def atkDamage(atk,poke):
	dexNum = Pokedex.pokedex[poke.title()]
	base = atkStats[atk.title()][0]
	cat = atkStats[atk.title()][2]
	attack = PokeStats.pokeStats[dexNum][1]
	spAttack = PokeStats.pokeStats[dexNum][3]
	if cat == 1:
		power = base * attack
	elif cat == 2:
		power = base * spAttack
	else:
		power = damage * 2
	return power
			
def secEffects(atk):
	effect = atkStats[atk.title()][3]
	if effect == 1:
	elif effect == 2:
	elif effect == 3:
	elif effect == 4:
	elif effect == 5:
	elif effect == 6:
	elif effect == 7:
	elif effect == 8:
	elif effect == 9:
	else: