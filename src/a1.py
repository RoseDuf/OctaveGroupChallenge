import time
import requests
import songSearch2
from tkinter import *
from PIL import ImageTk,Image

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
            
        if (count == 2):
            array = line.split(',')
            lyric.startingTime = convertToSeconds(array[0])
             
        if (count == 3):
            lyric.sentence = line
        
        if (count > 3):
            lyric.sentence = lyric.sentence + " " + line
            
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
    
def displayLyrics():
    
    songSearch2.songSearch()
    songName = songSearch2.getSongName()
    
    print(songName)
    parseFile('../lyrics/' + songName + '.txt')
    
    starttime=time.time()

    timeStampFound = False
    index = 0
    targetTime = 0
    
    #create a blank window
    root = Tk()
    root.geometry("900x600") 
    root.configure(background='pink')
   
    theLabel = Label(anchor=CENTER)
    
    def stopPlayer():
        root.destroy()
        a = requests.post("http://localhost:8080/stop?name=theFile.ogg")
    
    theButton = Button (root, text="Stop", command=lambda: stopPlayer(), font='Helvetica 21 bold')
    theButton.pack()
    
    '''
    image2 =Image.open('./image.jpg')
    background_image = PhotoImage(file=image2)
    background_label = Label(image=background_image)
    background_label.pack()
    '''
    
    targetSentence = ""
    
    loop = True
    
    while (loop == True):
        time.sleep(1 - ((time.time() - starttime) % 1))
        if (timeStampFound == False and targetTime != (lyricList[-1].startingTime)):
            targetTime = lyricList[index].startingTime
            timeStampFound = True

        if (int(time.time() - starttime) == targetTime):
            targetSentence = lyricList[index].sentence
            theLabel.pack_forget()
            theLabel = Label(root, text=("\n\n\n\n\n\n" + targetSentence), font='Helvetica 21 bold', fg="blue", bg="pink")
            theLabel.pack()
            index += 1
            timeStampFound = False
            
            
        print(int(time.time() - starttime))
        
        root.update_idletasks()
        root.update()
        
        if (int(time.time() - starttime) == (lyricList[-1].startingTime + 5)):
            loop = False
    
    

        




displayLyrics()