from datetime import datetime


def greetings_bytime():
    
    current_time=datetime.now()
    curretnt_hour=current_time.hour
    if(5<curretnt_hour<12):
        print("good morning")
    elif(12<curretnt_hour<18):
        print("good afternoon")
    else:
        print("good evening")        

greetings_bytime()