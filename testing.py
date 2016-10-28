import random
import time

def temp_converter():
	temp_num = float(input("Enter a temperature: "))
	opt = raw_input("Convert to (F)ahrenheit or (C)elsius?: ")
	if opt.upper() == "F":
		converted = (temp_num * 9/5) + 32
		print ("%s C = %s F" %(temp_num, converted))
	if opt.upper() == "C":
		converted = (temp_num - 32) * (5/9)
		print ("%s F = %s C" %(temp_num, converted))
	
def LeapYear(x):
	#checks if the year is divisable by 4 but not 100 unless divisable by 400
	if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
		return "%s is a Leap Year" %(x)
	return "%s is not a Leap Year" %(x)

def PigLatin(x):
	if len(x) > 0:
		#takes the first letter
		first = x[:1]
		#takes the rest of the word
		rest = x[1:len(x)]
		#puts them together with "ay"  at the end
		return rest + first.lower() + "ay"
	else:
		return ""
def PigLatinTrans(x):
	if len(x) > 0:
		#takes the rest of the word
		part1 = x[:len(x)-3]
		#takes the letter before the "ay"
		part2 = x[len(x)-3:len(x)-2]
	return part2.upper() + part1
	
def HangMan():
	#gives the user an option to use their own word or the codes words
	yn = raw_input("Do you want to use your own word? (y/n): ")
	w_list = ["COMPUTER","PYTHON", "MOUSE", "CHEESE", 'BOOK', 'HANGMAN']
	if yn == 'n': 
		word = w_list[random.randint(0,5)]
	if yn == 'y':
		word = raw_input("What word would you like: ").upper()
		print ("\n" * 29)
	#lives
	livesLeft = 7
	#the list fo dashed lines
	lst = list("_" * len(word))
	
	#the list of guessed letters
	GuessedL = []
	#main game loop
	while livesLeft > 0:
		correct = False
		#prints the lives Left and the letters you guessed
		print (" ".join(lst))
		print ()
		print ("Lives Left: %s" %(livesLeft))
		print ()
		print ("Guessed letters: %s \n" %(" ".join(GuessedL)))
		
		opt = raw_input("Pick a letter: ")
		#checkes to see if user guess letter is in the word and replaces "_" with the correct letter
		for x in range(len(word)):
			if opt.upper() == word[x]:
				lst.pop(x)
				lst.insert(x, opt.upper())
				correct = True
		#if it is incorrect lives -1
		if not correct:
			livesLeft -= 1
			
		GuessedL.append(opt.upper())
		#checkes if you got all the letters
		if "".join(lst) == word:
			print ()
			print (" ".join(lst))
			print ()
			print ("Lives Left: %s" %(livesLeft))
			print ()
			return ("You Win")
			
		print ("\n")
	return "You Lose"
	print ()

def bigger3(x,y,z):
	if x > y and x > z:
		biggest = x
	elif y > x and y > z:
		biggest = y
	elif z > x and z > y:
		biggest = z
	return "%s is the biggest" %(biggest)

def bigger32(x,y,z):
	lst = []
	lst.append(x)
	lst.append(y)
	lst.append(z)
	return max(lst)
	
def sum2(nums):
	if len(nums) > 0:
		nsum = nums[0] + nums[1]
	else:
		nsum = 0
	return nsum

def Clock():
	# give user option to choose a modern clock or analog clock
	x = raw_input("Would you like a (M)odern clock or (A)nalog clock? ")
	#if the user wants a analog clock
	if x.upper() == "A":
		#  I use 100 so that i can cut the 1 so it looks like 00:00.00
		hour = 101
		minute = 100 
		second = 100
		while True:
			#if the second is equal to 160 or just 60 it adds to minute and resets seconds
			if second == 160:
				minute += 1
				second = 100
			# if minute is equal to 160 or 60 it adds to hour and resets minutes
			if minute == 160:
				hour += 1
				minute == 100
			#if hour is 13 then reset back to 1
			if hour == 113:
				hour == 101
			strhour = str(hour)
			strminute = str(minute)
			strsecond = str(second)
			second += 1
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print (strhour[1:len(strhour)] + ":" + strminute[1:len(strminute)] + "." + strsecond[1:len(strsecond)])
			time.sleep(1)
#if the user wants a modern clock
	if x.upper() == "M":
		hour = 1
		minute = 100 
		second = 100
		while True:
			if second == 160:
				minute += 1
				second = 100
			if minute == 160:
				hour += 1
				minute == 100
			if hour == 113:
				hour == 1
			strhour = str(hour)
			strminute = str(minute)
			strsecond = str(second)
			second += 1
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print (strhour + ":" + strminute[1:len(strminute)] + "." + strsecond[1:len(strsecond)])
			time.sleep(1)

def customClock(hour, minute, second):
	minute += 100
	second += 100
	while True:
		if second == 160:
			minute += 1
			second = 100
		if minute == 160:
			hour += 1
			minute = 100
		if hour == 13: 
			hour = 1
		second += 1
		strhour = str(hour)
		strminute = str(minute)
		strsecond = str(second)
		print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
		print (strhour + ":" + strminute[1:len(strminute)] + "." + strsecond[1:len(strsecond)])
		time.sleep(1)

def fibonacci(x):
	lst = [0,1]

	for x in range(1,x+1):
		lst.append(lst[x - 1] + lst[x])
	return lst

def fib(n):
	a, b = 0, 1
	while a < n:
		print (a)
		a, b = b, a+b

class Test(object):
	def __init__(self,name):
		self.name = name
		
	def isGood(self):
		if self.name[-1] == "s":
			print (self.name + " are Good")
		else:
			print (self.name + " is Good")

class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __gt__(self, other):
    for index in range(len(other.cont)+1):
      result = other.cont[:index] + ">" + self.cont
      result += ">" + other.cont[index:]
      print(result)

def RPS():
	rps = [0,1,2]
	RPS = ["Rock", "Scissors", "Paper"]

	Playerpoint = 0

	while Playerpoint < 3:
		x = raw_input('(R)ock, (P)aper or (S)cissors?: ')

		if x.upper() == 'R' or x.upper() == 'ROCK':
			gamepoint = 0

		elif x.upper() == 'S' or x.upper() == 'SCISSORS':
			gamepoint = 1

		elif x.upper() == 'P' or x.upper() == 'PAPER':
			gamepoint = 2

		y = random.randint(0, 2)
		
		print ()

		if y == rps[gamepoint - 1]:
			print ('Com Wins\n')
			print ("Player's Choice: " + RPS[gamepoint])
			print ("Com's Choice: " + RPS[y])
			
		elif y == rps[gamepoint - 2]:
			print ("Player Wins\n")
			print ("Player's Choice: " + RPS[gamepoint])
			print ("Com's Choice: " + RPS[y])
			Playerpoint += 1
			
		elif y == rps[gamepoint]:
			print ("Draw\n")
			print ("Player's Choice: " + RPS[gamepoint])
			print ("Com's Choice: " + RPS[y])
		
		print ("\n")
		
		if Playerpoint == 3:
			return "Player wins"
	return "Player loses"

def RandomGame():
	
	DotBoard = []
	#board dimentions
	dimy = 10
	dimx = 10


	#creates the dots in empty board
	for x in range(0, dimy):
		DotBoard.append(["."] * dimx)

	#prints x and y amounts from 1 to dimention and prints the Dots in a square
	def print_board(board):
		boardx = 1
		boardy = []
		for i in range(1, len(board[0]) + 1):
			boardy.append(str(i))
		
		print ("   ",) 
		print (" ".join(boardy))
		
		for row in board:
			if boardx < 10:
				print (" ", boardx, " ".join(row))  
			else:
				print ("", boardx, " ".join(row))
			boardx += 1
		print ()
		
	#the cords for the start off the player in the center
	n = int(dimy/2) - 1
	m = int(dimx/2) - 1

	#places the Enemy randomly on the grid
	Ey = random.randint(0,len(DotBoard)-1)
	Ex = random.randint(0,len(DotBoard[0])-1)

	#the random move generator
	diceroll = random.randint(1,6)

	#game loop
	while True:
		print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
		#player is repersented by "O" and starts in the center
		DotBoard[n][m] = "O"
		#Enemy is represented by a "X"
		DotBoard[Ey][Ex] = "X"
		#prints board
		print_board(DotBoard)
		#tells player what the number represents
		print ("  ", int(diceroll), "You Can't Have More Moves Than The Dice Roll")
		#movement input from player
		x = int(input("can move positive or negitive from 0 to %s on the x plane: " %(int(diceroll))))
		y = int(input("can move positive or negitive from 0 to %s on the y plane: " %(int(diceroll))))
		print ()
		#tells the Enemy to move towardss the player one place at a time
		if (n-Ey) in range(-(len(DotBoard)-1),0):
			Eypos = random.randint(-1,0)
			
		elif (n-Ey) in range(0,len(DotBoard[0])-1):
			Eypos = random.randint(0,1)
			
		else:
			Eypos = random.randint(-1,1)
			
		if (m-Ex) in range(-(len(DotBoard[0])-1),0):
			Expos = random.randint(-1,0)
			
		elif (m-Ex) in range(0,len(DotBoard[0])-1):
			Expos = random.randint(0,1)
			
		else:
			Eypos = random.randint(-1,1)
		
		#checks if amount of moves are higher than dice roll
		if (x + y) > diceroll:
			print ("you can't do that")
		else:
			if DotBoard[n+y][m+x] == "C":
				print ("You Lose, You ran into your own trail...stupid")
				break
			#leaves a trail of "C" behind player
			for i in range(min(n, n+y),(max(n, n+y))+1):
				for u in range(min(m, m+x),(max(m, m+x))+1):
					DotBoard[i][m+x] = "C"
					DotBoard[n][u] = "C"
			#sets the old position of "X" to "."
			Ey += Eypos
			Ex += Expos
			DotBoard[Ey-Eypos][Ex-Expos] = "."
			#sets the new position of "O"
			n += y
			m += x
			#sets the old position of "O" to "C"
			DotBoard[n-y][m-x] = "C"
			
			#checks if player used less than the total dice roll then subtracts diceroll from total moves 
			if (((x + y)**2)**.5) < diceroll:
				diceroll -= (((x + y)**2)**.5)
			else:
				diceroll = random.randint(1,6)
			
			#Win, Lose condition
			if DotBoard[Ey+Eypos][Ex+Expos] == "C" or DotBoard[n+y][m+x] == "X":
				print ("You Win, The Enemy ether ran into your trail or you got him, idiot.")
				print_board(DotBoard)
				break
			elif DotBoard[Ey+Eypos][Ex+Expos] == "O":
				print ("You Lose, How did he get you its one of the most stupid things one the planet.")
				print_board(DotBoard)
				break

def locker(n):
	lst = []
	
	for i in range(1,n+1):
		lst.append("C")
	y = 1

	for m in range(1,n, y):
		if lst[m] == "C":
			lst[m] = "O"
		elif lst[m] == "O":
			lst[m] = "C"
		print(lst[m])
		y += 1
		
	return lst
	
print (locker(100))