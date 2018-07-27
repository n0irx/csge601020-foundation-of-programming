#This is program to make a word cloud from a file input by user and create html
import string 																	# import string to use function method
print("Program to create word cloud from a text file\n\
	The result is stored as an HTML file\n")
#------------------------getting input from user-------------------------------#
fileName = input("Please enter file name: ")
print("")  								 										# getting file name
wordList = open(fileName, 'r').read().lower().split()							# read and split item from .txt file to be put in list
stopList = open('stopWords.txt', 'r').read().split()							# read and put the stopwords to a list
wordListRemoved, countedVal, wrdCheck, valCheck = [], [], [], [] 				# initialize list which will be used
#----------------------append wanted item to the list-------------------------#
for item in wordList: 															# looping for append item to list
	item = item.strip(string.punctuation) 										# strip punctuatuion
	if item not in stopList and item != '': 									# strip item that exist in stopWords and isn't a blank string
		wordListRemoved.append(item)											# list which doesn't contains any punctuations and stopwords
for item in wordListRemoved: 													# loop, for counting value of words
	if item not in wrdCheck: 													# checking wheter the item's already in check list or not
		wrdCheck.append(item) 													# check list(item that we have been already counted)
		valCheck = wordListRemoved.count(item)									# count 'item'
		countedVal.append([valCheck, item])										# append list to the list[howmuchwords, whatword]
#---------------start sorting based on how much the words counted--------------#
countedVal.sort(reverse = True)													# sort and reverse based on val
countedVal = countedVal[:50] 													# getting 50 higher val of item
print(fileName, ':\n', len(countedVal), 'words in frequency\
		order as count:word pairs\n')											# print this for shell
maxVal = countedVal[0][0]														# set max val of list to maxVal
minVal = countedVal[-1][0]														# set min val of list to minVal
#-----------------------------print item to shell------------------------------#
for i in range(len(countedVal)): 												# loop for printing based on val
	if (i+1) % 4 !=0:
		print('{:5d}:{:15s}'.format(countedVal[i][0],countedVal[i][1]),end='')	# sort and format for printing in shell
	else:
		print('{:5d}:{:15s}'.format(countedVal[i][0],countedVal[i][1]))			# sort and format for printing in shell

for i in range(len(countedVal)):
	countedVal[i] = countedVal[i][::-1]											# reverse list in list index
countedVal.sort()
titleName = 'A Word Cloud of ' + fileName
#--below this line, there are html functions, that copied from htmlFunction.py--#
import random

# Functions adapted from ProgrammingHistorian
# http://niche.uwo.ca/programming-historian/index.php/Tag_clouds

def make_HTML_word(word,cnt,high,low):
    '''
    Make a word with a font size and a random color.
    Font size is scaled between htmlBig and htmlLittle (to be user set).
    high and low represent the high and low counts in the document.
    cnt is the count of the word.
    Required -- word (string) to be formatted
             -- cnt (int) count of occurrences of word
             -- high (int) highest word count in the document
             -- low (int) lowest word count in the document
    Return -- a string formatted for HTML that is scaled with respect to cnt
    '''
    htmlBig = 96
    htmlLittle = 14
    if high != low:
        ratio = (cnt-low)/float(high-low)
    else:
        ratio = 0
    fontsize = htmlBig*ratio + (1-ratio)*htmlLittle
    fontsize = int(fontsize)
    rgb = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    word_str = '<span style=\"color: rgb{}; font-size:{:s}px;\">{:s}</span>'
    return word_str.format(rgb,str(fontsize), word)

def make_HTML_box(body):
    '''
    Take one long string of words and put them in an HTML box.
    If desired, width, background color & border can be changed in the function
    This function stuffs the "body" string into the the HTML formatting string.

    Required -- body (string), a string of words
    Return -- a string that specifies an HTML box containing the body
    '''
    box_str = """<div style=\"
    width: 560px;
    background-color: rgb(250,250,250);
    border: 1px grey solid;
    text-align: center\" >{:s}</div>
    """
    return box_str.format(body)

def print_HTML_file(body,title):
    '''
    Create a standard html page (file) with titles, header etc.
    and add the body (an html box) to that page. File created is title+'.html'
    Required -- body (string), a string that specifies an HTML box
    Return -- nothing
    '''
    fd = open(title+'.html','w')
    the_str="""
    <html> <head>
    <title>"""+title+"""</title>
    </head>

    <body>
    <h1>"""+'A Word cloud of '+title+'</h1>'+'\n'+body+'\n'+"""<hr>
    </body> </html>
    """
    fd.write(the_str)
    fd.close()

#----make html file based on file that we have typed in the first program------#

pairs = countedVal																# assign our final last list to var pairs
high_count = maxVal																# assign maxVal for high_count needs
low_count = minVal																# assign minVal for low_count needs
body = ''
for word,cnt in pairs:
    body = body + " " + make_HTML_word(word, cnt, high_count, low_count)
box = make_HTML_box(body)  # creates HTML in a box
print_HTML_file(box, fileName)  # writes HTML to file name 'testFile.html'
exit = input("\n\nPlease type Enter to continue ...")							# prompt keyboard input to exit
