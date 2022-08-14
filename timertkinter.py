from os import startfile, times
from tkinter import *
from tkinter import messagebox
import pygame
#from playsound import playsound
import asyncio



class TimerTk():
    def __init__(self):
        global pygame
        global messagebox
        self.os = __import__("os")
        self.time = __import__("time")
        self.random = __import__("random")
        tkinter = __import__("tkinter")
        self.gui = tkinter.Tk()
        self.gui.title("Timer")
        self.gui.resizable(width=False, height=False)
        self.guipencere = Frame(self.gui)
        self.guipencere.pack(fill="both", expand=True)
        self.main()
        self.gui.mainloop()
        
    def main(self):
        global saatEntry,saatLabel,dakikaEntry,dakikaLabel,saniyeEntry,saniyeLabel,baslatButton
        self.gui.geometry("220x270")
        saatEntry = Entry(self.guipencere)
        saatLabel = Label(self.guipencere, text="Saat")
        dakikaEntry = Entry(self.guipencere)
        dakikaLabel = Label(self.guipencere, text="Dakika")
        saniyeEntry = Entry(self.guipencere)
        saniyeLabel = Label(self.guipencere, text="Saniye")
        baslatButton = Button(self.guipencere, text="Start",font=20,width=10, command=self.Start)
        saatLabel.place(
            x=10,
            y=10)

        saatEntry.place(
            x=70, 
            y=10)

        dakikaLabel.place(
            x=10,
            y=70)

        dakikaEntry.place(
            x=70,
            y=70)

        saniyeLabel.place(
            x=10,
            y=130)

        saniyeEntry.place(
            x=70,
            y=130)

        baslatButton.place(
            x=60,
            y=200
        )

        print(saatEntry.get())

    def checknumeric(self, x):
        if x.isnumeric():
            pass
        else:
            messagebox("Hata", "Tekrar deneyiniz")
    
    def Start(self):
        global saatGet, dakikaGet, saniyeGet
        saatGet = int(saatEntry.get())
        dakikaGet = int(dakikaEntry.get())
        saniyeGet = int(saniyeEntry.get())
        saatEntry.destroy()
        saatLabel.destroy()
        dakikaLabel.destroy()
        dakikaEntry.destroy()
        saniyeLabel.destroy()
        saniyeEntry.destroy()
        baslatButton.destroy()
        self.gui.geometry("160x100")
        asyncio(self.startTimer())
    
    def startTimer(self):
        x = (saatGet*3600)
        b = (dakikaGet*60)
        c = saniyeGet
        saniye = saniyeGet
        saat = saatGet
        dakika = dakikaGet
        for d in range(0, (x+b+c)):
            if saniye == 0:
                if dakika > 1 and saniye == 0:
                    dakika -= 1
                    saniye += 60
                    self.gui.update()
                    if dakika == 0 and saniye > 0:
                        pass
                if dakika == 0 and saniye == 0:
                    saat -= 1
                    dakika +=59
                    saniye += 60
                    self.gui.update()
            saniye -=1
            clock = Label(self.guipencere, text=F"{saat} :",font=10)
            minute = Label(self.guipencere, text=F"{dakika}",font=10)
            seconds = Label(self.guipencere, text=F": {saniye}",font=10)
            clock.place(
                x=50,
                y=30
            )
            minute.place(
                x=70,
                y=30
            )
            seconds.place(
                x=91,
                y=30
            )
            self.time.sleep(1)
            self.gui.update()
        file = "alarm.mp3"
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(0)
        pygame.mixer.music.set_volume(0.3)
        messagebox.showwarning("Warning",f"Sure doldu!")
        self.gui.destroy()
        pygame.mixer.music.stop()
        TimerTk()


TimerTk()