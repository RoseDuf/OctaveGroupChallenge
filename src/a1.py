import time

#parse lyrics 

class Lyric:
    sentenceNumber = 0
    startingTime = 0
    sndingTime = 0
    sentence = ""

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
            lyric.startingTime = convertToSeconds(array[0])
            
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
            
            
def convertToSeconds(time):
    seconds = 0
    seconds += int(time[6:8])
    seconds += int(time[3:5])*60
    seconds += int(time[0:2])*3600
    
    #print(seconds)
    
    return seconds
        
def findTimeStamp(time):
    
    #print(lyricList[0].startingTime)
    newTime = convertToSeconds(time)
    
    for i,_ in enumerate(lyricList):
        if (lyricList[i].startingTime == newTime):
            print(lyricList[i].sentence)

def displayLyricsTimer():
    
    parseFile('bj.txt')
    
    starttime=time.time()

    timeStampFound = False
    index = 0
    targetTime = 0

    while True:
        time.sleep(1 - ((time.time() - starttime) % 1))
        if (timeStampFound == False):
            targetTime = lyricList[index].startingTime
            timeStampFound = True

        if (int(time.time() - starttime) == targetTime):
            print(lyricList[index].sentence)
            index += 1
            timeStampFound = False

        print(int(time.time() - starttime))
        
displayLyricsTimer()
