import time

#parse lyrics 

class Lyric:
    sentenceNumber = 0
    startingTime = 0
    sndingTime = 0
    sentence = ""

    def printLyricContents():
        print(sentenceNumber)
        print(startingTime)
        print(endingTime)
        print(sentence)

lyricList = []
        
def parseFile(file):

    f = open(file,'r')
    
    count = 0
    
    listIndex = 0
    
    for line in f: 
        
        line = line.strip()
        
        count += 1
            
        if (count == 1):
            lyric = Lyric()
            lyric.sentenceNumber = line
            #print("senetence: ", lyric.sentenceNumber, "\n")
            
        if (count == 2):
            array = line.split(',')
            lyric.startingTime = array[0]
            #lyric.EndingTime = array[1]
            #print("time: ", lyric.startingTime, "\n")
             
        if (count == 3):
            lyric.sentence = line
            #print("line one: ", lyric.Sentence, "\n")
        
        if (count > 3):
            lyric.sentence = lyric.sentence + " " + line
            #print("line two: ", lyric.sentence[listIndex], "\n")
            
        if (line == ''):
            count = 0
            listIndex += 1
            lyricList.append(lyric)
        
def findTimeStamp(time):
    
    #print(lyricList[0].startingTime)
    
    for i,_ in enumerate(lyricList):
        if (lyricList[i].startingTime == time):
            print(lyricList[i].sentence)
            
   
    
parseFile('bj.txt')
findTimeStamp("00:00:34")

