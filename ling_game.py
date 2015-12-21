from random import randint, shuffle
from sys import exit
import ling_game_strings


# Choose mode.

print "Test mode or play mode? Type 'test' or 'play' (without quotes)"
print "(In test mode, the correct answers are indicated.)"
mode = raw_input("> ")
while (mode != "test") and (mode != "play"):
	print "Invalid input: please type 'test' or 'play'."
	mode = raw_input("> ")

# Number of points at the start of the game. CHANGE THIS NUMBER
points = 100

# These are the possible languages
#	(NOTE: could make this more sophisticated by programming it to look at the imported
#	file that contains the language classes, and making the list consist of those. Would
#	also have to do something with problem_dict of course.)
languages = ["French", "Tagalog", "Luganda"]

# Dictionary associates language names to corresponding classes from the imported file
problem_dict = {"French": ling_game_strings.French(),
				"Tagalog": ling_game_strings.Tagalog(),
				"Luganda": ling_game_strings.Luganda()
			}

# Randomly assign the player one of the languages at the beginning of the game.
language_name = languages[randint(0,len(languages)-1)]

# Assign a variable "language" the actual class for the language, from the imported file
language = problem_dict[language_name]

# Basic structure of a problem. Each problem object then just supplies its own
# question and answer strings.

def RunProblem(problem):
	
	# give the function access to "points"
	global points
	
	# Print the question
	print problem[0], "\n"
		
	# Put the answers in a list so they can be shuffled.
	answers = [problem[1], problem[2], problem[3], problem[4]]
	# IF PLAYING IN TEST MODE, make sure each question indicates the correct answer.
	if mode == "test":
		answers[0] += " <- CORRECT"
	# Shuffle the answers list in place.
	shuffle(answers)
	# Dictionary for letters of answers
	answers_dict = {"a": answers[0], "b": answers[1], "c": answers[2], "d": answers[3]}
	# Print the now-shuffled answers.
	print "a)", answers[0]; print "b)", answers[1]; print "c)", answers[2]; print "d)", \
		answers[3]
		
	# Solicit user's guess
	print "\nType the letter of your answer and hit enter. (Don't type the parenthesis.)"
	# Get guess from user
	guess = raw_input("> ")
	# If guess is invalid (i.e., something other than a letter a-d), make them try again.
	while guess not in ["a", "b", "c", "d"]:
		print "You didn't type an acceptable answer. Try again."
		guess = raw_input("> ")
	
	# If they did pick one of the choices, evaluate the choice, and continue to do that
	# until it's correct.
	while guess in ["a", "b", "c", "d"]:
		# Use the guess to get the answer it corresponds to, and change guess to that answer.
		guess = answers_dict[guess]
		# The second position in each problem list will be the correct answer, so if it's this,
		# they got it right. Print "correct".
		if (guess == problem[1]) or (guess == problem[1] + " <- CORRECT"):
			print "\nCorrect!\n"
		# If not, subtract a point and make them try again.
		elif guess != problem[1]:
			points -= 1
			print "Sorry, try again."
			guess = raw_input("> ")
			while guess not in ["a", "b", "c", "d"]:
				print "You didn't type an acceptable answer. Try again."
				guess = raw_input("> ")


# Each room introduces itself, calls the RunProblem() function on the three problems that
# correspond to that room, tells you your score, then returns the name of the next room to
# the Engine.

class Room(object):

	# List this room's puzzles. List to be overridden by each Room instance.	
	puzzles = []
	
	# Function that runs all the puzzles.
	def DoPuzzles(self):
		for puzzle in self.puzzles:
			RunProblem(puzzle)
	
	def __init__(self):
	
		# Intro text. The field name is taken from the name of the room, and uncapitalized.
		field_name = self.__class__.__name__.lower()
		self.intro_text = "Welcome to the %s room.\nPlease solve the following problems in the field of %s %s.\n" % (
							field_name, language_name, field_name)

		# Print the intro text.
		print self.intro_text
		# Do the puzzles.
		self.DoPuzzles()
		# Allow the room to take its leave.
		print "Good job: you have completed the %s room." % field_name
		print "You have %d points left." % points
		print "Now on to the next room.\n"


class Phonetics(Room):
	
	puzzles = [language.phone1, language.phone2, language.phone3]
	next_room = "phonology"
	

class Phonology(Room):
	
	next_room = "morphology"
	puzzles = [language.phono1, language.phono2, language.phono3]
	

class Morphology(Room):
	
	next_room = "syntax"
	puzzles = [language.morph1, language.morph2, language.morph3]
	
	
class Syntax(Room):
	
	next_room = "results"
	puzzles = [language.syn1, language.syn2, language.syn3]
	

class Results(Room):
	
	# Override the init function because this room has no puzzles.
	def __init__(self):
		
		print "You have completed the game. Your final score is %d." % points
	
	# Set next_room to None, so the Engine knows to exit the game.
	next_room = None

class Engine(object):
	
	def __init__(self):
		
		# Dictionary matching names of rooms to the classes.
		self.rooms = {"phonetics": Phonetics, "phonology": Phonology,
						"morphology": Morphology, "syntax": Syntax, "results": Results
					}
		
		# Set the next (in this case, first) room.
		self.next = "phonetics"
		
		# The last thing each room does is to change self.next to the key for the
		# following room. Thus, a while loop that runs the room corresponding to self.next
		# will run through all the rooms sequentially.
		while True:
			self.rooms[self.next]()
			self.next = self.rooms[self.next].next_room
			if self.next == None:
				exit()

Engine()

# OUTLINE OF GAME:

# linguistic fieldwork game. Each room represents a level of structure (phonetics, etc.) and
#    you have to figure out the puzzle before moving on. At the beginning of the game
#    you are randomly assigned one of several languages (it doesn't tell you which) and the
#    puzzles in all the rooms are about that language. You start with a certain number of points
#    and then lose them during the game for wrong guesses. At the end you are told how many
#    points you got and given one of three different 'congratulations' messages depending
#    how many points that was. You have to give your name at the beginning of the game.
# Phonetics room:
#    You have to describe three segments. For each segment, an impressionistic description
#    is given, and then you guess from a list of phonetic descriptions (e.g., "voiced palatal
#    stop") which sound it is. You have three guesses out of four, then you lose. 
# Phonology room:
#    You solve three phonology problems. One is on syllable structure, the next is on some
#    segmental phonological process, and the third is on some aspect of prosody.
# Morphology room:
#    Three morphology problems. One on the plural, one on something tense/aspect-related,
#    one on whatever is most atypical about the given language.
# Syntax room:
#    The final challenge room. Only one problem.
# Result room:
#    Professor Oak comes out to congratulate you. He tells you you've passed the game and
#    how many points you have. Then he says that by the way, he's taken the liberty of
#    submitting your work for publication, and he hands you a book. You open the book and it
#    prints a text file: "A Grammar of [Language Name], by [Your Name]." Etc. It has a
#    table of contents and then in each section are the rules you figured out.

# Rooms:
#   phonetics room, phonology room, morphology room, syntax room, result room.
# Variables:
#   your name, the language name, how many points you have (modified by each room).
# Lists:
#   the languages
# Other:
#   each language is a class, with a function for each room; the function gives you the
#   puzzles corresponding to that room and changes your point count accordingly. The
#   functions should be named consistently so the main engine can call them the same way
#   for each room.

# Representing the sets of problems for each language.
# Each language is a class.			E.g.,						French()
# It has variables for each field.								self.morphology = ... 
# (Using consistent names allows the rooms to call the problems in a generic way
# regardless of the language.)
# Each field variable corresponds to a list of problems.		[self.morph1, self.morph2...]
# Each problem consists of a list of strings.					self.morph1 = ["quest", "ans"...]

# There is a 'problem-runner' that goes to a problem, takes its
# questions and answers, and runs them in a consistent way.
# 
# languages: each language is a CLASS, e.g. French(). it contains fields.
# field: each field is a LIST of problems. bind each problem to a VARIABLE.
# problem: each problem is a LIST of STRINGS (question and answers)

# The class for each language is imported from ling_game_strings.py.
# (Importing them (a) makes the program itself cleaner, and (b) allows you to easily
# switch out/add puzzles by writing a new file, without modifying the program itself.


# HOW I SOLVED SOME PROBLEMS

# Below are some old errors and my thought processes while trying to fix them. Also, some
# parts of the program where I changed my mind on how to do them. This was all written for
# myself as a went along, so may not make much sense.

# error in RunProblems(): IndexError, and it's index 0, so that means it's not finding the
	#   list at all. That means it's using the Room()'s version of "puzzles", which is an
	#   empty list, rather than Phonetics()'s version, which has three items.
	
	# POTENTIAL FIXES
	# 1.
	# This might be fixable if I declare self.puzzles in init of Room(), then use super to
	# inherit the init function in each of the child classes, and override self-puzzles in
	# each of those inits. But since the init function itself uses the self.puzzles variable,
	# assuming the whole init runs before the part that's overridden is changed, wouldn't
	# the override be too late?
	#
	# RESULT: The program now completely skips the problems.
	# The DoPuzzles() function is defined inside Room(), but outside init. It uses the
	# variable self.puzzles. But when this function is called inside init, it can't see
	# the variable self.puzzles, which is defined inside init, at all.
	#
	# 2.
	# Define DoPuzzles() inside init.
	#
	# RESULT: First I get "AttributeError: 'Phonology' object has no attribute 'DoPuzzles'".
	# This is because the function is now defined inside init rather than as a class method.
	# I changed the line "self.DoPuzzles()" to "DoPuzzles(self)", so it would run the
	# function instead of looking for a class method. Now the program goes back to
	# completely ignoring this line (i.e., I assume, it can't find self.puzzles, so assumes
	# it's empty, so the for-loop does nothing).
	#
	# 3.
	# The IndexError is better than the skipping, because the IndexError means it's at
	# least reaching the stage where it calls RunProblem(). So, I took puzzles back out of
	# init.
	#
	# 4.
	# (wrong) Figured it out (I think). self.puzzles is a list of STRINGS. my for-loop in the
	# definition of DoPuzzles() in the Room() class says, "for each object in puzzles..."
	# but each object in puzzles is a string, NOT a list of strings. So it should run
	# RunProblem() on the ...wait, let me test something. Ok, I changed "print problem[0]"
	# to "print problem", and it printed "[]". This means that it is looking at Room()'s
	# version, not Phonetics()'s version, of self.puzzles. Also, self.puzzles IS a list of
	# lists, not a list of strings. The first item in self.puzzles for phonetics is
	# "language.phone1", which refers to French.phone1, which as can be seen in
	# ling_game_strings.py is actually a list of strings.
	#
	# 5.
	# Want to test whether "self" in an implicitly inherited __init__() method refers to
	# the superclass or the subclass. Tested using Python in Terminal with a simple
	# example, showing that self refers to the subclass.
	#
	#	class Orthography(object):
	#		kind = "unspecified"
	#		def __init__(self):
	#			print self.kind
	#
	#	class Abjad(Orthography):
	#		kind = "abjad"
	#	
	# arabic = Abjad()
	# abjad
	#
	# So why, in Phonetics(), when the inherited __init__() method from Room() calls
	# self.puzzles, does it return a blank list of puzzles, which would seem to be from
	# Room(), not Phonetics()? Aha: the function DoPuzzles() is a class function of Room(),
	# and is outside of __init__(). DoPuzzles() uses self, and since it's a class function,
	# maybe the self that is uses is the superclass's self. Testing this hypothesis in
	# Terminal: no, the answer to the question at the beginning of this section is that it
	# refers to the subclass. E.g.:
	#
	#	class Family(object):
	#		kind = "family"
	#		def Branch(self):
	#			print self.kind
	##				self.Branch()
	#	 
	#	class Algic(Family):
	#		kind = "Algic"
	#
	#	yurok = Algic()
	#	Algic
	#
	# 6.
	# I changed Room().puzzles to ["test1", "test2"]. It still gets an IndexError on
	# problem[0]. Therefore it's not accessing the Room() version of puzzles either.
	# 
	# 7.
	# Every step of this process (should test at each step):
	# a. Phonetics() inherits Room()'s __init__() function
	# b. this function calls Room()'s DoPuzzles() function on self.puzzles
	# c. self.puzzles should be [language.phone1, language.phone2, language.phone3]
	#		...and language is, e.g., ling_game_strings.French()
	# d. DoPuzzles() runs RunProblem() on every item in self.puzzles
	# e. RunProblem() starts by printing the first item in whatever it's called on, which
	#		should be a list. (This is where the IndexError happens)
	# Results of testing:
	# a-b: both of these work, they're in the traceback.
	# c: not sure, the problem could be here
	# d: DoPuzzles() seems to work: I changed self.puzzles to
	#		[["test", "test"], ["test", "test"]] and it printed test, not IndexError.
	# e: This works, as explained in d.
	# 
	# 8. It looks like the Engine is actually calling the Phonology() room, not the
	# Phonetics() room first. I figured this out by changing the phonology strings in 
	# ling_game_strings to "tada". It printed "tada". So either it's calling the Phonology()
	# room instead of the Phonetics() room, or it's assigning self.next to the output of
	# Phonetics() as it should, but somehow not actually running Phonetics(), which
	# requires it to print stuff and get input. If that is the case, how is it getting the
	# output without running it?
	#
	# Actually, the Phonetics() room incorrectly calls the phonology problems. I tested 
	# this by having the Engine run Phonetics(), and also by deleting the puzzles from the
	# Phonology() room, which makes it skip the problems instead of returning the IndexError.
	# Why is this happening?
	#
	# 9.
	# When I have the engine run Phonetics(), rather than the line
	# "self.next_room = Phonetics()" which tries to assign the output of Phonetics() to a
	# variable, Phonetics() runs perfectly. Leaves two questions: 1) why do I get the
	# index error and wrong strings the other way? I realize now you can't have __init__()
	# return stuff, so I have to do the room transitions another way (exercise 43 has a
	# class function "Enter()" that handles all the action, rather than __init__() doing it),
	# but what exactly is happening when I do "self.next_room = Phonetics()"? 2) How should
	# I now handle the room transitions?
	#
	# 1) Duh-- "x = Class()" creates an instance of that class.
	#	a. When Engine() does Phonetics() first thing, it works.
	#	b. When it first creates the self.rooms dictionary, which maps room names to the
	#		correct classes for those rooms, it crashes with the IndexError because it's
	#		taking the phonology strings instead of the phonetics ones. This has something
	#		to do with the following two facts: the string "phonology" is mapped to the
	#		Phonology() class in the self.rooms dictionary; (<- RIGHT | IRRELEVANT ->) and Phonetics() has a variable
	#		next_room that is assigned to the string "phonology". So perhaps somehow
	#		Phonetics() calls Phonology() instead of itself. But how?
	#	c. OHHH--when the dictionary is created, the fact that it contains "Phonology()"
	#		makes it call Phonology().__init__(). So now the question is simply, how can I
	#		create a dictionary mapping strings to classes without calling the initializer
	#		of those classes. Can I just leave off the parentheses, and put them in later?
	#		...Yes! Tested in Terminal and if a dictionary value is a class or a class
	#		method without parentheses, you can call the class/method like this:
	#			dictionary[key]()


# problem: in Room(), it used to skip DoPuzzles() entirely.
		# Aha: class vs. instance variables.
		#
		# - Variables defined outside __init__ are STATIC CLASS VARIABLES, and changing
		#    them changes them for the whole class.
		# - Variables defined inside __init__ are INSTANCE/OBJECT variables, and you can
		#    change them for individual objects.
		# http://stackoverflow.com/questions/9056957/correct-way-to-define-class-variables-in-python
		# https://timothyawiseman.wordpress.com/2012/10/06/class-and-instance-variables-in-python-2-7/
		# I want "puzzles" to be an instance variable.
		#
		# Ways to do this:
		# 1. I could leave puzzles undefined in the base class, Room(), and define it as a
		#    class variable in each room individually. Then I would just change Room's
		#    __init__ code to say puzzles instead of self.puzzles, since it's not an
		#    instance variable. Potential problem: is it a problem that the base class
		#    includes code referring to a variable that doesn't exist yet? <- (Yes, tested)
		#      (But you still use the "self." prefix, whether instance or class variable.)
		#      (For class variables: when DECLARING, you don't use self; when using them, you do.)
		#      (For instance variables (declared inside function): you use self in both cases.)
		# 2. I could have puzzles as a class variable in Room(), and then just override it
		#    in each subclass. This would be to eliminate the problem from option 1, if it
		#    is actually a problem. <- (It is)
		# (Note to self: when experimenting with class vs. instance variables, I keep
		# confusing instances of the SAME class with instances of different classes that
		# both inherit from the same metaclass. So, pay attention to that.)


# OLD STUFF
#				This is stuff I changed my mind on how to do. I'm keeping it down here
#				just in case.

#		(1)
#class Problem(object):
#	
#	# Each problem supplies its own question, correct answer, and three wrong answers.
#	self.question = "sample text"
#	self.correct_answer = "sample text"
#	self.incorrect_answers = []
#	
#	# The answers list is shuffled each time.
#	self.answers_list = shuffle([self.correct_answer, self.incorrect_answers[1],
#						self.incorrect_answers[2], self.incorrect_answers[3]
#					])
#	
#	def enter():
#		print question
#		print ("\n", answers_list[0])
#		print answers_list[1] 
#		print answers_list[2]
#		print answers_list[3]
#		guess = raw_input("> ")
#		while guess != correct_answer:
#			points -= 1
#			guess = raw_input("> ")
#		if guess = correct_answer:
#			return 'correct'

#		(2)
# ABANDONED ALTERNATIVE: Associating languages with problems doesn't use functions, so could be done
# without classes. A language is instead a dictionary. Key = a field, value = a variable
# corresponding to the list of problems; the rest is the same. The problem is the variable
# names become increasingly long and there's a ton of them not organized very well.
# Sample is below, commented out.
#
# Dictionary of fields for the French language.
# french = {"Phonetics": french_phone, "Phonology": french_phono, "Morphology": french_morp,
#			"Syntax": french_syn
#		}
#
# For the field of phonetics, here is the list of problems.
# french_phone = [french_phone_1, french_phone_2, french_phone_3]
#
# For the first problem, here is the list of strings
# french_phone_1 = (french_phone_1_question, french_phone_1_correct,
#				french_phone_1_incorrect1, french_phone_1_incorrect_2, french_phone_1_incorrect_3
#			)
#
# The actual strings:
#french_phone_1_question = "Question about French phonetics?"
#french_phone_1_correct = "Correct answer"
#french_phone_1_incorrect1 = "Wrong answer #1"
#french_phone_1_incorrect2 = "Wrong answer #2"
#french_phone_1_incorrect3 = "Wrong answer #3"
#
#tagalog = {}
#luganda = {}

# REQUIREMENTS OF LPTHW EXERCISE 45

# Use more than one file, and use import to use them.
# Use one class per room and give the classes names that fit their purpose
# make a class that runs them and knows about them
# classes
# functions
# dicts
# lists