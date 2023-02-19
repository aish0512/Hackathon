import time
from datetime import datetime
from gtts import gTTS

def convert_24(time_string):
    if ":" in time_string:
        hour, minute_period = time_string.split(':')
        minute, period = minute_period[:-2], minute_period[-2:]

        hour = int(hour)
        minute = int(minute)
        
        if period == 'AM' and hour == 12 and minute == 0:
            return "zero"
        
        if period == 'PM' and hour != 12 and minute != 0:
            hour += 12
        
            return str(hour) + " "+str(minute)
        
        if period == 'AM' and hour != 12 and minute != 0:
            hour = hour
        
            return str(hour) + " "+str(minute)
        
        if minute == 0 and period == "AM":
            return str(hour) + " hundred hours"
        if minute == 0 and period == "PM":
            return str(hour + 12) + " hundred hours"
    else:
        num_digits = 0

        for char in time_string:
            if char.isdigit():
                num_digits += 1
        if num_digits == 1:
            hour = int(time_string[:1])
            period = time_string[1:]
        else:
            hour = int(time_string[:2])
            period = time_string[2:]

        if period == "AM" and hour ==12:
            return "zero"
        elif period =="AM":
            return hour

        elif period == "PM":
            return datetime.strptime(time_string, '%I%p').strftime('%H')

userInput = input('Enter a time in the format HH:MM AM/PM\n')
time = convert_24(userInput)
tts = gTTS(text=time, slow=False)
tts.save("Military2.mp3")

