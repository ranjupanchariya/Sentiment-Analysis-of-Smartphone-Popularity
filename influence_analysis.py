import csv

def analyze():
	f = open("graph.csv")
	content = []
	try:
		r = csv.reader(f)
		for row in r:
			content.append(row)

	finally:
		f.close()
	
	votes = {}
	voteto = {}
	
	for i in range(1, 900):
		votes[i] = 0
		voteto[i] = 0

	o = open("votes.txt", 'w')

	for i in range(len(content)):
		content[i][0] = int(content[i][0])	
		content[i][1] = int(content[i][1])	
		content[i][2] = int(content[i][2])
	
	for i in range(1, 900):
		maxim  = -1
		j = 0
		while j < len(content):
			if content[j][0] == i and content[j][2] > maxim:
				maxim = content[j][2]
				voteto[i] = content[j][1]
			else:
				pass
			j = j + 1
		if voteto[i] > 0:	
			votes[voteto[i]] = votes[voteto[i]] + 1

	high = 0
	guy = 0
	for i in range(1, 900):
		o.write(str(i) + " " + str(votes[i]) + "\n")
		if votes[i] > high:
			high = votes[i]
			guy = i

	o.close()
	return votes
if __name__ == "__main__":
	analyze()
