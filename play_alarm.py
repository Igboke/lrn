from playsound import playsound
import time
CLEAR= '\033[2J'
RESTART = '\033[H'

def user_input():
    minutes = int(input('enter the minutes: '))
    seconds = int(input('enter the seconds: '))
    total_time = minutes * 60 + seconds
    return total_time,minutes,seconds

def play_alarm():
    total_time,minutes,seconds=user_input()
    time_to_alarm = 0
    sec_to_alarm = 0
    min_to_alarm = 0
    print(f'Alarm to be sounded in {total_time} seconds')
    print(f'{minutes:02d}:{seconds:02d}')
    print(CLEAR)
    while total_time > time_to_alarm:
        time.sleep(1)
        time_to_alarm +=1
        sec_to_alarm+=1
        if sec_to_alarm % 60 == 0:
            min_to_alarm += 1
            sec_to_alarm = 0 
        print(f'{RESTART}{min_to_alarm:02d}:{sec_to_alarm:02d}')

    playsound('C:\\Users\\Lenovo\\Documents\\scripts\\alarm.mp3')    

play_alarm()