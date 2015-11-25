# CHARICALC: A Python script to make basic URPG calculations easier.
#
# Current features:
# Type Calculator: Find out a move's effectiveness.
# Dice Roller: Roll a random number.
# Dex Search (Incomplete): Ender a Pokemon's name to find the dex number.

# First, import the required files. TypeChart contains
#   the official X/Y type chart, as well as functions
#   for finding the effectiveness of a move. Random
#   contains the function to generate a random number.
#   Pokedex contains the dex list and search function.
import TypeChart
import Pokedex
from random import randint

# Define the variable that will be used to log the
#   user's command.
user = ""

# Now, show the user the fancy logo.
print(" _____ _                _ _____       _ ")
print("/  __ \ |              (_)  __ \     | |")
print("| /  \/ |__   __ _ _ __ _| /  \/ __ _| | ___")
print("| |   | '_ \ / _` | '__| | |    / _` | |/ __|")
print("| \__/\ | | | (_| | |  | | \__/\ (_| | | (__")
print("\_____/_| |_|\__,_|_|  |_|\____/\__,_|_|\___|")
print("")
print("For support, contact jacenboy1@gmail.com")
print("")
print("")

# Begin the main loop of the program. As long as the
#   user does not choose to quit, keep asking for
#   input. If the user chooses to quit, the loop ends.
while user.lower() != "e":
	print("Choose an option and press Enter or Return:")
	print("'T'ype calculator")
	print("'R'oll Dice")
	print("Poke'd'ex Search")
	print("'E'xit")
	print("")
	user = input(">>> ")

	# If the user chooses to check a type advantage, ask for the types being
	#   compared and return the effectiveness.
	if user.lower() == "t":
		atk = TypeChart.atkType(input("What is the attack type? "))
		dfdf = TypeChart.defType(input("What is the defender's first type? "))
		dfds = TypeChart.defType(input("What is the defender's second type? "))
		if atk > 17 or dfdf > 17 or dfds == 19:
			print("One or more of your types are invalid.")
		elif dfds == 18:
			if TypeChart.typeChart[atk][dfdf] == 1:
				print("Normal effectiveness.")
			elif TypeChart.typeChart[atk][dfdf] == 2:
				print("Super effective!")
			elif TypeChart.typeChart[atk][dfdf] == .5:
				print("Not very effective...")
			elif TypeChart.typeChart[atk][dfdf] == 0:
				print("No effect...")
			else:
				print("I don't know how effective that was...")
		elif dfds < 18:
			defend = TypeChart.typeChart[atk][dfdf] * TypeChart.typeChart[atk][dfds]
			if defend == 1:
				print("Normal effectiveness")
			elif defend == 2 or defend == 4:
				print("Super effective!")
			elif defend == .5 or defend == .25:
				print("Not very effective...")
			elif defend == 0:
				print("No effect...")
			else:
				print("I don't know how effective that was...")
				
	# If the user wants to do a dice roll, ask for the number of dice to
	#   roll and the number of sides, then return the results.
	elif user.lower() == "r":
		dice = int(input("How many dice to roll? "))
		sides = int(input("How many sides per die? "))
		for i in range(1,dice+1):
			roll = randint(1,sides)
			print(roll)
			print("")
		print("End of roll.")
		
	# If the user wants to search for a Pokedex number, ask them for the
	#   Pokemon's name and return the dex number.
	elif user.lower() == "d":
		dex = input("Enter the Pokemon's name. ")
		print(Pokedex.dexSearch(dex))
		
	# If the user doesn't choose any of the above options, they either want to
	#   quit or entered the command wrong. If they want to quit, make them
	#   confirm. Otherwise, tell them that the command is wrong.
	else:
		if user.lower() == "e":
			user = input("Type 'e' again to confirm. Otherwise, type any other character. ")
		else:
			print("I don't recognize the command " + user + ".")
	print("")
	print("")
