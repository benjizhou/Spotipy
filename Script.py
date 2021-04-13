import CurrentlyPlaying
from datetime import datetime
import os

import xlsxwriter

def run():

    with open("output.txt", "rb") as file:
        file.seek(-2, os.SEEK_END)
        while file.read(1) != b'\n':
            file.seek(-2, os.SEEK_CUR) 
        last = file.readline().decode()

    f = open("output.txt","a")
#Song has to be playing
    current = CurrentlyPlaying.run()
    #current = current.encode('utf-8')
    song = str(datetime.now()) + '    ' + str(current)
    if (current != last[30:]):
        f.write("\n" + song)