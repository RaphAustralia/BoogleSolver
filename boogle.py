import sys, string, random, Queue
#####INIT METHODS####

class letterOnBoard:
    nextTo = []
    def __init__(self,val):
        self.val=val
    def __repr__(self):
    	return self.val

def buildWordDict():
	f = open('/usr/share/dict/web2','r')
	words = {}
	for word in f:
		words[word.replace('\n','')] = "word"
	return words

def buildBoard(size):
	board = []
	for x in xrange(0,size):
		board.append([])
		for y in xrange(0,size):
			rndChar = random.choice(string.ascii_lowercase)
			board[x].append(letterOnBoard(rndChar))
	return board

def buildLink(board):
    size = len(board[0])
    for x in xrange(0,size):
        for y in xrange(0,size):
            #get right neighbour +1 to x
            #get left neightbour: -1 to x
            #get top neighbour: -1 to y
            #get bottom neighbour: +1 to y
            rightNeighbour = x +1
            leftNeighbour = x -1
            topNeighbour = y - 1
            bottomNeighbour = y + 1
            board[x][y].nextTo = []
            if rightNeighbour <= (size-1):
                board[x][y].nextTo.append(board[rightNeighbour][y])

            if leftNeighbour >= 0:
                board[x][y].nextTo.append(board[leftNeighbour][y])

            if topNeighbour >= 0:
                board[x][y].nextTo.append(board[x][topNeighbour])

            if bottomNeighbour <=(size-1):
                board[x][y].nextTo.append(board[x][bottomNeighbour])
#####INIT METHODS####

def search(curr,end,path=[],paths=[]):
	if curr is end:
		paths.append(path)
	for adjacent in curr.nextTo:
		if adjacent not in path:
			search(adjacent,end,path+[adjacent],paths)
                
board = buildBoard(4)
buildLink(board)
words = buildWordDict()


[sys.stdout.write(str(row) +'\n') for row in board]#just printing the board


listOfLetters = [letter for row in board for letter in row]

for startLetter in listOfLetters:
	for endLetter in listOfLetters:
		paths = []
		search(startLetter,endLetter,[startLetter],paths)
		for path in paths:
			word = ""
			for letter in path:
				word += letter.val
			lengthOfWord = len(word)
			if lengthOfWord >=3 and word in words:
				print word
				wordReversed = word[::-1]
				if wordReversed in words:
					print wordReversed

	listOfLetters.remove(startLetter)


print    
print 'word find finished!'
