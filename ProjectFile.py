from tkinter import*
from random import shuffle
import random
import string

charSpec = "!@#$%^&*()_+-={}[]:;,./?<>"
charLow = string.ascii_letters.lower()
charUpr = charLow.upper()
charNum = "1234567890"

def specialCharacterAdd(inpStr):
    if(SpecialBool.get() == False) :
        return inpStr
    inpStr += random.choice(charSpec)
    return inpStr

def lowercaseCharacterAdd(inpStr) :
    if(LowerBool.get() == False) :
        return inpStr
    inpStr += random.choice(charLow)
    return inpStr

def uppercaseCharacterAdd(inpStr) :
    if(UpperBool.get() == False) :
        return inpStr
    inpStr += random.choice(charUpr)
    return inpStr

def numAdd(inpStr) :
    if(NumberBool.get() == False) :
        return inpStr
    inpStr += random.choice(charNum)
    return inpStr

def listToString(shuffleList) :
    returnString = ""
    for i in range(len(shuffleList)) :
        returnString += shuffleList[i]
    return returnString

def ErrorHandeling(errorString) :
    SpecialString.set("0")
    LowerString.set("0")
    UpperString.set("0")
    NumberString.set("0")
    LengthString.set("0")
    PasswordString.set("")
    SpecialBool.set(True)
    LowerBool.set(True)
    NumberBool.set(True)
    UpperBool.set(True)
    ErrorString.set("Error : " + errorString)

def CalculateStringLength() :
    try:
        strLen = int(LengthString.get())
        specStrLen = int(SpecialString.get())
        lowStrLen = int(LowerString.get())
        upStrLen = int(UpperString.get())
        numStrLen = int(NumberString.get())
    except ValueError:
        ErrorHandeling("Input needs to be a number!")
        return    
    tempLength = 0

    if(SpecialBool.get() == True) :
        tempLength += specStrLen
    if(LowerBool.get() == True) :
        tempLength += lowStrLen
    if(UpperBool.get() == True) :
        tempLength += upStrLen
    if(NumberBool.get() == True) :
        tempLength += numStrLen

    if(tempLength > int(LengthString.get())) :
        LengthString.set(tempLength)

def generatePassword(var):
    try:
        strLen = int(LengthString.get())
        specStrLen = int(SpecialString.get())
        lowStrLen = int(LowerString.get())
        upStrLen = int(UpperString.get())
        numStrLen = int(NumberString.get())
    except ValueError:
        ErrorHandeling("Input needs to be a number!")
        return

    if(specStrLen + lowStrLen + upStrLen + numStrLen > 50 or strLen > 50) :
        ErrorHandeling("Password length exceeds 50!")
        return

    if(specStrLen < 0 or lowStrLen < 0 or upStrLen < 0 or numStrLen < 0 or strLen < 0) :
        ErrorHandeling("Input can't be a negative number!")
        return
    if(specStrLen == 0 and lowStrLen == 0 and upStrLen == 0 and numStrLen == 0 and strLen == 0) :
        return      

    tempStrLen = strLen
    tempSpecStrLen = specStrLen
    tempLowStrLen = lowStrLen
    tempUpStrLen = upStrLen
    tempNumStrLen = numStrLen

    if(SpecialBool.get() == False) :
        tempSpecStrLen = 0
    if(LowerBool.get() == False) :
        tempLowStrLen = 0
    if(UpperBool.get() == False) :
        tempUpStrLen = 0
    if(NumberBool.get() == False) :
        tempNumStrLen = 0

    finalStr = ""

    if((UpperBool.get() == False) and (LowerBool.get() == False) and (SpecialBool.get() == False) and (NumberBool.get() == False)):
        ErrorHandeling("You need to include a character type!")
        return
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
    #Add number characters to string
    while tempNumStrLen > 0 :
        tempNumStrLen -= 1
        finalStr = numAdd(finalStr)
        
    if tempStrLen > tempSpecStrLen + tempLowStrLen + tempUpStrLen + tempNumStrLen :       
        while len(finalStr) < tempStrLen :
            randInt = random.randrange(0,4)
            if(randInt == 0):
                finalStr = specialCharacterAdd(finalStr)
            elif(randInt == 1):
                finalStr = lowercaseCharacterAdd(finalStr)
            elif(randInt == 2) :
                finalStr = uppercaseCharacterAdd(finalStr)
            else :
                finalStr = numAdd(finalStr)

    #Convert the string into a list
    shuffleList = list(finalStr)
    #Shuffle the list

    random.shuffle(shuffleList)
    #Convert the list into a string
    finalStr = listToString(shuffleList)

    PasswordString.set(finalStr)
    ErrorString.set("")

def LengthCallback(var) :
    try:
        strLen = int(LengthString.get())
        specStrLen = int(SpecialString.get())
        lowStrLen = int(LowerString.get())
        upStrLen = int(UpperString.get())
        numStrLen = int(NumberString.get())
    except ValueError:
        ErrorHandeling("Input needs to be a number!")
        return

    if(specStrLen + lowStrLen + upStrLen + numStrLen > 50 or strLen > 50) :
        ErrorHandeling("Password length exceeds 50!")
        return

    if(specStrLen < 0 or lowStrLen < 0 or upStrLen < 0 or numStrLen < 0 or strLen < 0) :
        ErrorHandeling("Input can't be a negative number!")
        return        

    if(SpecialString.get()=="" or int(SpecialString.get()) < 0 or SpecialBool.get() == False) :
        SpecialString.set("0")
    if(LowerString.get()=="" or int(LowerString.get()) < 0 or LowerBool.get() == False) :
        LowerString.set("0")
    if(UpperString.get()=="" or int(UpperString.get()) < 0 or UpperBool.get() == False) :
        UpperString.set("0")
    if(NumberString.get()=="" or int(NumberString.get()) < 0 or NumberBool.get() == False) :
        NumberString.set("0")
    if(LengthString.get()=="" or int(LengthString.get()) < 0) :
        LengthString.set("0")

    CalculateStringLength()
    
def EntryState(var, index, mode) :
    if SpecialBool.get() == False :
        SpecialEntry.config(state = "disabled")
        SpecialString.set("0")
    else:
        SpecialEntry.config(state = "normal")

    if NumberBool.get() == False :
        NumberEntry.config(state = "disabled")
        NumberString.set("0")
    else:
        NumberEntry.config(state = "normal")

    if UpperBool.get() == False :
        UpperEntry.config(state = "disabled")
        UpperString.set("0")
    else:
        UpperEntry.config(state = "normal")

    if LowerBool.get() == False :
        LowerEntry.config(state = "disabled")
        LowerString.set("0")
    else:
        LowerEntry.config(state = "normal")

root = Tk()
root.title('Password Generator')

window_width = 300
window_height = 200

root.geometry(f"{window_width}x{window_height}")

LengthString = StringVar()
LengthEntry=Entry(root,width=10, textvariable=LengthString)
LengthEntry.insert(0,"0")
LengthEntry.bind('<FocusIn>', LengthCallback)
LengthEntry.bind('<FocusOut>', LengthCallback)

LengthEntry.place(x=115,y=90)

ErrorString = StringVar()
ErrorLabel = Label(root, textvariable=ErrorString)
ErrorLabel.pack(side = BOTTOM)

LengthLabel=Label(root,width=10,text="Length(0-50)")
LengthLabel.place(x=110,y=65)

NumberString = StringVar()
NumberEntry=Entry(root,width=10, textvariable=NumberString)
NumberEntry.insert(0,"0")
NumberEntry.place(x=5,y=25)

NumberLabel=Label(root,width=10,text="Number")
NumberLabel.place(x=0,y=0)
NumberEntry.bind('<FocusOut>', LengthCallback)

NumberBool = IntVar()
NumberBool.set(True)
NumberCheck = Checkbutton(root, text="Include", variable=NumberBool, onvalue=1,
                         offvalue=0)
NumberCheck.place(x=0,y=45)
NumberBool.trace_add('write', EntryState)

SpecialString = StringVar()
SpecialEntry=Entry(root,width=10, textvariable=SpecialString)
SpecialEntry.insert(0,"0")
SpecialEntry.place(x=80,y=25)

SpecialLabel=Label(root,width=10,text="Special")
SpecialLabel.place(x=75,y=0)
SpecialEntry.bind('<FocusOut>', LengthCallback)

SpecialBool = IntVar()
SpecialBool.set(True)
SpecialCheck = Checkbutton(root, text="Include", variable=SpecialBool, onvalue=1,
                         offvalue=0)
SpecialCheck.place(x=75,y=45)
SpecialBool.trace_add('write', EntryState)

LowerString = StringVar()
LowerEntry=Entry(root,width=10, textvariable=LowerString)
LowerEntry.insert(0,"0")
LowerEntry.place(x=155,y=25)

LowerLabel=Label(root,width=10,text="Lower")
LowerLabel.place(x=150,y=0)
LowerEntry.bind('<FocusOut>', LengthCallback)

LowerBool = IntVar()
LowerBool.set(True)
LowerCheck = Checkbutton(root, text="Include", variable=LowerBool, onvalue=1,
                         offvalue=0)
LowerCheck.place(x=150,y=45)
LowerBool.trace_add('write', EntryState)

UpperString = StringVar()
UpperEntry=Entry(root,width=10, textvariable=UpperString)
UpperEntry.insert(0,"0")
UpperEntry.place(x=230,y=25)

UpperLabel=Label(root,width=10,text="Upper")
UpperLabel.place(x=225,y=0)
UpperEntry.bind('<FocusOut>', LengthCallback)

UpperBool = IntVar()
UpperBool.set(True)
UpperCheck = Checkbutton(root, text="Include", variable=UpperBool, onvalue=1,
                         offvalue=0)
UpperCheck.place(x=225,y=45)
UpperBool.trace_add('write', EntryState)

PasswordString = StringVar()
PasswordEntry=Entry(root,width=49, textvariable=PasswordString)
PasswordEntry.place(x=0,y=120)

buttonOne = Button(root, text = "Generate")
buttonOne.pack(side = BOTTOM, ipadx=5, ipady=5)
buttonOne.bind('<ButtonPress>', LengthCallback)
buttonOne.bind('<ButtonRelease>', generatePassword)
root.bind('<Return>', generatePassword)

root.mainloop()
