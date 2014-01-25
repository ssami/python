#!/usr/bin/python


def south_indian_surname (name):

	"""
		A very simplistic way of determining of someone 
		has a South or North Indian surname. 

		It takes a 'defining letter' of 'a' and uses that 
		to determine the density of defining words within 
		the given name.

	"""

	from decimal import Decimal 
	import math

	# the defining letter and the threshold 
	def_lett = 'a' 

	num_def_lett = len([x for x in name if x == def_lett])
	lett_density = float(num_def_lett) / float(guess_indian_syllables(name))
	
	return lett_density


def south_indian_surname_features (name):

	return {'letter_density' : south_indian_surname(name)}


def surname_features(name):

	return {

		'name_length' : len(name), 
		'a_count' : len([x for x in name if x == 'a']) ,
		'syllable_guess' : guess_indian_syllables(name)
	}

def guess_indian_syllables(word): 

	"""
		An extremely simple syllable guesstimator that 
		counts the number of syllables an Indian name might have. 
	"""

	import string

	letters = [x for x in string.lowercase]
	vowels = ['a', 'e', 'i', 'o', 'u']

	syllable_count = 0
	for l in word: 
		if l in vowels: 
			seglist = list(word.partition(l))
			syllable_count += 1
			word = seglist[2]		# we keep only the remaining word to split

	if word and (list(word))[-1] == 'y': 			# 'y' also counts as an 'i' so we pretend it's another vowel
		syllable_count += 1

	return syllable_count



def train_test(south_names, north_names):

	"""
		Takes in data in the form of two text files, 
		one for south and the other for north names. 
	"""

	import nltk

	f = open(south_names, 'r')
	south_surnames = []
	for line in f: 
		line = line.rstrip()
		if line: 
			south_surnames.append(line)

	f2 = open(north_names, 'r')
	north_surnames = []
	for line in f2: 
		line = line.rstrip()
		if line: 
			north_surnames.append(line)



	name_tuples = ([(name, 'south') for name in south_surnames] + [(name, 'north') for name in north_surnames])
	import random 
	random.shuffle(name_tuples)

	featuresets = [(surname_features(n), d) for (n, d) in name_tuples]
	train_set = featuresets[len(featuresets)/2:]
	test_set = featuresets[:len(featuresets)/2]
	classifier = nltk.NaiveBayesClassifier.train(train_set)

	print nltk.classify.accuracy(classifier, test_set)

	return classifier


def check_classifier(classifier, name):

	print "The classifier thinks", name, "is a", classifier.classify(surname_features(name)), "Indian name"
