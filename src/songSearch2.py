import requests
import json
from player import Player
import api
import soundfile as sf    # Use this package
import sounddevice as sd  # and this one
# from playsound import playsound

class Song:
    def __init__(self, name):
        self.name = name

    def setSongName(self, b):
        self.name = b

    def getSongName(self):
        return self.name


def songSearch(song):
    headers = {
        'Authorization': 'f9f6d21375373f9b69a826b6f564bd40',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    songName = input("Enter a song name: ")
    songName = songName.replace(" ", "*")
    songName1 = songName.replace("*", "")

    thesong = song.setSongName(songName1)
    # thesong.name = str(songName1)

    print(songName1)

    params = (
        ('query', songName),)
    response = requests.get('https://conuhacks-2020.tsp.cld.touchtunes.com/v1/songs', headers=headers,
                            params=params).json()
    try:
        print(response)
        with open(str('theFile') + '.json', 'w') as outfile:
            json.dump(response, outfile)
    except:
        print("Doesn't work")

    songList = []
    songIdList = []
    with open('theFile' + '.json') as f:
        data = json.load(f)
    for i in range(len(data["songs"])):
        if data["songs"][i]["id"] not in songIdList:
            d = data["songs"][i]["artistName"]
            c = data["songs"][i]["id"]
            print(str(i + 1) + ': ' + d)
            print(c)
            songList.append(data["songs"][i]["artistName"])
            # if data["songs"][i]["id"] not in songIdList:
            songIdList.append(c)

    choice = input("Enter the number of your choice: ")
    # print(songIdList[2])
    choice = int(choice) - 1
    print(songIdList[int(choice)])
    songId = songIdList[choice]
    response = requests.get('https://conuhacks-2020.tsp.cld.touchtunes.com/v1/songs/' + str(songId),
                            headers=headers).json()
    try:
        print(response)
        with open('theFile' + 'Id.json', 'w') as outfile:
            json.dump(response, outfile)
    except:
        print("Doesn't work")

    with open(str('theFile') + 'Id.json') as f:
        data = json.load(f)

        print(data["artist"]["name"])
        print(data["id"])
        print(data["title"])
        print(data["album"]["title"])

    url = str(data["playUrl"])
    print(url)
    r = requests.get(url)

    notNeeded = 'https://cdn.apps.playnetwork.com/master/'
    myfile = requests.get(url)
    # fileName = fileName.replace(str(notNeeded), "")
    theFile = 'theFile.ogg'
    path = '../music/'

    open((path + theFile), 'wb').write(myfile.content)
    # try:
    #    open(theFile, 'wb').write(myfile.content)
    # except:
    #    print("KHAAAAN!!!")
    print("Do you want the song with:"+'\n'
            "1. Lyrics" + '\n'
            "2. Fast" + '\n')
    print("Enter your selection: ")
    z = str(input())
    if (z == '1'):
        print('path1')
        a = requests.post("http://localhost:8080/play?name=theFile.ogg")
    elif (z == '2'):
        print('path2')
        kiss, samplerate = sf.read("../music/theFile.ogg")  # load Kiss.aiff into kiss variable

        sd.play(kiss, samplerate * 1.3)  # start playing the music

        sd.wait()
    
