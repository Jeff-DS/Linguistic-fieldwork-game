# -*- coding: utf-8 -*-

# Note: I originally used pseudo-questions of the following form:
#
# ["French phonetics question 1?", "Correct answer", "Wrong answer 1",
#				"Wrong answer 2", "Wrong answer 3"]
#
# This saved me the trouble of writing 36 linguistics problems about the analysis of
# random languages I don't know, and since the point of the project was coding practice,
# not linguistics practice, it didn't really matter. I have now started to fill in
# questions resembling actual linguistics problems, but have not gotten all the way
# through.


# One class per language.
#
# One list per problem, named as follows: "self.field#", where field is the subfield
#	of linguistics, and # is the number of the problem, 1 through 3.
#
# Each problem consists of five strings, in this order: the question, the correct answer,
#	and three incorrect answers.


class French(object):

	phone1 = [("You ask for the word for 'red.' The word begins with a consonant that "
				"sounds like a gargle. What is it?"),
				"Voiced uvular fricative",
				"Voiceless pharyngeal stop",
				"Mid back rounded vowel",
				"Voiced velar stop"
				]
	phone2 = ["You ask for the name of the city your consultant is from. It sounds kind "
				"of like \"ranz\", but in an [nz] cluster, you might expect " # the city is Reims
				"to hear an excrescent [d], and no matter how many times your consultant "
				"repeats the word, you hear none. What is the most likely reason for this?",
				"There is actually no [n]; the vowel is nasal.",
				"You're not listening hard enough.",
				"The [z] is aspirated, obscuring the excrescent consonant.",
				"Your perception is incorrectly reversing the order of the segments."
				]
	phone3 = ["Your consultant says a word with a funny vowel in it. You push the corners "
				"of their lips apart as they say the vowel, and now it sounds like the "
				"vowel in the American English pronunciation of pet. What is the original "
				"vowel?",
				"Low-mid front rounded",
				"Low-mid front unrounded",
				"Low central rounded",
				"Mid back rounded"
				]
	
	phono1 = ["You observe that in some words, a final schwa deletes when a vowel-initial "
				"word follows. Which of the following phonological rules best captures "
				"this fact?",
				"schwa --> null / _# V",
				"null --> schwa / _# V",
				"V --> null / schwa_#",
				"V --> -V / _#"]
	phono2 = ["During your elicitation sessions, you have discovered that sometimes, but "
				"not always, a [z] appears between the plural definite article and the "
				"following word. For example, consider the following data, in which the "
				"isolation form of the plural noun is given in the first column, followed "
				"by the article + noun, then the gloss:\n\n"
				"[ami]\t\t[lezami]\t\t'the friends'\n"
				"[ɑ̃fɑ̃]\t\t[lezɑ̃fɑ̃]\t\t'the children'\n"
				"[ɔ̃bʁə]\t\t[lezɔ̃bʁə]\t\t'the shadows'\n\n"
				"but:\n\n"
				"[gæʁsɔ̃]\t\t[legæʁsɔ̃]\t\t'the boys'\n"
				"[fi]\t\t[lefi]\t\t'the girls'\n"
				"[pwaʁ]\t\t[lepwaʁ]\t\t'the pears'\n\n"
				"Note: [ale] 'gone', [ɑ̃] 'to', [aleɑ̃nɑ̃gləteʁ] 'gone/went to England'"
				"\n\nWhat is the best analysis of the data so far?",
				"The underlying form of the article is /lez/, and z --> null / _#C",
				"The underlying form of the article is /le/, and null --> z / _#V",
				"The presence or absence of [z] is determined by the animacy of the noun.",
				"There is no phonological pattern; nouns select for their allomorph."]
	phono3 = ["All words appear to be stressed on the last syllable. What's the analysis?",
				"Regular word-final stress; there is no underlying stress.",
				"Lexical, underlying stress that always happens to be final (so far).",
				"The language has no stress pattern.",
				"This is in fact a tone pattern, with regular final H tone."]
	
	morph1 = ["Based on the following examples, how does this language pluralize nouns?"
				"\n\n"
				"SG\t\tPL\t\tgloss\n\n"
				"mɛzɔ̃\t\tmɛzɔ̃\t\thouse\n"
				"gæto\t\tgæto\t\tcake\n"
				"tɔʁty\t\ttɔʁty\t\tturtle",
				"There appears to be no overt plural morpheme on nouns.",
				"The language does not distinguish singular from plural at all.",
				"Pluralization must be syntactic rather than morphological.",
				"There is a length distinction."]
	morph2 = ["Examine the following first-person forms of the verb 'to speak':\n\n"
				"\tPRES\tPST\tFUT\t\tPST.IPFV.SBJV\n"
				"SG\tpaʁl\tpaʁle\tpaʁləʁe\t\tpaʁlas\n"
				"PL\tpaʁlɔ̃\tpaʁlɑm\tpaʁləʁɔ̃\t\tpaʁlasjɔ̃\n\n"
				"Although the forms do not seem entirely reducible to a set of underlying "
				"morphemes, if we had to ascribe some phonological element to a 1PL "
				"morpheme, the most likely candidate would be ____.",
				"nasality",
				"the sequence /paʁl/",
				"/e/",
				"[+front]"]
	morph3 = ["You know the 2PL.PRES and .FUT form of 'go' is [ale]. Your consultant translates "
				"the sentence [ʒə swɛt kə vuz alje] as 'I hope you.PL go.' You confirm "
				"that the consultant considers [alje] and [ale] to be forms of the same "
				"verb, and that using [ale] here would be ungrammatical. What's going "
				"on?",
				"[alje] is some kind of subjunctive form.",
				"A penultimate [j] infix is added to the end of all sentences.",
				"The underlying form of the verb is revealed in the future tense.",
				"The two forms are in free variation."]
	
	syn1 = ["French syntax question 1?",
			"Correct answer",
			"Wrong answer 1",
			"Wrong answer 2",
			"Wrong answer 3"]
	syn2 = ["French syntax question 2?",
			"Correct answer",
			"Wrong answer 1",
			"Wrong answer 2",
			"Wrong answer 3"]
	syn3 = ["French syntax question 3?",
			"Correct answer",
			"Wrong answer 1",
			"Wrong answer 2",
			"Wrong answer 3"]

class Luganda(object):

	phone1 = ["When giving certain words beginning with stops, your consultant always "
				"seems to pause. This happens consistently with these words, and equally "
				"consistently does not happen with other stop-initial words. What's "
				"going on?",
				"Initial gemination. The silence is the elongated stop closure.",
				"These stops are articulated further back in the vocal tract.",
				"These are reverse affricates.",
				"The consultant has a stutter."
				]
	phone2 = ["Different words seem to be spoken to different melodies, even words that "
				"are otherwise homophonous. What's going on?",
				"The language is tonal.",
				"The consultant is using list intonation.",
				"This happens when consultants become bored by long elicitation sessions.",
				"The pitch variations are conditioned by raisor and depressor consonants."
				]
	phone3 = ["Words with [ç] or [tʃ] are sometimes uttered with one of these consonants, "
				"sometimes the other. What's going on?",
				"The two sounds are in free variation.",		# I don't know if this is actually true for Luganda.
				"These are allophones conditioned by the phonological environment.",
				"[tʃ] is the geminated version of [ç].",
				"These are different tenses."
				]
	
	phono1 = ["Looking through your notes, you notice that [ɾ] occurs only after [i] or "
				"[e], and [l] occurs only word-initially or after [a], [o], or [u]. Which "
				"analysis best captures these facts?",		
				"/l/ -> [r] / V[+front] _ ",
				"/r/ -> [l] / {#, V[-front]} _",
				"/l/ and /ɾ/ are two different phonemes.",
				"/l/ -> [r] / _ V[+front]"]
# source: https://books.google.com/books?id=4TgoAAAAQBAJ&pg=PA68&lpg=PA68&dq=l+and+r+in+luganda&source=bl&ots=3E79Zo5YBb&sig=UMNyGqLB3dNzxSgRF7UqY5zWiMo&hl=en&sa=X&ved=0ahUKEwjL463a3OPJAhWCaz4KHUk6AHsQ6AEILjAD#v=onepage&q=l%20and%20r%20in%20luganda&f=false

	phono2 = ["Consider the following: \n"
				"/n-/\t+\t/-laba/\t-->\t/n̩dába/\n"
				"What's going on?",
				"/l/ -> [d] / n_",
				"/d/ -> [l] / _a",
				"/l/ -> [d] / _n",
				"/d/ -> [n]"]
	phono3 = ["Which Optimality Theory constraint would motivate the following "
				"alternation?\n"
				"/a-/\t+\t/sóma/\t->\t[asóma]\n"
				"/bá-/\t+\t/sóma/\t->\t[básomá]",
				"*HH",
				"*HLH, *LHL",
				"*STRUC",
				"*H#"]
	
	morph1 = ["Luganda morphology question 1?",
				"Correct answer",
				"Wrong answer 1",
				"Wrong answer 2",
				"Wrong answer 3"]
	morph2 = ["Luganda morphology question 2?",
				"Correct answer",
				"Wrong answer 1",
				"Wrong answer 2",
				"Wrong answer 3"]
	morph3 = ["Luganda morphology question 3?",
				"Correct answer",
				"Wrong answer 1",
				"Wrong answer 2",
				"Wrong answer 3"]
	
	syn1 = ["Luganda syntax question 1?",
			"Correct answer",
			"Wrong answer 1",
			"Wrong answer 2",
			"Wrong answer 3"]
	syn2 = ["Luganda syntax question 2?",
			"Correct answer",
			"Wrong answer 1",
			"Wrong answer 2",
			"Wrong answer 3"]
	syn3 = ["Luganda syntax question 3?",
			"Correct answer",
			"Wrong answer 1",
			"Wrong answer 2",
			"Wrong answer 3"]

class Tagalog(object):

	phone1 = ["Tagalog phonetics question 1?",
				"Correct answer",
				"Wrong answer 1",
				"Wrong answer 2",
				"Wrong answer 3"
				]
	phone2 = ["Tagalog phonetics question 2?",
				"Correct answer",
				"Wrong answer 1",
				"Wrong answer 2",
				"Wrong answer 3"
				]
	phone3 = ["Tagalog phonetics question 3?",
				"Correct answer",
				"Wrong answer 1",
				"Wrong answer 2",
				"Wrong answer 3"
				]
	
	phono1 = ["Tagalog phonology question 1?",
				"Correct answer",
				"Wrong answer 1",
				"Wrong answer 2",
				"Wrong answer 3"]
	phono2 = ["Tagalog phonology question 2?",
				"Correct answer",
				"Wrong answer 1",
				"Wrong answer 2",
				"Wrong answer 3"]
	phono3 = ["Tagalog phonology question 3?",
				"Correct answer",
				"Wrong answer 1",
				"Wrong answer 2",
				"Wrong answer 3"]
	
	morph1 = ["Tagalog morphology question 1?",
				"Correct answer",
				"Wrong answer 1",
				"Wrong answer 2",
				"Wrong answer 3"]
	morph2 = ["Tagalog morphology question 2?",
				"Correct answer",
				"Wrong answer 1",
				"Wrong answer 2",
				"Wrong answer 3"]
	morph3 = ["Tagalog morphology question 3?",
				"Correct answer",
				"Wrong answer 1",
				"Wrong answer 2",
				"Wrong answer 3"]
	
	syn1 = ["Tagalog syntax question 1?",
			"Correct answer",
			"Wrong answer 1",
			"Wrong answer 2",
			"Wrong answer 3"]
	syn2 = ["Tagalog syntax question 2?",
			"Correct answer",
			"Wrong answer 1",
			"Wrong answer 2",
			"Wrong answer 3"]
	syn3 = ["Tagalog syntax question 3?",
			"Correct answer",
			"Wrong answer 1",
			"Wrong answer 2",
			"Wrong answer 3"]

	# OLD APPROACH
	# Each field is a list of problems.
	#self.phonetics = [phone1, phone2, phone3]
	#self.phonology = [phono1, phono2, phono3]
	#self.morphology = [morph1, morph2, morph3]
	#self.syntax = [syn1, syn2, syn3]
