import requests
import json
from player import Player
import api
import requests

r = requests.post("http://localhost:8080/play?name=" + theFile.ogg")