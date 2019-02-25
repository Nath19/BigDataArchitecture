import time 
import os 


from interruptingcow import timeout

try:
    with timeout(10, exception=RuntimeError):
        os.system('python tweepy_streamer.py')
        pass
except RuntimeError:
    print("didn't finish within 10 seconds")

