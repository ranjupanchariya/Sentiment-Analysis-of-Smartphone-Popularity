import random
import csv
from influence_analysis import analyze
import nltk
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize


def word_feats(words):
    return dict([(word, True) for word in words])
 
negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')
 
negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
negcutoff = len(negfeats)
poscutoff = len(posfeats)
 
trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
 
classifier = NaiveBayesClassifier.train(trainfeats)
#classifier.show_most_informative_features()

votes = {}
votes = analyze()
f = open("reviews.csv","r")
p = 0.0
pos = 0.0
tot = 0.0

content = []
scores = []

print "Reading file..."
try:
	reader = csv.reader(f)
	for row in reader:
		if len(row)>0:
			content.append(row)
		else:
			pass
finally:
	f.close()

print "Calculating for all phones"
for i in range(len(content)):
	if content[i][2] == "iphone7":
		st = content[i][3]
		document = word_tokenize(st)
		features = word_feats(document)
		ans = classifier.classify(features)
		if ans is 'pos':
			ans='positive'
			pos = pos + 1 + (float(votes[i])/10)
			tot = tot + 1 + (float(votes[i])/10)
		elif ans is 'neg':
			ans='negative'
			tot = tot + 1 + (float(votes[i])/10)
p = (pos / tot) * 100
l = [p, "iphone7"]
scores.append(l)

p = 0.0
pos = 0.0
tot = 0.0

for i in range(len(content)):
	if content[i][2] == "galaxys7":
		st = content[i][3]
		document = word_tokenize(st)
		features = word_feats(document)
		ans = classifier.classify(features)
		if ans is 'pos':
			ans='positive'
			pos = pos + 1 + (float(votes[i])/10)
			tot = tot + 1 + (float(votes[i])/10)
		elif ans is 'neg':
			ans='negative'
			tot = tot + 1 + (float(votes[i])/10)
p = (pos / tot) * 100
l = [p, "galaxys7"]
scores.append(l)

p = 0.0
pos = 0.0
tot = 0.0

for i in range(len(content)):
	if content[i][2] == "motoz":
		st = content[i][3]
		document = word_tokenize(st)
		features = word_feats(document)
		ans = classifier.classify(features)
		if ans is 'pos':
			ans='positive'
			pos = pos + 1 + (float(votes[i])/10)
			tot = tot + 1 + (float(votes[i])/10)
		elif ans is 'neg':
			ans='negative'
			tot = tot + 1 + (float(votes[i])/10)
p = (pos / tot) * 100
l = [p, "motoz"]
scores.append(l)

p = 0.0
pos = 0.0
tot = 0.0

for i in range(len(content)):
	if content[i][2] == "leeco":
		st = content[i][3]
		document = word_tokenize(st)
		features = word_feats(document)
		ans = classifier.classify(features)
		if ans is 'pos':
			ans='positive'
			pos = pos + 1 + (float(votes[i])/10)
			tot = tot + 1 + (float(votes[i])/10)
		elif ans is 'neg':
			ans='negative'
			tot = tot + 1 + (float(votes[i])/10)
p = (pos / tot) * 100
l = [p, "leeco"]
scores.append(l)
		
p = 0.0
pos = 0.0
tot = 0.0

for i in range(len(content)):
	if content[i][2] == "xz":
		st = content[i][3]
		document = word_tokenize(st)
		features = word_feats(document)
		ans = classifier.classify(features)
		if ans is 'pos':
			ans='positive'
			pos = pos + 1 + (float(votes[i])/10)
			tot = tot + 1 + (float(votes[i])/10)
		elif ans is 'neg':
			ans='negative'
			tot = tot + 1 + (float(votes[i])/10)
p = (pos / tot) * 100
l = [p, "xz"]
scores.append(l)

p = 0.0
pos = 0.0
tot = 0.0

for i in range(len(content)):
	if content[i][2] == "pixel":
		st = content[i][3]
		document = word_tokenize(st)
		features = word_feats(document)
		ans = classifier.classify(features)
		if ans is 'pos':
			ans='positive'
			pos = pos + 1 + (float(votes[i])/10)
			tot = tot + 1 + (float(votes[i])/10)
		elif ans is 'neg':
			ans='negative'
			tot = tot + 1 + (float(votes[i])/10)
p = (pos / tot) * 100
l = [p, "pixel"]
scores.append(l)


pos = 0.0
tot = 0.0

for i in range(len(content)):
	if content[i][2] == "xiomimi5":
		st = content[i][3]
		document = word_tokenize(st)
		features = word_feats(document)
		ans = classifier.classify(features)
		if ans is 'pos':
			ans='positive'
			pos = pos + 1 + (float(votes[i])/10)
			tot = tot + 1 + (float(votes[i])/10)
		elif ans is 'neg':
			ans='negative'
			tot = tot + 1 + (float(votes[i])/10)
p = (pos / tot) * 100
l = [p, "xiomimi5"]
scores.append(l)

pos = 0.0
tot = 0.0

for i in range(len(content)):
	if content[i][2] == "oneplus3":
		st = content[i][3]
		document = word_tokenize(st)
		features = word_feats(document)
		ans = classifier.classify(features)
		if ans is 'pos':
			ans='positive'
			pos = pos + 1 + (float(votes[i])/10)
			tot = tot + 1 + (float(votes[i])/10)
		elif ans is 'neg':
			ans='negative'
			tot = tot + 1 + (float(votes[i])/10)
p = (pos / tot) * 100
l = [p, "oneplus3"]
scores.append(l)


p = 0.0
pos = 0.0
tot = 0.0

for i in range(len(content)):
	if content[i][2] == "htc10":
		st = content[i][3]
		document = word_tokenize(st)
		features = word_feats(document)
		ans = classifier.classify(features)
		if ans is 'pos':
			ans='positive'
			pos = pos + 1 + (float(votes[i])/10)
			tot = tot + 1 + (float(votes[i])/10)
		elif ans is 'neg':
			ans='negative'
			tot = tot + 1 + (float(votes[i])/10)
p = (pos / tot) * 100
l = [p, "htc10"]
scores.append(l)

print "Sorting in Order"
for i in range(len(scores) - 1):
	mn = i
	for j in range(i+1, len(scores)):
		if scores[j][0] > scores[mn][0]:
			mn = j
	scores[i], scores[mn] = scores[mn], scores[i]

print "Smartphones and their Popularity:-"
print ""
for i in range(len(scores)):
	some = ""
	if scores[i][1] == "iphone7":
		some = "Apple iPhone 7"
		print some
		print " - %.2f" % (scores[i][0]) + "%"
	elif scores[i][1] == "galaxys7":
		some = "Samsung Galaxy S7 EDGE"
		print
		print some 
		print " - %.2f" % (scores[i][0]) + "%"
	elif scores[i][1] == "htc10":
		some = "HTC 10"
		print
		print some
		print " - %.2f" % (scores[i][0]) + "%"
	elif scores[i][1] == "xz":
		some = "Sony Xperia XZ"
		print
		print some
		print " - %.2f" % (scores[i][0]) + "%"
	elif scores[i][1] == "motoz":
		some = "Motorola MotoZ"
		print
		print some
		print " - %.2f" % (scores[i][0]) + "%"
	elif scores[i][1] == "oneplus3":
		some = "OnePlus 3"
		print
		print some
		print " - %.2f" % (scores[i][0]) + "%"
	elif scores[i][1] == "xiomimi5":
		some = "Xiaomi Mi5"
		print
		print some
		print " - %.2f" % (scores[i][0]) + "%"
	elif scores[i][1] == "pixel":
		some = "Google Pixel"
		print
		print some
		print " - %.2f" % (scores[i][0]) + "%"
	elif scores[i][1] == "leeco":
		some = "LeEco Le Pro 3"
		print
		print some
		print " - %.2f" % (scores[i][0]) + "%"
	else:
		pass

