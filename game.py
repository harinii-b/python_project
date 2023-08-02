import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.ttk import *
import random 
import string
import time
import math
from datetime import date
from tkinter import Toplevel, Button, Tk, Menu,messagebox 
 
 
IMAGE_PATH = 'C:/Users/CHANDANA/OneDrive/Desktop/PythonProject/escaperoom1.jpg' #change file path accordingly
WIDTH, HEIGHT = 2000, 2000
 
root = Tk()
root.title("GAME-The Escape Room")
root.state('zoomed')
width1= root.winfo_screenwidth()
height1= root.winfo_screenheight()
 
canvas1 = tk.Canvas(root, width=width1, height=height1)
canvas1.pack()
 
img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((1270, 750), Image.ANTIALIAS))
canvas1.background = img  # Keep a reference in case this code is put in a function.
bg = canvas1.create_image(0, 0, anchor=tk.NW, image=img)
 
def startBTN():
    
    startBTN.counter+=1
    gameWin = Toplevel(root)
    gameWin.title("The Game")
    gameWin.state('zoomed')
    titles_font= ("Century Schoolbook",10,"bold", "underline")
    normal_font = ("Lucida Fax",8)
    hint_font = ("Lucida Fax",8,"bold")
    voice_font=("Lucida Calligraphy",8)
    certificate_font = ("Comic Sans MS", 20, "bold")
    s0 = ttk.Style()
    s0.configure("TLabel", background='light cyan')
    s0.configure("TLabelframe",background='light cyan')
    
    def intro():
        intro_LBL1=ttk.Label(terminalFrame1, text="\"I need to make friends ASAP\" you whisper to yourself while tidying your clothes in your dorm. " *1, wraplengt=1000)
        intro_LBL1.configure(font=normal_font)
        intro_LBL1.place(x=10, y=40)
        intro_LBL2=ttk.Label(terminalFrame1, text="It's your first time away from home as you've moved in to a new city to pursue college. It's just the third day at college and you being the introvert that you are haven't made friends yet." * 1, wraplengt=1000,)
        intro_LBL2.configure(font=normal_font)
        intro_LBL2.place(x=10, y=70)
        intro_LBL3=ttk.Label(terminalFrame1, text="You badly want to explore the city but are missing the quintessential friends gang. Tired of the boredom you have surrounded yourself with, you lay on your bed and start to daydream. As you are laying on the bed and scrolling through instagram, a random post about a new escape room in the city pops up in your feed." * 1, wraplengt=1000)
        intro_LBL3.configure(font=normal_font)
        intro_LBL3.place(x=10, y=115)
        intro_LBL4=ttk.Label(terminalFrame1, text="After deliberating for about 20 minutes in your mind, you finally decide to signup for a solo escape room adventure to kill the boredom blues." * 1, wraplengt=1000)
        intro_LBL4.configure(font=normal_font)
        intro_LBL4.place(x=10, y=155)
        intro_LBL5=ttk.Label(terminalFrame1, text="POV: You have arrived at the escape room facility and are asked to fill up a basic form as follows:    " * 1, wraplengt=1000)
        intro_LBL5.configure(font=normal_font)
        intro_LBL5.place(x=10, y=185)

    def confirm():
        global Name
        Name= nameENT.get()
        Gender= genderENT.get()
        Age= ageENT.get()
        msg=ttk.Label(terminalFrame1, text=f'You have successfully submitted your details {Name} , thank you!')
        msg.configure(font = voice_font)
        msg.place(x=10, y=450)

    def rules():
        global r1, r2, r3
        r1=ttk.Label(terminalFrame1, text="1. Always click on the \'Attempt to solve\' button whenever you want to try keying in the answer or code asked." *1, wraplengt=800)
        r1.configure(font=hint_font)
        r1.place(x=10, y=560)
        r2=ttk.Label(terminalFrame1, text="2. There are 3 chances available in each room to guess the correct answer or code. Once the 3 chances are exhausted, the room will terminate automatically." *1, wraplengt=800)
        r2.configure(font=hint_font)
        r2.place(x=10, y=590)
        r3=ttk.Label(terminalFrame1, text="3. Be mindful to click on the next button within 10 seconds of guessing the right answer or code. On failing to do so, you may have to restart the game again." *1, wraplengt=800)
        r3.configure(font=hint_font)
        r3.place(x=10, y=620)
 
    def detailsEntry():     
        name = ttk.Label(terminalFrame1, text="NAME",width=20,font=("bold", 10))
        name.configure(font=titles_font)
        name.place(x=50,y=230)
        global nameENT
        nameENT = Entry(terminalFrame1)
        nameENT.place(x=150,y=230)
        gender = ttk.Label(terminalFrame1, text="GENDER",width=20,font=("bold", 10))
        gender.configure(font=titles_font)
        gender.place(x=50,y=280)
        global genderENT
        genderENT = Entry(terminalFrame1)
        genderENT.place(x=150,y=280)
        age = ttk.Label(terminalFrame1, text="AGE:",width=20,font=("bold", 10))
        age.configure(font=titles_font)
        age.place(x=50,y=330)
        global ageENT
        ageENT = Entry(terminalFrame1)
        ageENT.place(x=150,y=330)
        submitBTN = Button(terminalFrame1,text = 'SUBMIT', command=confirm)
        submitBTN.place(x=50,y=400)
        rulesBTN = Button(terminalFrame1, text= 'RULES', command=rules)
        rulesBTN.place(x=150, y=400)
        playBTN = Button(terminalFrame1,text = 'PLAY', command=room1)  
        playBTN.after(8000, lambda:playBTN.place(x=250,y=400))
    
    def room1():
        room1Win=Toplevel(gameWin)
        room1Win.title("GAME-The Escape Room")
        room1Win.state('zoomed')
        width1= room1Win.winfo_screenwidth()
        height1= room1Win.winfo_screenheight()

        room1Win.columnconfigure(0,weight=1)
        room1Win.columnconfigure(1,weight=1)    
        room1Win.rowconfigure(0, weight=4) 
        room1Win.rowconfigure(1, weight=4) # change weight to 4
        room1Win.rowconfigure(2, weight=4)

        titles_font= ("Century Schoolbook",10,"bold", "underline")
        normal_font = ("Lucida Fax",8)
        hint_font = ("Lucida Fax",8,"bold")
        voice_font=("Lucida Calligraphy",8)

        terminalFrame = LabelFrame(room1Win, height=750, width=800)
        terminalFrame.grid(row=0,column=0, rowspan=3,sticky='WENS')
        terminalFrame.grid_propagate(False)
        terminalLabel=Label(terminalFrame, text="                                                                                                                           ROOM 1                                                                                                                    ")
        terminalLabel.configure(font= titles_font)
        terminalLabel.pack()

        chancesFrame = LabelFrame(room1Win)
        chancesFrame.grid(row=2,column=1,sticky='WENS')
        chancesLabel=Label(chancesFrame, text="              CHANCES LEFT             ")
        chancesLabel.configure(font= titles_font)
        chancesLabel.pack()

        timerFrame = LabelFrame(room1Win)
        timerFrame.grid(row=0,column=1,sticky='WENS')
        timerLabel=Label(timerFrame, text="                                                 TIMER                                                   ")
        timerLabel.configure(font= titles_font)
        timerLabel.pack()
        
        minute=StringVar()
        second=StringVar()
  
        minute.set("10")
        second.set("00")
        
        mins_box = Entry(
	        timerFrame, 
	        width=3, 
	        font=("Arial",20),
	        textvariable=minute)
        mins_box.place(x=150,y=20)
  
        sec_box = Entry(
	        timerFrame, 
	        width=3,
	        font=("Arial",20),
	        textvariable=second)
        sec_box.place(x=250,y=20)
  
        def countdowntimer():
    
            default= int(minute.get())*60 + int(second.get())

            while default>-1:
         
                mins,secs = divmod(default,60)
                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))
  
                timerFrame.update()
                time.sleep(1)
            
                if (default== 0):
                    L1=Label(timerFrame, text="Time-up!! The room is closing in a second").place(x=100, y=100)
                    L2=Label(timerFrame, text="dummy")
                    L2.after(1500, lambda:room1Win.destroy())
         
                default-= 1

        l0=Label(timerFrame, text="STARTS")
        l0.after(100, lambda:countdowntimer())
        

        buttonsFrame = LabelFrame(room1Win)
        buttonsFrame.grid(row=1,column=1,sticky='WENS')
        buttonsLabel=Label(buttonsFrame, text="                        BUTTONS                  ")
        buttonsLabel.configure(font= titles_font)
        buttonsLabel.pack()
        rightBTN = Button(buttonsFrame, text="Right")
        rightBTN.place(x=280, y=30)
        leftBTN= Button(buttonsFrame, text="Left")
        leftBTN.place(x=130, y=30)
        okBTN=Button(buttonsFrame, text="Ok")
        okBTN.place(x=290, y=90)
        attemptBTN=Button(buttonsFrame, text="Attempt to solve")
        attemptBTN.place(x=100, y=90) 
        hintBTN=Button(buttonsFrame, text="Hint")
        hintBTN.place(x=130, y=150)     
        nextBTN=Button(buttonsFrame, text="Next")
        nextBTN.place(x=280, y=150)

        def rightside_room1(event):
            rightside1=Label(terminalFrame, text="There is a pile of history books, definitely not of much use to you :|"*1, wraplengt=800)
            rightside1.configure(font = normal_font)
            rightside1.place(x=10, y=450)     

        def leftside_room1(event):
            leftside1=Label(terminalFrame, text="There is a numeric keypad wherein you can enter a four-digit code"*1, wraplengt=800)
            leftside1.configure(font = normal_font)
            leftside1.place(x=10, y=480)

        
        def attempt_room1(event):
            attempt_room1.counter+=1
            l1=Label(terminalFrame, text="So, what do you think the code is after analyzing the room's atmosphere?"*1, wraplengt=800)
            l1.configure(font = normal_font)
            l1.place(x=10,y=510)           
            l2=Label(chancesFrame, text="                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       "*1, wraplengt=380)
            l2.place(x=10,y=30)
            l3=Label(chancesFrame, text="                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       "*1, wraplengt=380)
            l2.place(x=10,y=40)

            def hint_room1(event):
                l3=Label(terminalFrame, text="HINT: A major event in India's history")
                l3.configure(font = hint_font)
                l3.place(x=10,y=650)

            def checkans(event):
                
                    code = attempt1.get()
                    if code=='1947':
                        l4=Label(terminalFrame, text="Yay!! You cracked this! The door has opened for you to enter the next room. Click on the next button to move to room 2 "*1, wraplengt=800) 
                        l4.configure(font = normal_font)
                        l4.place(x=50, y=570)
                        global minleft1, secleft1 
                        minleft1=9-int(minute.get())
                        secleft1=59-int(second.get())
                
                        nextBTN.bind('<Button-1>', room2)
                        finalcall=Label(terminalFrame, text="You've got 10 seconds before this room closes. Therefore hurry up and click on the next button to move to the next room, lest you are out of the game."*1, wraplengt=800)
                        finalcall.configure(font = normal_font)
                        finalcall.after(1000, lambda:finalcall.place(x=10, y=600))
                        room1Win.after(15000,lambda:room1Win.destroy())                                    
                    elif code!='1947':
                        if attempt_room1.counter==1:
                            l5=Label(chancesFrame, text="Wrong answer! You've got two more chances before this room closes."*1, wraplengt=380)
                            l5.configure(font = normal_font)
                            l5.place(x=10, y=30)
                        if attempt_room1.counter==2:
                            l6=Label(chancesFrame, text="Wrong answer! You've got one more chance before this room closes."*1, wraplengt=380)
                            l6.configure(font = normal_font)
                            l6.place(x=10, y=30)
                        if attempt_room1.counter==3:
                            l7=Label(chancesFrame, text="Wrong answer! You've exhausted all your 3 chances....bye-bye!!                                                                                      "*1, wraplengt=380)
                            l7.configure(font = normal_font)
                            l7.place(x=10, y=30)
                            room1Win.after(3000,lambda:room1Win.destroy())                    


            attempt1=Entry(terminalFrame)
            attempt1.place(x=10, y=540)
            attempt1.focus_set()

            okBTN.bind('<Button-1>', checkans)
            hintBTN.bind('<Button-1>', hint_room1)

        
        about1=Label(terminalFrame, text="You look around and see various maps of India plastered on all four walls. On the ceiling, there is a picture of doves escaping a cage. The lighting of the room keeps fluctuating between orange, white and green. The room is pretty empty except for these details. To your left there is a door that has the wording \"COME TO ME\"    "  *1, wraplengt=800)
        about1.configure(font = normal_font)
        about1.after(1000, lambda:about1.place(x=10, y=30))
        global IMG
        IMG=ImageTk.PhotoImage(Image.open("C:/Users/CHANDANA/OneDrive/Desktop/PythonProject/text_based_game/doves_room1.jpg")) #change file path accordingly
        doves_img=Label(terminalFrame,image=IMG)
        doves_img.after(2000, lambda:doves_img.place(x=10,y=90))
        
        rightBTN.bind('<Button-1>', rightside_room1)
        leftBTN.bind('<Button-1>', leftside_room1) 
        attempt_room1.counter=0
        attemptBTN.bind('<Button-1>', attempt_room1)

        room1Win.mainloop()
    
    def room2(event):
        room2Win=Toplevel(gameWin)
        room2Win.title("GAME-The Escape Room")
        room2Win.state('zoomed')
        width1= room2Win.winfo_screenwidth()
        height1= room2Win.winfo_screenheight()

        room2Win.columnconfigure(0,weight=1)
        room2Win.columnconfigure(1,weight=1)    
        room2Win.rowconfigure(0, weight=4) 
        room2Win.rowconfigure(1, weight=4) # change weight to 4
        room2Win.rowconfigure(2, weight=4)

        """ s2 = ttk.Style()
        s2.configure("TLabel", background='goldenrod1')
        s2.configure("TLabelframe",background='goldenrod1') """

        titles_font= ("Century Schoolbook",10,"bold", "underline")
        normal_font = ("Lucida Fax",8)
        hint_font = ("Lucida Fax",8,"bold")
        voice_font=("Lucida Calligraphy",8)

        terminalFrame = LabelFrame(room2Win, height=750, width=800)
        terminalFrame.grid(row=0,column=0, rowspan=3,sticky='WENS')
        terminalFrame.grid_propagate(False)
        terminalLabel=Label(terminalFrame, text="                                                                                                                           ROOM 2                                                                                                                   ")
        terminalLabel.configure(font= titles_font)
        terminalLabel.pack()
        
        chancesFrame = LabelFrame(room2Win)
        chancesFrame.grid(row=2,column=1,sticky='WENS')
        chancesLabel=Label(chancesFrame, text="              CHANCES LEFT             ")
        chancesLabel.configure(font= titles_font)
        chancesLabel.pack()

        timerFrame = LabelFrame(room2Win)
        timerFrame.grid(row=0,column=1,sticky='WENS')
        timerLabel=Label(timerFrame, text="                                                 TIMER                                                   ")
        timerLabel.configure(font= titles_font)
        timerLabel.pack()        
        
        minute=StringVar()
        second=StringVar()
  
        minute.set("10")
        second.set("00")
        
        mins_box = Entry(
	        timerFrame, 
	        width=3, 
	        font=("Arial",20),
	        textvariable=minute)
        mins_box.place(x=150,y=20)
  
        sec_box = Entry(
	        timerFrame, 
	        width=3,
	        font=("Arial",20),
	        textvariable=second)
        sec_box.place(x=250,y=20)
  
        def countdowntimer():
    
            default= int(minute.get())*60 + int(second.get())

            while default>-1:
         
                mins,secs = divmod(default,60)
                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))
  
                timerFrame.update()
                time.sleep(1)
            
                if (default== 0):
                    L1=Label(timerFrame, text="Time-up!! The room is closing in a second").place(x=100, y=100)
                    L2=Label(timerFrame, text="dummy")
                    L2.after(1500, lambda:room2Win.destroy())
         
                default-= 1

        l0=Label(timerFrame, text="STARTS")
        l0.after(100, lambda:countdowntimer())


        buttonsFrame = LabelFrame(room2Win)
        buttonsFrame.grid(row=1,column=1,sticky='WENS')
        buttonsLabel=Label(buttonsFrame, text="                        BUTTONS                  ")
        buttonsLabel.configure(font= titles_font)
        buttonsLabel.pack()
        rightBTN = Button(buttonsFrame, text="Right")
        rightBTN.place(x=280, y=30)
        leftBTN= Button(buttonsFrame, text="Left")
        leftBTN.place(x=130, y=30)
        frontBTN= Button(buttonsFrame, text="Front")
        frontBTN.place(x=210, y=30)
        okBTN=Button(buttonsFrame, text="Ok")
        okBTN.place(x=280, y=90)
        attemptBTN=Button(buttonsFrame, text="Attempt to solve")
        attemptBTN.place(x=100, y=90) 
        hintBTN=Button(buttonsFrame, text="Hint")
        hintBTN.place(x=130, y=150)     
        nextBTN=Button(buttonsFrame, text="Next")
        nextBTN.place(x=280, y=150)   
    
        
        def frontside_room2(event):
            frontside1=Label(terminalFrame, text="There is a fireplace with a few logs of dry wood."*1, wraplengt=800)
            frontside1.configure(font = normal_font)
            frontside1.place(x=10, y=310) 
        def leftside_room2(event):
            leftside1=Label(terminalFrame, text="You see a few matches, a kerosene lamp, and a candle lying in the left corner of the room."*1, wraplengt=800)
            leftside1.configure(font = normal_font)
            leftside1.place(x=10, y=340)
            leftside2=Label(terminalFrame, text="There is also another door that has a wallpaper of blazing fire on it. Probably a clue leading to the next room, you think."*1, wraplengt=800)       
            leftside2.configure(font = normal_font)
            leftside2.after(1000, lambda:leftside2.place(x=10, y=370))
        def rightside_room2(event):
            rightside1=Label(terminalFrame, text="\'SOLVE AND MOVE FORWARD\' these letters are painted in bold on the right wall of the room."*1, wraplengt=800)
            rightside1.configure(font = normal_font)
            rightside1.place(x=10, y=400)
        def attempt_room2(event):
            attempt_room2.counter+=1
            l1=Label(terminalFrame, text="The note that was printed on the balls must make some sense now....."*1, wraplengt=800)
            l1.configure(font = normal_font)
            l1.place(x=10,y=430)           
            l2=Label(terminalFrame, text="What would you light first?"*1, wraplengt=800)
            l2.configure(font = normal_font)
            l2.place(x=10,y=460)
            l3=Label(chancesFrame, text="                                                                                                                                                                                                                            "*1, wraplengt=380)
            l3.place(x=10,y=30)
            l9=Label(chancesFrame, text="                                                                                                                                                                                                                            "*1, wraplengt=380)
            l9.place(x=10,y=40)
            def hint_room2(event):
                l4=Label(terminalFrame, text="HINT: Think logically!")
                l4.configure(font = hint_font)
                l4.place(x=10,y=650)
                           
            def checkans(event):
                
                ans = attempt2.get()
                if ans=='matches' or ans=='MATCHES' or ans=='match' or ans=='MATCH':
                    l5=Label(terminalFrame, text="Yay!! You cracked this! The door has opened for you to enter the next room."*1, wraplengt=800) 
                    l5.configure(font = normal_font)
                    l5.place(x=10,y=520)
                    global minleft2, secleft2
                    minleft2=9-int(minute.get())
                    secleft2=59-int(second.get())
                    nextBTN.bind('<Button-1>', room3)    
                    finalcall=Label(terminalFrame, text="You've got 10 seconds before this room closes. Therefore hurry up and click on the next button to move to the next room, lest you are out of the game."*1, wraplengt=800)
                    finalcall.configure(font = normal_font)
                    finalcall.after(1000, lambda:finalcall.place(x=10, y=550))
                    room2Win.after(15000,lambda:room2Win.destroy())                    
                            
                elif ans!='matches' or ans!='MATCHES' or ans!='match' or ans!='MATCH':
                    # chances-=1                        
                    if attempt_room2.counter==1:
                        l6=Label(chancesFrame, text="Wrong answer! You've got two more chances before this room closes."*1, wraplengt=380)
                        l6.configure(font = normal_font)
                        l6.place(x=10,y=30)
                    if attempt_room2.counter==2:
                        l7=Label(chancesFrame, text="Wrong answer! You've got one more chance before this room closes."*1, wraplengt=380)
                        l7.configure(font = normal_font)
                        l7.place(x=10,y=30)
                    if attempt_room2.counter==3:
                        l8=Label(chancesFrame, text="Wrong answer! You've exhausted all your 3 chances....bye-bye!                                                                                      "*1, wraplengt=380)
                        l8.configure(font = normal_font)
                        l8.place(x=10,y=30)
                        room2Win.after(3000,lambda:room2Win.destroy())                    
                

            attempt2=Entry(terminalFrame)
            attempt2.place(x=10, y=490)
            attempt2.focus_set()

            okBTN.bind('<Button-1>', checkans)
            hintBTN.bind('<Button-1>', hint_room2)

        about1=Label(terminalFrame, text="Well, now you are in the second room. It is a dimly lit room and you can barely see anything. From nowhere, a bunch of balls come rolling on the floor. You can see that all of them have something in common printed on them."  *1, wraplengt=800)
        about1.configure(font = normal_font)
        about1.after(1000, lambda:about1.place(x=10, y=30))
        img=ImageTk.PhotoImage(Image.open("C:/Users/CHANDANA/OneDrive/Desktop/PythonProject/text_based_game/balls_room2.jpg")) #change file path accordingly
        balls_img=Label(terminalFrame,image=img)
        balls_img.after(2500, lambda:balls_img.place(x=10,y=60))
        decision=Label(terminalFrame, text="The print on the balls read: \"What would you light first?\" So much ambiguity in this room, you think. You start to look around the room for clues. "*1, wraplengt=800)
        decision.configure(font = normal_font)
        decision.after(4000, lambda:decision.place(x=10, y=280))
        rightBTN.bind('<Button-1>', rightside_room2)
        leftBTN.bind('<Button-1>', leftside_room2) 
        frontBTN.bind('<Button-1>', frontside_room2)
        attempt_room2.counter=0
        attemptBTN.bind('<Button-1>', attempt_room2)

        room2Win.mainloop()
    
    def room3(event):
        room3Win=Toplevel(gameWin)
        room3Win.title("GAME-The Escape Room")
        room3Win.state('zoomed')
        width1= room3Win.winfo_screenwidth()
        height1= room3Win.winfo_screenheight()

        room3Win.columnconfigure(0,weight=1)
        room3Win.columnconfigure(1,weight=1)    
        room3Win.rowconfigure(0, weight=4) 
        room3Win.rowconfigure(1, weight=4) # change weight to 4
        room3Win.rowconfigure(2, weight=4)

        """ s3 = ttk.Style()
        s3.configure("TLabel", background='old lace')
        s3.configure("TLabelframe",background='old lace') """

        titles_font= ("Century Schoolbook",10,"bold", "underline")
        normal_font = ("Lucida Fax",8)
        hint_font = ("Lucida Fax",8,"bold")
        voice_font=("Lucida Calligraphy",8)

        terminalFrame = LabelFrame(room3Win, height=750, width=800)
        terminalFrame.grid(row=0,column=0, rowspan=3,sticky='WENS')
        terminalFrame.grid_propagate(False)
        terminalLabel=Label(terminalFrame, text="                                                                                                                           ROOM 3                                                                                                                    ")
        terminalLabel.configure(font= titles_font)
        terminalLabel.pack()

        chancesFrame = LabelFrame(room3Win)
        chancesFrame.grid(row=2,column=1,sticky='WENS')
        chancesLabel=Label(chancesFrame, text="              CHANCES LEFT             ")
        chancesLabel.configure(font= titles_font)
        chancesLabel.pack()

        timerFrame = LabelFrame(room3Win)
        timerFrame.grid(row=0,column=1,sticky='WENS')
        timerLabel=Label(timerFrame, text="                                                 TIMER                                                   ")
        timerLabel.configure(font= titles_font)
        timerLabel.pack()
        
        minute=StringVar()
        second=StringVar()
  
        minute.set("10")
        second.set("00")
        
        mins_box = Entry(
	        timerFrame, 
	        width=3, 
	        font=("Arial",20),
	        textvariable=minute)
        mins_box.place(x=150,y=20)
  
        sec_box = Entry(
	        timerFrame, 
	        width=3,
	        font=("Arial",20),
	        textvariable=second)
        sec_box.place(x=250,y=20)
  
        def countdowntimer():
    
            default= int(minute.get())*60 + int(second.get())

            while default>-1:
         
                mins,secs = divmod(default,60)
                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))
  
                timerFrame.update()
                time.sleep(1)
            
                if (default== 0):
                    L1=Label(timerFrame, text="Time-up!! The room is closing in a second").place(x=100, y=100)
                    L2=Label(timerFrame, text="dummy")
                    L2.after(1500, lambda:room3Win.destroy())
         
                default-= 1

        l0=Label(timerFrame, text="STARTS")
        l0.after(100, lambda:countdowntimer())

        buttonsFrame = LabelFrame(room3Win)
        buttonsFrame.grid(row=1,column=1,sticky='WENS')
        buttonsLabel=Label(buttonsFrame, text="                        BUTTONS                  ")
        buttonsLabel.configure(font= titles_font)
        buttonsLabel.pack()
        downBTN = Button(buttonsFrame, text="Down")
        downBTN.place(x=280, y=30)
        rightBTN= Button(buttonsFrame, text="Right")
        rightBTN.place(x=130, y=30)
        frontBTN= Button(buttonsFrame, text="Front")
        frontBTN.place(x=210, y=30)
        okBTN=Button(buttonsFrame, text="Ok")
        okBTN.place(x=280, y=90)
        attemptBTN=Button(buttonsFrame, text="Attempt to solve")
        attemptBTN.place(x=100, y=90) 
        hintBTN=Button(buttonsFrame, text="Hint")
        hintBTN.place(x=130, y=150)     
        nextBTN=Button(buttonsFrame, text="Next")
        nextBTN.place(x=280, y=150)  

    

        def rightside_room3(event):
            rightside1=Label(terminalFrame, text="You look to your right and see a scary painting"*1, wraplengt=800)
            rightside1.configure(font = normal_font)
            rightside1.place(x=10, y=60)
            global img1
            img1=ImageTk.PhotoImage(Image.open("C:/Users/CHANDANA/OneDrive/Desktop/PythonProject/text_based_game/hangingrope_room3.jpg")) #change file path accordingly
            hangingrope_img=Label(terminalFrame,image=img1)
            hangingrope_img.after(1200, lambda:hangingrope_img.place(x=10,y=90))
        
        def downside_room3(event):
            downside1=Label(terminalFrame, text="You look at the floor and find these two phrases scribbled all over it \'GHOST HUNTERS-----PARANORMAL INVESTIGATORS\'. Creepy enough you think to yourself. "*1, wraplengt=800)
            downside1.configure(font = normal_font)
            downside1.place(x=10, y=270)

        def frontside_room3(event):
            frontside1=Label(terminalFrame, text="You see a door that probably leads to the next room, but the code painted in white on top of the door catches your attention."*1, wraplengt=800)
            frontside1.configure(font = normal_font)
            frontside1.place(x=10, y=300)
            global img2
            img2 =ImageTk.PhotoImage(Image.open("C:/Users/CHANDANA/OneDrive/Desktop/PythonProject/text_based_game/morsecode_room3.jpg")) #change file path accordingly
            morsecode_img=Label(terminalFrame,image=img2)
            morsecode_img.after(2000, lambda:morsecode_img.place(x=10,y=330))
            frontside2=Label(terminalFrame, text="\"Now I know that you aren't too good at deciphering codes like this, hence I have given you ample \'HINTS\' . If you know what I mean\" you hear a mysterious man speak through the speakers in the room. )"*1, wraplengt=800)       
            frontside2.configure(font = voice_font)
            frontside2.after(4500, lambda:frontside2.place(x=10, y=470))
        
        def attempt_room3(event):
            attempt_room3.counter+=1
            l1=Label(terminalFrame, text="\"And I see that you are brave enough to attempt to answer this room's mystery\", you hear the same voice again"*1, wraplengt=800)
            l1.configure(font = voice_font)
            l1.place(x=10, y=500)
            ques=Label(terminalFrame, text="What do you think all the clues are leading up to? Also did you decipher the code yet? Try keying in your answer below."*1, wraplengt=800)
            ques.configure(font = normal_font)
            ques.after(1000,lambda: ques.place(x=10,y=530))
            l2=Label(chancesFrame, text="                                                                                                                                                                                                                            "*1, wraplengt=380).place(x=10, y=30)
            l8=Label(chancesFrame, text="                                                                                                                                                                                                                            "*1, wraplengt=380).place(x=10, y=40)
            
            def hint_room3(event):
                global img3
                img3=ImageTk.PhotoImage(Image.open("C:/Users/CHANDANA/OneDrive/Desktop/PythonProject/text_based_game/morsecoderef_room3.jpg")) #change file path accordingly
                morsecoderef_img=Label(terminalFrame,image=img3)
                morsecoderef_img.after(2000,lambda:morsecoderef_img.place(x=400,y=315))
                           
            def checkans(event):
                
                ans = attempt3.get()
                if ans=='THE CONJURING' or ans=='the conjuring':
                    l2=Label(terminalFrame, text="Yay!! You cracked this! The door has opened for you to enter the next room."*1, wraplengt=800) 
                    l2.configure(font = normal_font)
                    l2.place(x=10, y=590)
                    global minleft3, secleft3
                    minleft3=9-int(minute.get())
                    secleft3=59-int(second.get())
                    nextBTN.bind('<Button-1>', room4)    
                    finalcall=Label(terminalFrame, text="You've got 10 seconds before this room closes. Therefore hurry up and click on the next button to move to the next room, lest you are out of the game"*1, wraplengt=800)
                    finalcall.configure(font = normal_font)
                    finalcall.after(1000, lambda:finalcall.place(x=10, y=620))
                    room3Win.after(15000,lambda:room3Win.destroy())                                    
                elif ans!='THE CONJURING' or ans!='the conjuring':
                    # chances-=1                        
                    if attempt_room3.counter==1:
                        l3=Label(chancesFrame, text="Wrong answer! You've got two more chances before this room closes."*1, wraplengt=380)
                        l3.configure(font = normal_font)
                        l3.place(x=10, y=30)
                    if attempt_room3.counter==2:
                        l4=Label(chancesFrame, text="Wrong answer! You've got one more chance before this room closes."*1, wraplengt=380)
                        l4.configure(font = normal_font)
                        l4.place(x=10, y=30)
                    if attempt_room3.counter==3:
                        l5=Label(chancesFrame, text="Wrong answer! You've extinguished all your 3 chances....bye-bye!                                                                                      "*1, wraplengt=380)
                        l5.configure(font = normal_font)
                        l5.place(x=10, y=30)
                        room3Win.after(3000,lambda:room3Win.destroy())                    
                

            attempt3=Entry(terminalFrame)
            attempt3.place(x=10, y=560)
            attempt3.focus_set()

            okBTN.bind('<Button-1>', checkans)
            hintBTN.bind('<Button-1>', hint_room3)

        about1=Label(terminalFrame, text="Room 3 it is! This room has such an eerie feeling to it. It feels like something straight out of a horror movie. A thoroughly dark scene coming up, you sense...."  *1, wraplengt=800)
        about1.configure(font = normal_font)
        about1.after(1000, lambda:about1.place(x=10, y=30))
        rightBTN.bind('<Button-1>', rightside_room3)
        frontBTN.bind('<Button-1>', frontside_room3) 
        downBTN.bind('<Button-1>', downside_room3)
        attempt_room3.counter=0
        attemptBTN.bind('<Button-1>', attempt_room3)

        room3Win.mainloop()

    def room4(event):
        room4Win=Toplevel(gameWin)
        room4Win.title("GAME-The Escape Room")
        room4Win.state('zoomed')
        width1= room4Win.winfo_screenwidth()
        height1= room4Win.winfo_screenheight()

        room4Win.columnconfigure(0,weight=1)
        room4Win.columnconfigure(1,weight=1)    
        room4Win.rowconfigure(0, weight=4) 
        room4Win.rowconfigure(1, weight=4) # change weight to 4
        room4Win.rowconfigure(2, weight=4)

        titles_font= ("Century Schoolbook",10,"bold", "underline")
        normal_font = ("Lucida Fax",8)
        hint_font = ("Lucida Fax",8,"bold")
        voice_font=("Lucida Calligraphy",8)

        terminalFrame = LabelFrame(room4Win, height=750, width=800)
        terminalFrame.grid(row=0,column=0, rowspan=3,sticky='WENS')
        terminalFrame.grid_propagate(False)
        terminalLabel=Label(terminalFrame, text="                                                                                                                           ROOM 4                                                                                                                   ")
        terminalLabel.configure(font= titles_font)
        terminalLabel.pack()

        chancesFrame = LabelFrame(room4Win)
        chancesFrame.grid(row=2,column=1,sticky='WENS')
        chancesLabel=Label(chancesFrame, text="              CHANCES LEFT             ")
        chancesLabel.configure(font= titles_font)
        chancesLabel.pack()

        timerFrame = LabelFrame(room4Win)
        timerFrame.grid(row=0,column=1,sticky='WENS')
        timerLabel=Label(timerFrame, text="                                                 TIMER                                                   ")
        timerLabel.configure(font= titles_font)
        timerLabel.pack()

        minute=StringVar()
        second=StringVar()
  
        minute.set("10")
        second.set("00")
        
        mins_box = Entry(
	        timerFrame, 
	        width=3, 
	        font=("Arial",20),
	        textvariable=minute)
        mins_box.place(x=150,y=20)
  
        sec_box = Entry(
	        timerFrame, 
	        width=3,
	        font=("Arial",20),
	        textvariable=second)
        sec_box.place(x=250,y=20)
  
        def countdowntimer():
    
            default= int(minute.get())*60 + int(second.get())

            while default>-1:
         
                mins,secs = divmod(default,60)
                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))
  
                timerFrame.update()
                time.sleep(1)
            
                if (default== 0):
                    L1=Label(timerFrame, text="Time-up!! The room is closing in a second").place(x=100, y=100)
                    L2=Label(timerFrame, text="dummy")
                    L2.after(1500, lambda:room4Win.destroy())
         
                default-= 1

        l0=Label(timerFrame, text="STARTS")
        l0.after(100, lambda:countdowntimer())


        buttonsFrame = LabelFrame(room4Win)
        buttonsFrame.grid(row=1,column=1,sticky='WENS')
        buttonsLabel=Label(buttonsFrame, text="                        BUTTONS                  ")
        buttonsLabel.configure(font= titles_font)
        buttonsLabel.pack()
        rightBTN = Button(buttonsFrame, text="Right")
        rightBTN.place(x=280, y=30)
        leftBTN= Button(buttonsFrame, text="Left")
        leftBTN.place(x=130, y=30)
        frontBTN= Button(buttonsFrame, text="Front")
        frontBTN.place(x=210, y=30)
        okBTN=Button(buttonsFrame, text="Ok")
        okBTN.place(x=280, y=90)
        attemptBTN=Button(buttonsFrame, text="Attempt to solve")
        attemptBTN.place(x=100, y=90) 
        hintBTN=Button(buttonsFrame, text="Hint")
        hintBTN.place(x=130, y=150)     
        nextBTN=Button(buttonsFrame, text="Next")
        nextBTN.place(x=280, y=150)  

        def leftside_room4(event):
            leftside1=Label(terminalFrame, text="A beautiful photo frame with the photo of a PRIMA ballerina surrounded by random numbers hangs on the left wall."*1, wraplengt=800)
            leftside1.configure(font = normal_font)
            leftside1.place(x=10, y=110)
            global img1
            img1=ImageTk.PhotoImage(Image.open("C:/Users/CHANDANA/OneDrive/Desktop/PythonProject/text_based_game/primaballerina_room4.jpg")) #change file path accordingly
            hangingrope_img=Label(terminalFrame,image=img1)
            hangingrope_img.after(1200, lambda:hangingrope_img.place(x=100,y=130))
            leftside2=Label(terminalFrame, text="She is the \"PRIME\" ballerina in a ballet troupe, so since this room is about math, there must be something with her and the numbers surrounding her...."*1, wraplengt=800)       
            leftside2.configure(font = normal_font)
            leftside2.after(2800, lambda:leftside2.place(x=10, y=280))   
    
        
        def frontside_room4(event):
            frontside1=Label(terminalFrame, text="And now you are staring at a wall with numeric wallpaper:\ More numbers, more problems:{"*1, wraplengt=800)
            frontside1.configure(font = normal_font)
            frontside1.place(x=10, y=310) 
        
        def rightside_room4(event):
            rightside1=Label(terminalFrame, text="There's a table on your right that has a picture of people sharing a delicious dessert on it."*1, wraplengt=800)
            rightside1.configure(font = normal_font)
            rightside1.place(x=10, y=340)
            global img2
            img2=ImageTk.PhotoImage(Image.open("C:/Users/CHANDANA/OneDrive/Desktop/PythonProject/text_based_game/pie_room4.jpg")) #change file path accordingly
            pie_img=Label(terminalFrame,image=img2)
            pie_img.after(1200, lambda:pie_img.place(x=100,y=370))
            rightside2=Label(terminalFrame, text="\"What's this dessert called? And how many are sharing it? How much portion would each person get?\" a note beside the picture bombards you with these questions."*1, wraplengt=800)
            rightside1.configure(font = normal_font)
            rightside2.after(2200, lambda:rightside2.place(x=10, y=480))


        def attempt_room4(event):
            attempt_room4.counter+=1
            l1=Label(terminalFrame, text="You need to give a 6-digit numeric code which is formed using the two clues given on the left and right sides of the room."*1, wraplengt=800)
            l1.configure(font = normal_font)
            l1.place(x=10,y=510)
            l2=Label(terminalFrame, text="The first 3 digits are to be derived from the prima ballerina photo and the last 3 from the pie-sharing picture."*1, wraplengt=800)
            l2.configure(font = normal_font)
            l2.place(x=10,y=540)
            l3=Label(chancesFrame, text="                                                                                                                                                                                                                            "*1, wraplengt=380).place(x=10, y=30)
            l4=Label(chancesFrame, text="                                                                                                                                                                                                                            "*1, wraplengt=380).place(x=10, y=40)
            def hint_room4(event):
                l5=Label(terminalFrame, text="HINT 1: This \"PRIME\" ballerina is in the 4th room and is surrounded by numbers which may be prima as well and indicate a 4 somehow?")
                l5.configure(font = hint_font)
                l5.place(x=10,y=660)
                l6=Label(terminalFrame, text="HINT 2: The decimal part of how much each person in the picture receives after the pi is shared equally amongst them ;) ")
                l6.configure(font = hint_font)
                l6.place(x=10,y=690)
                           
            def checkans(event):
                
                ans = attempt2.get()
                if ans=='103448' :
                    l7=Label(terminalFrame, text="Yay!! You cracked this! The door has opened for you to enter the next room."*1, wraplengt=800)
                    l7.configure(font = normal_font)
                    l7.place(x=10,y=600)
                    global minleft4, secleft4
                    minleft4=9-int(minute.get())
                    secleft4=59-int(second.get())
                    nextBTN.bind('<Button-1>', room5)    
                    finalcall=Label(terminalFrame, text="You've got 10 seconds before this room closes. Therefore hurry up and click on the next button to move to the next room, lest you are out of the game"*1, wraplengt=800)
                    finalcall.configure(font=normal_font)
                    finalcall.after(1000, lambda:finalcall.place(x=10, y=630))
                    room4Win.after(15000,lambda:room4Win.destroy())                    
                            
                elif ans!='103448':
                    # chances-=1                        
                    if attempt_room4.counter==1:
                        l8=Label(chancesFrame, text="Wrong answer! You've got two more chances before this room closes."*1, wraplengt=380)
                        l8.configure(font = normal_font)
                        l8.place(x=10,y=30)
                    if attempt_room4.counter==2:
                        l9=Label(chancesFrame, text="Wrong answer! You've got one more chance before this room closes."*1, wraplengt=380)
                        l9.configure(font = normal_font)
                        l9.place(x=10,y=30)
                    if attempt_room4.counter==3:
                        l10=Label(chancesFrame, text="Wrong answer! You've extinguished all your 3 chances....bye-bye!                                                                                      "*1, wraplengt=380)
                        l10.configure(font = normal_font)
                        l10.place(x=10,y=30)
                        room4Win.after(3000,lambda:room4Win.destroy())                    
                

            attempt2=Entry(terminalFrame)
            attempt2.place(x=10, y=570)
            attempt2.focus_set()

            okBTN.bind('<Button-1>', checkans)
            hintBTN.bind('<Button-1>', hint_room4)

        about1=Label(terminalFrame, text="As soon as you enter this room, you hear a song play in the background, actually, it's some stupid nursery rhyme about numbers and math. \"I have always hated math....hopefully, this room isn't about it\" you whisper to yourself"  *1, wraplengt=800)
        about1.configure(font =normal_font)
        about1.after(1000, lambda:about1.place(x=10, y=30))
        about2=Label(terminalFrame, text="Disappointment shines bright on your face when you look at the ceiling and read \'FUN WITH NUMBERS BEGINS\'. This is enough reason for you to believe that you will be sinking into the whirlpool of math."*1, wraplengt=800)
        about2.configure(font = normal_font)
        about2.after(2100, lambda:about2.place(x=10, y=60))
        decision=Label(terminalFrame, text="Nevertheless, you decide to explore around...."*1, wraplengt=800)
        decision.configure(font = normal_font)
        decision.after(3150, lambda:decision.place(x=10, y=90))
        rightBTN.bind('<Button-1>', rightside_room4)
        leftBTN.bind('<Button-1>', leftside_room4) 
        frontBTN.bind('<Button-1>', frontside_room4)
        attempt_room4.counter=0
        attemptBTN.bind('<Button-1>', attempt_room4)

        room4Win.mainloop()

    def room5(event):
        room5Win=Toplevel(gameWin)
        room5Win.title("GAME-The Escape Room")
        room5Win.state('zoomed')
        width1= room5Win.winfo_screenwidth()
        height1= room5Win.winfo_screenheight()

        room5Win.columnconfigure(0,weight=1)
        room5Win.columnconfigure(1,weight=1)    
        room5Win.rowconfigure(0, weight=4) 
        room5Win.rowconfigure(1, weight=4) # change weight to 4
        room5Win.rowconfigure(2, weight=4)

        # style = ttk.Style()
  

        # style.theme_use('winnative')
        # style.configure("TLabelframe", bordercolor="red")

        """ s5 = ttk.Style()
        s5.configure("TLabel", background='PaleTurquoise1')
        s5.configure("TLabelframe",background='PaleTurquoise1') """
        titles_font= ("Century Schoolbook",10,"bold", "underline")
        normal_font = ("Lucida Fax",8)
        hint_font = ("Lucida Fax",8,"bold")
        voice_font=("Lucida Calligraphy",8)
        

        terminalFrame = LabelFrame(room5Win, height=750, width=800)
        terminalFrame.grid(row=0,column=0, rowspan=3,sticky='WENS')
        terminalFrame.grid_propagate(False)
        terminalLabel=Label(terminalFrame, text="                                                                                                                           ROOM 5                                                                                                                  ")
        terminalLabel.configure(font = titles_font)
        terminalLabel.pack()

        chancesFrame = LabelFrame(room5Win)
        chancesFrame.grid(row=2,column=1,sticky='WENS')
        chancesLabel=Label(chancesFrame, text="              CHANCES LEFT             ")
        chancesLabel.configure(font = titles_font)
        chancesLabel.pack()

        timerFrame = LabelFrame(room5Win)
        timerFrame.grid(row=0,column=1,sticky='WENS')
        timerLabel=Label(timerFrame, text="                                                 TIMER                                                   ")
        timerLabel.configure(font = titles_font)
        timerLabel.pack()

        minute=StringVar()
        second=StringVar()
  
        minute.set("10")
        second.set("00")
        
        mins_box = Entry(
	        timerFrame, 
	        width=3, 
	        font=("Arial",20),
	        textvariable=minute)
        mins_box.place(x=150,y=20)
  
        sec_box = Entry(
	        timerFrame, 
	        width=3,
	        font=("Arial",20),
	        textvariable=second)
        sec_box.place(x=250,y=20)
  
        def countdowntimer():
    
            default= int(minute.get())*60 + int(second.get())

            while default>-1:
         
                mins,secs = divmod(default,60)
                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))
  
                timerFrame.update()
                time.sleep(1)
            
                if (default== 0):
                    L1=Label(timerFrame, text="Time-up!! The room is closing in a second").place(x=100, y=100)
                    L2=Label(timerFrame, text="dummy")
                    L2.after(1500, lambda:room5Win.destroy())
         
                default-= 1

        l0=Label(timerFrame, text="STARTS")
        l0.after(100, lambda:countdowntimer())

        buttonsFrame = LabelFrame(room5Win)
        buttonsFrame.grid(row=1,column=1,sticky='WENS')
        buttonsLabel=Label(buttonsFrame, text="                        BUTTONS                  ")
        buttonsLabel.configure(font= titles_font)
        buttonsLabel.pack()
        turnaroundBTN = Button(buttonsFrame, text="Turn Around")
        turnaroundBTN.place(x=265, y=30)
        ledscreenBTN = Button(buttonsFrame, text="Launch LED")
        ledscreenBTN.place(x=115, y=30)   
        okBTN=Button(buttonsFrame, text="OK")
        okBTN.place(x=280, y=90) 
        attemptBTN=Button(buttonsFrame, text="Attempt to solve")
        attemptBTN.place(x=100, y=90) 
        hintBTN=Button(buttonsFrame, text="Hint")
        hintBTN.place(x=130, y=150)   
        finishBTN=Button(buttonsFrame, text="Finish")
        finishBTN.place(x=280, y=150)



        def turnaround_room5(event):
            turnaround1=Label(terminalFrame, text="So you decide to turn a full circle to have complete look at the entire room as you are keen on finding anything which might be \"THE\" clue. While you are in this process, you hear a voice....."*1, wraplengt=800)
            turnaround1.configure(font = normal_font)
            turnaround1.place(x=10, y=205)  
            turnaround2=Label(terminalFrame, text="\"Once you determine the angle you turn to get a full view of this room, sum up the individual digits of that angle and you are halfway through your victory\", the same voice from the third room. "*1, wraplengt=800)
            turnaround2.configure(font = voice_font)
            turnaround2.place(x=10, y=235)   
    
        
        def ledscreens(event):
            ledscreens1=Label(terminalFrame, text="You are still pretty clueless and doubting whether the angle you have in guess is correct or not when the LED screens power up and display this image all over them."*1, wraplengt=800)
            ledscreens1.configure(font = normal_font)
            ledscreens1.place(x=10, y=265) 
            global img2
            img2=ImageTk.PhotoImage(Image.open("C:/Users/CHANDANA/OneDrive/Desktop/PythonProject/text_based_game/led_room5.jpg")) #change file path accordingly
            led_img=Label(terminalFrame,image=img2)
            led_img.after(1000, lambda:led_img.place(x=10,y=295))
            ledscreens2=Label(terminalFrame, text="\"You are majoring in CS\", the same person you heard before says \"Understanding this should be a piece of cake for you, but I will give you a few spoilers. The next thing to do after you get the sum of the angles' digits, is to make a computer understand that number in its own language \" with this little hint the mysterious voice goes on mute."*1, wraplengt=800)
            ledscreens2.configure(font = voice_font)
            ledscreens2.after(2000, lambda:ledscreens2.place(x=10, y=375))
        
        def attempt_room5(event):
            attempt_room5.counter+=1
            l1=Label(terminalFrame, text="\"I suppose you have the object code ready\", the mystery man speaks again \"You are just 1 final step away from your grand escape. All you have to do now is replace the characters of the object code as follows:"*1, wraplengt=800)
            l1.configure(font = voice_font)
            l1.place(x=10,y=430)
            l2=Label(terminalFrame, text="A) That \'1\'st ranker in school who would proudly \'exclaim\' how good he/she did in the exams"*1, wraplengt=800)
            l2.configure(font = voice_font)
            l2.place(x=10,y=460)
            l3=Label(terminalFrame, text="B) No one could \'score\' anything \'under\' a \'0\' in an exam"*1, wraplengt=800)
            l3.configure(font = voice_font)
            l3.place(x=10,y=475)
            l4=Label(terminalFrame, text="\"All you have to do is find symbols which correspond to both the statements above\"says the mystery man"*1, wraplengt=800)
            l4.configure(font = voice_font)
            l4.place(x=10,y=490)
            l5=Label(terminalFrame, text="So, what do you think the final 4-character code is??"*1, wraplengt=800)
            l5.configure(font = voice_font)
            l5.place(x=10,y=510)
            Label(chancesFrame, text="                                                                                                                                                                                                                                                                                                                                                                                                                                        "*1, wraplengt=380).place(x=10, y=30)
            Label(chancesFrame, text="                                                                                                                                                                                                                                                                                                                                                                                                                                        "*1, wraplengt=380).place(x=10, y=40)
            
            def hint_room5(event):
                l6=Label(terminalFrame, text="HINT 1: The angle = a full angle(mathematically)")
                l6.configure(font = hint_font)
                l6.place(x=10,y=600)
                l7=Label(terminalFrame, text="HINT 2: The language which has only 2 letters/characters. Try converting the sum into this language")
                l7.configure(font = hint_font)
                l7.place(x=10,y=630)
                l8=Label(terminalFrame, text="HINT 3: While trying to replace characters, pay close attention to the highlighted words, the number which is to be replaced with a specific symbol is implicitly depicted "*1, wraplengt=800)
                l8.configure(font = hint_font)
                l8.place(x=10,y=660)
                           
            def checkans(event):
                
                ans = attempt2.get()
                if ans=='!__!' :
                    l9=Label(terminalFrame, text="Yay!! You cracked this! You've finished the final room of the series. Well done!! Click on the finish button to end the game."*1, wraplengt=800) 
                    l9.configure(font =normal_font)
                    l9.place(x=10,y=560)
                    global minleft5, secleft5
                    minleft5=9-int(minute.get())
                    secleft5=59-int(second.get())
                    finishBTN.bind('<Button-1>', finish)                      
                            
                elif ans!='!__!':
                    # chances-=1                        
                    if attempt_room5.counter==1:
                        l10=Label(chancesFrame, text="Wrong answer! You've got two more chances before this room closes."*1, wraplengt=380)
                        l10.configure(font =normal_font)
                        l10.place(x=10,y=30)
                    if attempt_room5.counter==2:
                        l11=Label(chancesFrame, text="Wrong answer! You've got one more chance before this room closes."*1, wraplengt=380)
                        l11.configure(font =normal_font)
                        l11.place(x=10,y=30)
                    if attempt_room5.counter==3:
                        l12=Label(chancesFrame, text="Wrong answer! You've extinguished all your 3 chances....bye-bye!                                                                                      "*1, wraplengt=380)
                        l12.configure(font =normal_font)
                        l12.place(x=10,y=30)
                        room5Win.after(3000,lambda:room5Win.destroy())                    
                

            attempt2=Entry(terminalFrame)
            attempt2.place(x=10, y=530)
            attempt2.focus_set()

            okBTN.bind('<Button-1>', checkans)
            hintBTN.bind('<Button-1>', hint_room5)
        
        # s.configure("TLabel", background="light blue")
        
  
        
        about1=ttk.Label(terminalFrame, text="Remember how in the previous room there was no mention of the next door? Well, that was because you were to be placed in the center of a round room that doesn't have four walls, but rather has LED screens in a curvature running the entire circumference of the room. "  *1, wraplengt=800,style="TLabel")
        about1.configure(font = normal_font)
        about1.after(1000, lambda:about1.place(x=10, y=30))
        img=ImageTk.PhotoImage(Image.open("C:/Users/CHANDANA/OneDrive/Desktop/PythonProject/text_based_game/roundroom_room5.jpg")) #change file path accordingly
        roundroom_img=Label(terminalFrame,image=img)
        roundroom_img.after(2300, lambda:roundroom_img.place(x=10,y=60))
        decision=Label(terminalFrame, text="The room has absolutely no clues. Nothing comes rolling towards you, no paintings or pictures, no wordings on the walls, or the floor, or even the ceiling. The walls are nothing but LED screens."*1, wraplengt=800)
        decision.configure(font = normal_font)
        decision.after(3000, lambda:decision.place(x=10, y=175))
        turnaroundBTN.bind('<Button-1>', turnaround_room5)
        ledscreenBTN.bind('<Button-1>', ledscreens)
        attempt_room5.counter=0
        attemptBTN.bind('<Button-1>', attempt_room5)

        room5Win.mainloop()

    def finish(event):
        endWin=Toplevel(gameWin)
        endWin.title("GAME-The Escape Room")
        endWin.state('zoomed')
        width1= endWin.winfo_screenwidth()
        height1= endWin.winfo_screenheight()

        """ s6 = ttk.Style()
        s6.configure("TLabel", background='Lavender')
        s6.configure("TLabelframe",background='Lavender') """

        def timeleft():
            totalminleft= minleft1 + minleft2 + minleft3 + minleft4 + minleft5
            totalsecleft= int(math.fabs(secleft1) + math.fabs(secleft2) + math.fabs(secleft3) + math.fabs(secleft4) + math.fabs(secleft5))
            totalminleft2= totalminleft*602
            totaltimeleft= totalminleft2 + totalsecleft
            global mincomp, seccomp
            mincomp=totaltimeleft//60
            seccomp=totaltimeleft%60

            print(mincomp, "mins")
            print(seccomp, "seconds")

        timeleft()

        titles_font= ("Century Schoolbook",10,"bold", "underline")
        normal_font = ("Lucida Fax",8)
        # hint_font = ("Lucida Fax",8,"bold")
        # voice_font=("Lucida Calligraphy",8)
        certificate_font1 = ("Comic Sans MS", 18, "bold")
        certificate_font2 = ("Comic Sans MS", 14, "bold")
        certificate_font3 = ("Comic Sans MS", 12, "bold")


        terminalFrame = LabelFrame(endWin, height=750, width=800)
        terminalFrame.grid(row=0,column=0, rowspan=3,sticky='WENS')
        terminalFrame.grid_propagate(False)
        terminalFrame.pack(expand=1, fill=BOTH)
        terminalLabel=Label(terminalFrame, text="                                                                                                                           EPILOGUE                                                                                                                   ")
        terminalLabel.configure(font= titles_font)
        terminalLabel.pack()
        l1=Label(terminalFrame, text="Congratulations on completing the escape room adventure and making it to the end."*1,wraplengt=800)
        l2=Label(terminalFrame,text="You are a keen observer who is also quick-witted and pays attention to details."*1,wraplengt=800)
        l3=Label(terminalFrame, text="Thanks for being here!!"*1,wraplengt=800)

        l1.configure(font = normal_font)
        l2.configure(font = normal_font)
        l3.configure(font = normal_font)

        l1.place(x=10,y=30)
        l2.place(x=10,y=60)
        l3.place(x=10,y=90)

        global finalimg
        finalimg=ImageTk.PhotoImage(Image.open("C:/Users/CHANDANA/OneDrive/Desktop/PythonProject/text_based_game/certifcate_endWin.jpg")) #change file path accordingly
        certificate_img=Label(terminalFrame,image=finalimg)
        certificate_img.after(1000, lambda:certificate_img.place(x=280,y=90))

        name=Label(terminalFrame, text=nameENT.get())
        print(nameENT.get())
        name.configure(font=certificate_font1)
        name.after(1200, lambda:name.place(x=580, y=220))
        

        timetaken=str(mincomp)+" minutes "+str(seccomp)+" seconds "
        print(timetaken)
        strvar=StringVar(endWin, name="timetocomplete")
        endWin.setvar(name="timetocomplete",value=str(timetaken))
        timecomp=Label(terminalFrame, text=strvar.get())
        timecomp.configure(font=certificate_font2)
        timecomp.after(2600, lambda:timecomp.place(x=555, y=460))
        

        todayfromfunc=date.today()
        print(todayfromfunc)
        strvar2= StringVar(endWin, name="today")
        endWin.setvar(name="today",value=str(todayfromfunc))
        date2=Label(terminalFrame, text=strvar2.get())
        date2.configure(font=certificate_font3)
        date2.after(3400, lambda:date2.place(x=600, y=560))

        
    
        endWin.mainloop()
    

    gameWin.columnconfigure(0,weight=1)
    gameWin.columnconfigure(1,weight=1)
    gameWin.rowconfigure(0, weight=4) 
    gameWin.rowconfigure(1, weight=4) # change weight to 4
    gameWin.rowconfigure(2, weight=4)

    terminalFrame1 = LabelFrame(gameWin, height=750, width=800)
    terminalFrame1.grid(row=0,column=0, rowspan=3,sticky='WENS')
    terminalFrame1.grid_propagate(False)
    terminalFrame1.pack(expand=1, fill=BOTH)
    terminalLabel=Label(terminalFrame1, text="                                                                                                                          PROLOGUE                                                                                                                   ")
    terminalLabel.configure(font=titles_font)
    terminalLabel.pack()

    intro()
    detailsEntry()

    menubar = Menu(gameWin)
    def newGame():
        startBTN()
 
    def statistics():
        a=startBTN.counter
        l=list()
        line="Number of times this game has been tried/played/visited/cursed at by people :) ;) = "
        l.append(line)
        l.append(a)
    
        messagebox.showinfo("Statistics",l)

    Main = Menu(menubar, tearoff=0)  
    Main.add_command(label="New game",command=newGame)  
    Main.add_command(label="Statistics",command=statistics)  
    menubar.add_cascade(label="Main", menu=Main)  
    
    def aboutGame(): #func in help menu
        messagebox.showinfo("About game", "This game was developed in 2022 by Harini.B & M S Chandana as a submission to the prescribed mini project based in Python language (Python 3.11.0).")
    def howToPlay(): #func in help menu
        messagebox.showinfo("How to play","Refer to the rules given in the first window.")
    help = Menu(menubar, tearoff=0)  
    help.add_command(label="About game",command=aboutGame)
    help.add_command(label="How to play",command=howToPlay)
    help.add_command(label="Exit",command=root.quit)
    menubar.add_cascade(label="Help", menu=help)
    gameWin.config(menu=menubar)
    gameWin.mainloop()
 
# global startBTN.counter
startBTN.counter=0
startButton = tk.Button(root, text="Start", height=1, width=7, command=startBTN)
startButton_window = canvas1.create_window(650, 650, anchor=tk.CENTER, window=startButton)
 
menubar = Menu(root)
def newGame():
    startBTN()
 
def statistics():
    a=startBTN.counter
    l=list()
    line="Number of times this game has been tried/played/visited/cursed at by people :) ;) = "
    l.append(line)
    l.append(a)
    
    messagebox.showinfo("Statistics",l)

Main = Menu(menubar, tearoff=0)  
Main.add_command(label="New game",command=newGame)  
Main.add_command(label="Statistics",command=statistics)  
menubar.add_cascade(label="Main", menu=Main)  
 
def aboutGame(): 
    messagebox.showinfo("About game", "This game was developed in 2022 by Harini.B & M S Chandana as a submission to the prescribed mini project based in Python language (Python 3.11.0).")
def howToPlay(): 
    messagebox.showinfo("How to play","Refer to the rules given in the first window.")
help = Menu(menubar, tearoff=0)  
help.add_command(label="About game",command=aboutGame)
help.add_command(label="How to play",command=howToPlay)
help.add_command(label="Exit",command=root.quit)
menubar.add_cascade(label="Help", menu=help) 
 
root.config(menu=menubar)
 
root.mainloop()
 
