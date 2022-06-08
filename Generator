from tkinter import*
from random import shuffle
import random
import string

charSpec = "!@#$%^&*()_+-={}[]:;,./?<>"
charLow = string.ascii_letters.lower()
charUpr = charLow.upper()

strLen = 0
specStrLen = 0
lowStrLen = 0
upStrLen = 0

def specialCharacterAdd(inpStr):
    inpStr += random.choice(charSpec)
    return inpStr

def lowercaseCharacterAdd(inpStr) :
    inpStr += random.choice(charLow)
    return inpStr

def uppercaseCharacterAdd(inpStr) :
    inpStr += random.choice(charUpr)
    return inpStr

def numAdd(inpStr) :
    inpStr += random.choice(charNum)
    return inpStr

def listToString(shuffleList) :
    returnString = ""
    for i in range(len(shuffleList)) :
        returnString += shuffleList[i]
    return returnString

def generatePassword():
    global strLen
    global specStrLen
    global lowStrLen
    global upStrLen

    try:
        strLen = int(LengthString.get())
        specStrLen = int(SpecialString.get())
        lowStrLen = int(LowerString.get())
        upStrLen = int(UpperString.get())
    except ValueError:
        print("Error : ValueError")

    tempStrLen = strLen
    tempSpecStrLen = specStrLen
    tempLowStrLen = lowStrLen
    tempUpStrLen = upStrLen
    
    finalStr = ""
    
    print(specStrLen)

    #Check the strLen is lower than the input length
    if tempStrLen < tempSpecStrLen + tempLowStrLen + tempUpStrLen:
      tempStrLen = tempSpecStrLen + tempLowStrLen + tempUpStrLen
      print("Error: Length Shorter than Values Inputed")
      
    #Add special characters to string
    while tempSpecStrLen > 0 :
        tempSpecStrLen -= 1
        finalStr = specialCharacterAdd(finalStr)

    #Add lowercase characters to string
    while tempLowStrLen > 0 :
        tempLowStrLen -= 1
        finalStr = lowercaseCharacterAdd(finalStr)

    #Add uppercase characters to string
    while tempUpStrLen > 0 :
        tempUpStrLen -= 1
        finalStr = uppercaseCharacterAdd(finalStr)

    if tempStrLen > tempSpecStrLen + tempLowStrLen + tempUpStrLen :
        while len(finalStr) < tempStrLen :
            randInt = random.randrange(0,2)
            if(randInt == 0):
                finalStr = specialCharacterAdd(finalStr)
            elif(randInt == 1):
                finalStr = lowercaseCharacterAdd(finalStr)
            else :
                finalStr = uppercaseCharacterAdd(finalStr)

    #Convert the string into a list
    shuffleList = list(finalStr)
    #Shuffle the list

    random.shuffle(shuffleList)
    #Convert the list into a string
    finalStr = listToString(shuffleList)

    PasswordString.set(finalStr)
    
    print("Final String : " + finalStr)
    print(f"String Length : {strLen}")  

def LengthCallback(var, index, mode) :
    global strLen
    global specStrLen
    global lowStrLen
    global upStrLen

    try:
        strLen = int(LengthString.get())
        specStrLen = int(SpecialString.get())
        lowStrLen = int(LowerString.get())
        upStrLen = int(UpperString.get())
    except ValueError:
        print("Error : ValueError")
        
    if(SpecialString.get()=="" or int(SpecialString.get()) < 0) :
        SpecialString.set("0")
    if(LowerString.get()=="" or int(LowerString.get()) < 0) :
        LowerString.set("0")
    if(UpperString.get()=="" or int(UpperString.get()) < 0) :
        UpperString.set("0")
        
    if(int(LengthEntry.get())<specStrLen+lowStrLen+upStrLen) :
        LengthString.set(specStrLen+lowStrLen+upStrLen)
    print(SpecialString.get())

                
root = Tk()
root.title('Password Generator')

window_width = 300
window_height = 200

root.geometry(f"{window_width}x{window_height}")

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

LengthString = StringVar()
LengthEntry=Entry(root,width=10, textvariable=LengthString)
LengthEntry.insert(0,"0")
LengthEntry.place(x=5,y=25)

LengthLabel=Label(root,width=10,text="Length")
LengthLabel.place(x=0,y=0)
LengthString.trace_add('write', LengthCallback)


SpecialString = StringVar()
SpecialEntry=Entry(root,width=10, textvariable=SpecialString)
SpecialEntry.insert(0,"0")
SpecialEntry.place(x=80,y=25)

SpecialLabel=Label(root,width=10,text="Special")
SpecialLabel.place(x=75,y=0)
SpecialString.trace_add('write', LengthCallback)


LowerString = StringVar()
LowerEntry=Entry(root,width=10, textvariable=LowerString)
LowerEntry.insert(0,"0")
LowerEntry.place(x=155,y=25)

LowerLabel=Label(root,width=10,text="Lower")
LowerLabel.place(x=150,y=0)
LowerString.trace_add('write', LengthCallback)


UpperString = StringVar()
UpperEntry=Entry(root,width=10, textvariable=UpperString)
UpperEntry.insert(0,"0")
UpperEntry.place(x=230,y=25)

UpperLabel=Label(root,width=10,text="Upper")
UpperLabel.place(x=225,y=0)
UpperString.trace_add('write', LengthCallback)

PasswordString = StringVar()
PasswordEntry=Entry(root,width=100, textvariable=PasswordString)
PasswordEntry.place(x=0,y=130)

buttonOne = Button(root, text = "Generate", command = generatePassword)
buttonOne.pack(side = BOTTOM, ipadx=5, ipady=5)

root.mainloop()
