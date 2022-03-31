import random
import time
from datetime import datetime,timedelta

class Num():
    def __init__(self):
        self.mis = 0
        self.numbers=['0','1','2','3','4','5','6','7','8','9']
    def make_num(self):
        now = datetime.now()
        final_time = now + timedelta(minutes=0.1)
        print(now)
        print(final_time)

        while(datetime.now()<final_time):
            time.sleep(0)
            x = random.choice(self.numbers)
            print(x)
            a=input("=> ")
            if a != x:
                self.mis = self.mis+1

class Word():
    def __init__(self):
        self.mis = 0
        self.words =['action','angry', 'certain','rock', 'contempt','arise','head', 'river', 'accurate', 'zone', 'hotdog', 'image', 'victory','deport','digress', 'breathe', 'leak', 'interest', 'cheque','slab','swipe','qualified','bird','accompany','variety','secure','reinforce','leadership','time','pain','sulphur','entertain','dominate','relax','dinner','exact','traction','joke','kid','evening','railroad','draw','mixture','study','exploration','assume','basketball','order','fame','bolt','sacred','stem','accessible','dismissal','aquarium','excitement','planet','rider','reliance','pray','neck','enter','shark','nuance','psychology','cash','variant','theme','talented','coverage','tribe']

    def make_word(self):
        now = datetime.now()
        final_time = now + timedelta(minutes=0.1)
        print(now)
        print(final_time)

        while(datetime.now()<final_time):
            time.sleep(0)
            x = random.choice(self.words)
            print(x)
            a=input("=> ")
            if a != x:
                self.mis = self.mis+1

class Next(Word,Num):
    def next(self):
        print("What will you chose","Numbers and words ?")
        turn=input()
        if turn=='numbers' or turn=="num":
            print("Wait!")
            time.sleep(3)
            n = self.make_num()
        else:
            if turn=='words' or turn=="w":
                print("Wait!")
                time.sleep(3)
                w = self.make_word()

class Start(Next,Word,Num):
    def __init__(self):
        self.mis = 0
        self.words =['action','angry', 'certain','rock', 'contempt','arise','head', 'river', 'accurate', 'zone', 'hotdog', 'image', 'victory','deport','digress', 'breathe', 'leak', 'interest', 'cheque','slab','swipe','qualified','bird','accompany','variety','secure','reinforce','leadership','time','pain','sulphur','entertain','dominate','relax','dinner','exact','traction','joke','kid','evening','railroad','draw','mixture','study','exploration','assume','basketball','order','fame','bolt','sacred','stem','accessible','dismissal','aquarium','excitement','planet','rider','reliance','pray','neck','enter','shark','nuance','psychology','cash','variant','theme','talented','coverage','tribe']
        self.numbers = ['0','1','2','3','4','5','6','7','8','9']
    def start(self):
        print("Do you want to start ?")
        man=input()
        if man=='no':
          print('quit')
        if man=='yes':
          self.next()
start = Start()

print(start.start())
print(f"you have {start.mis} mistakes")