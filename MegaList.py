canMega = [3,6,9,15,18,65,80,94,127,130,142,150,181,208,212,214,229,248,254,257,260,282,302,303,306,308,310,319,323,334,354,359,373,376,380,381,384,428,445,448,460,475,531,719]
megaForms = [6,150]

def findMega(dex):
	if dex in canMega:
		if dex in megaForms:
			return "This Pokemon has multiple Mega Evolutions."
		else:
			return "This Pokemon can Mega Evolve."
	else:
		return "This Pokemon cannot mega Evolve."