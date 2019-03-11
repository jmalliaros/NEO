from liblo import *
from aiy.board import Board, Led
from aiy.voice import tts
import sys
import time
from time import sleep

def avgValue(a,b):
    avg = (a + b )/2.0
    return avg 

class MuseServer(ServerThread):
    #listen for messages on port 5000

    def __init__(self):
        ServerThread.__init__(self, 5000)
        self.board = Board()
        self.haslooped = False
        self.avgmax = 0
        self.count = 0

    #receive accelrometer data
    @make_method('/muse/acc', 'fff')
    def acc_callback(self, path, args):
        acc_x, acc_y, acc_z = args
        # print "%s %f %f %f" % (path, acc_x, acc_y, acc_z)

    #receive EEG data
    @make_method('/muse/eeg', 'ffff')
    def eeg_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        # print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)

    #handle unexpected messages
    @make_method(None, None)
    def fallback(self, path, args, types, src):
        if (self.haslooped == False):
            tts.say("Hello there I am your neuro assistant named Neo.")
            tts.say("Let's improve your concentration, please get ready with your muse headset. Now concentrate and try to slow the light pulse by calming your mind")
            self.haslooped = True

        l_ear, l_forehead, r_forehead, r_ear = args
        l_ear_f = float(l_ear)
        l_forehead_f = float(l_forehead)
        r_forehead_f = float(r_forehead)
        r_ear_f = float(r_ear)

        if ('beta_absolute' in path):
            if(self.count >= 300):
                tts.say("Thank you ! Your maximum concentration level was " +  str(int(self.avgmax * 100)))
                return
            print(path)
            print((l_ear_f + l_forehead_f + r_forehead_f + r_ear_f)/4)
            avgf = (l_ear_f + l_forehead_f + r_forehead_f + r_ear_f)/4 #avgValue(l_forehead_f, r_forehead_f) #l_ear_f, r_ear_f
            avgp = max(0,avgf)
            print(avgp)
        
            if (avgp > self.avgmax):
                self.avgmax = avgp
            
            self.board.led.state = Led.ON
            sleep(avgp*avgp)
            self.board.led.state = Led.OFF
            sleep(avgp*avgp)
            print(self.count)
            self.count +=1

try:
    server = MuseServer()
except ServerError as err:
    print(str(err))
    sys.exit()

server.start()

if __name__ == "__main__":
    while 1:
        time.sleep(1)
