import sounddevice as sd
import soundfile as sf
from tkinter import *
def Voice_rec():
    fs = 48000
    duration = 5
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channel=2)
    sd.wait()
    return sf.write('my_audio-file.flac', myrecording, fs)
master = Tk()
Label(master, text=" voice Recorder :").grid(row=0, sticky=W, rowspan=5)
b = Button(master, text="start", command=Voice_rec)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)
mainloop()
