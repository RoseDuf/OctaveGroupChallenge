import requests
import json
#from playsound import playsound

headers = {
    'Authorization': 'f9f6d21375373f9b69a826b6f564bd40',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}

songName = input("Enter a song name: ")
songName = songName.replace(" ", "*")
songName1 = songName.replace("*", "")
print(songName)
params = (
    ('query', songName),)
response = requests.get('https://conuhacks-2020.tsp.cld.touchtunes.com/v1/songs', headers=headers, params=params).json()
try:
    print(response)
    with open(str('theFile') + '.json', 'w') as outfile:
        json.dump(response, outfile)
except:
    print("Doesn't work")

songList = []
songIdList = []
with open('theFile'+'.json') as f:
    data = json.load(f)
for i in range(len(data["songs"])):
    if data["songs"][i]["id"] not in songIdList:
        d = data["songs"][i]["artistName"]
        c = data["songs"][i]["id"]
        print(str(i+1)+ ': ' + d)
        print(c)
        songList.append(data["songs"][i]["artistName"])
        #if data["songs"][i]["id"] not in songIdList:
        songIdList.append(c)

choice = input("Enter the number of your choice: ")
#print(songIdList[2])
choice = int(choice)-1
print(songIdList[int(choice)])
songId = songIdList[choice]
response = requests.get('https://conuhacks-2020.tsp.cld.touchtunes.com/v1/songs/' + str(songId),
                            headers=headers).json()
try:
    print(response)
    with open('theFile'+ 'Id.json', 'w') as outfile:
        json.dump(response, outfile)
except:
        print("Doesn't work")


with open(str('theFile')+ 'Id.json') as f:
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
fileName = url[:url.rindex('.ogg')+4]
fileName = fileName.replace(str(notNeeded), "")
theFile = 'theFile.ogg'
try:
    open(theFile, 'wb').write(myfile.content)
except:
    print("File already exists")