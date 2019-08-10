import obd
import vlc
import time
import random
connection = obd.OBD("/dev/ttyUSB0", 38400) # auto-connects to USB or RF port
song = vlc.MediaPlayer("mix1.mp3")
eurobeat = vlc.MediaPlayer("eurobeat.mp3")
song.play()
running = True
extra = 0


while running:
    cmd = obd.commands.RELATIVE_ACCEL_POS 
    rec_throttle = connection.query(cmd) 
    throttle = rec_throttle.value.magnitude
    print(throttle)
    caseNum = random.randint(1,7)
    if caseNum == 1:
        eurobeat = vlc.MediaPlayer("eurobeat.mp3")
    elif caseNum == 2:
        eurobeat = vlc.MediaPlayer("eurobeat2.mp3")
    elif caseNum == 3:
        eurobeat = vlc.MediaPlayer("eurobeat3.mp3")
    elif caseNum == 4:
        eurobeat = vlc.MediaPlayer("eurobeat4.mp3")
    elif caseNum == 5:
        eurobeat = vlc.MediaPlayer("eurobeat5.mp3")
    elif caseNum == 6:
        eurobeat = vlc.MediaPlayer("eurobeat6.mp3")
    elif caseNum == 7:
        eurobeat = vlc.MediaPlayer("eurobeat7.mp3")
   

    while throttle >= 40:
        extra = extra + 1
        song.set_pause(1)

        if (eurobeat.is_playing()) == 0:
            print("[EUROBEAT INTENSIFIES]")
            eurobeat.play()
        if extra > 2:
            time.sleep(3)
        time.sleep(3)
        rec_throttle = connection.query(cmd) 
        throttle = rec_throttle.value.magnitude

    if throttle < 40:
        song.set_pause(0)
        eurobeat.stop()
    eurobeat.stop()

