# File Input/Output in Python

import os

def getDesktopPath(filename = ""):
    # next line is odd, but works in Windows/Mac/Linux
    homepath = os.getenv('USERPROFILE') or os.getenv('HOME')
    return homepath + os.sep + "Desktop" + os.sep + filename

def fileExists(filename):
    return os.path.exists(filename)
    
def deleteFile(filename):
    if (fileExists(filename) == True):
        os.remove(filename)

def readTextFile(filename):
    if (fileExists(filename) == False):
        print "File does not exist:", filename
        return None
    fileHandler = open(filename, "rt")
    text = fileHandler.read()
    fileHandler.close()
    return text

def readTextFileAsList(filename):
    # readlines includes '\n' characters, so we'll use split() instead
    text = readTextFile(filename)
    if (text == None):
        return None
    return text.split(" ") #note, this turns the textFile into a 2d List

def writeTextFile(text, filename):
    fileHandler = open(filename, "wt")
    fileHandler.write(text)
    fileHandler.close()

#writeTextFile(readTextFile("Dictionary/twoLetter.txt"), "Dictionary/Blarg.txt")

def isAWord(word): #returns True is word is in Dictionary, otherwise, false   
    word = word.upper()
    return (word in readTextFileAsList("Dictionary/twoLetterWords.txt") or
            word in readTextFileAsList("Dictionary/threeLetterWords.txt") or
            word in readTextFileAsList("Dictionary/fourLetterWords.txt") or
            word in readTextFileAsList("Dictionary/fiveLetterWords.txt") or
            word in readTextFileAsList("Dictionary/sixLetterWords.txt") or
            word in readTextFileAsList("Dictionary/sevenLetterWords.txt") or
            word in readTextFileAsList("Dictionary/eightLetterWords.txt") or
            word in readTextFileAsList("Dictionary/nineLetterWords.txt") or
            word in readTextFileAsList("Dictionary/tenLetterWords.txt") or
            word in readTextFileAsList("Dictionary/elevenLetterWords.txt") or
            word in readTextFileAsList("Dictionary/twelveLetterWords.txt") or
            word in readTextFileAsList("Dictionary/thirteenLetterWords.txt") or
            word in readTextFileAsList("Dictionary/fourteenLetterWords.txt") or
            word in readTextFileAsList("Dictionary/fifteenPlusLetterWords.txt")) 
    

