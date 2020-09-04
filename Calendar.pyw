from tkinter import *
from tkinter import messagebox
import datetime
import calendar
import os

root = Tk() #make the window

#get menubar setting
global menub
try:
   menuread = open('./settings/MenuBar.txt', 'r')
   menu = menuread.read()
   if menu != '1' and menu != '0': #if the contents are invalid
      menub = 0 #default it off
      menuwrite = open('./settings/MenuBar.txt', 'w')
      menuwrite.write('0') #default the settings file
   else:
      menub = int(menu)
except: #Makes the setting file if not there
   menub = 0 #default it off
   menuwrite = open('./settings/MenuBar.txt', 'w')
   menuwrite.write('0') #default the settings file
   
      


#get Theme Setting
global color
try:
   colorread = open('./settings/Theme.txt', 'r')
   color = colorread.read()
   if color != 'white' and color != 'black': #if the color is an invalid option
      color = white #default it to white
      colorwrite = open('./settings/Theme.txt', 'w')
      colorwrite.write('white') #default the settings file
except: #Makes the setting file if not there
   color = 'white' #default it to white
   colorwrite = open('./settings/Theme.txt', 'w')
   colorwrite.write('white') #default the settings file



#variables

global mas #mas - mana are just key binds to change the blue highlighted button
mas = 2

global sms
sms = 1

global ssms
ssms = 1

global ses
ses = 1

global sdc
sdc = 1

global swes
swes = 1

global swbs
swbs = 1

global suds
suds = 1

global css
css = 1

global mansa
mansa = 1

global mana
mana = 1

global today #gets todays date
today = datetime.date.today()

global hday #gets a date format for the holiday checker
hday = today.strftime('%m/%d')

global day
day = today.strftime("%B %d, %Y") #gets another format of today

global month
month = today.strftime("%B") #gets the month

global monthl
monthl = month.lower() #gets the month in lowercase

global dayotw
dayotw = calendar.day_name[today.weekday()] #gets day of the week

global dayotwl # gets the day of the week lowercase
dayotwl = dayotw.lower()

global years
years = today.strftime("%Y") #gets the year as a string

global year
year = int(years)#converts to an integer

global numdays #gets the day as a string
numdays = today.strftime("%d")

global numday #converts to an integer
numday = int(numdays)


#gets tommorows day of the week
global dayotwlt

if dayotwl == 'monday':
   dayotwlt = 'tuesday'
if dayotwl == 'tuesday':
   dayotwlt = 'wednesday'
if dayotwl == 'wednesday':
   dayotwlt = 'thursday'
if dayotwl == 'thursday':
   dayotwlt = 'friday'
if dayotwl == 'friday':
   dayotwlt = 'saturday'
if dayotwl == 'saturday':
   dayotwlt = 'sunday'
if dayotwl == 'sunday':
   dayotwlt = 'monday'


#check if it is leap year
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           leap = True
       else:
           leap = False
   else:
       leap = True
else:
   leap = False


#check for current single events
global sef
os.chdir('months')
os.chdir(month)
try:
   re = open("{}.txt".format(numday),"r")
   tsevent = re.read()
   sef = 1
except:
   sef = 0
os.chdir("..")
os.chdir("..")

#check for tommorrows single event
global seft
os.chdir('months')
os.chdir(month)
if monthl == 'january':
   dmax = 31
if monthl == 'february':
   if leap == True:
      dmax = 29
   if leap == False:
      dmax = 28
if monthl == 'march':
   dmax = 31
if monthl == 'april':
   dmax = 30
if monthl == 'may':
   dmax = 31
if monthl == 'june':
   dmax = 30
if monthl == 'july':
   dmax = 31
if monthl == 'august':
   dmax = 31
if monthl == 'september':
   dmax = 30
if monthl == 'october':
   dmax = 31
if monthl == 'november':
   dmax = 30
if monthl == 'december':
   dmax = 31
   
if not numday == dmax:
   try:
      re = open("{}.txt".format(numday+1),"r")
      tsevento = re.read()
      seft = 1
   except:
      seft = 0
   os.chdir("..")
   os.chdir("..")
else:
   os.chdir("..")
   if monthl == 'january':
      os.chdir('February')
   if monthl == 'february':
      os.chdir('March')
   if monthl == 'march':
      os.chdir('April')
   if monthl == 'april':
      os.chdir('May')
   if monthl == 'may':
      os.chdir('June')
   if monthl == 'june':
      os.chdir('July')
   if monthl == 'july':
      os.chdir('August')
   if monthl == 'august':
      os.chdir('September')
   if monthl == 'september':
      os.chdir('October')
   if monthl == 'october':
      os.chdir('November')
   if monthl == 'november':
      os.chdir('December')
   if monthl == 'december':
      os.chdir('January')
   try:
      re = open("1.txt","r")
      tsevento = re.read()
      seft = 1
   except:
      seft = 0
   os.chdir("..")
   os.chdir("..")


#delete yesterdays single event
os.chdir('months')
os.chdir(month)
delmax = numday - 1
if numday == 0:
   os.chdir("..")
   if month == 'January':
      os.chdir('December')
      delmax = 31
   if month == 'February':
      os.chdir('January')
      delmax = 31
   if month == 'March':
      os.chdir('February')
      if leap == True:
         delmax = 29
      if leap == False:
         delmax = 28
   if month == 'April':
      os.chdir('March')
      delmax = 31
   if month == 'May':
      os.chdir('April')
      delmax = 30
   if month == 'June':
      os.chdir('May')
      delmax = 31
   if month == 'July':
      os.chdir('June')
      delmax = 30
   if month == 'August':
      os.chdir('July')
      delmax = 31
   if month == 'September':
      os.chdir('August')
      delmax = 31
   if month == 'October':
      os.chdir('September')
      delmax = 30
   if month == 'November':
      os.chdir('October')
      delmax = 31
   if month == 'December':
      os.chdir('November')
      delmax = 30
try:
   os.remove('{}.txt'.format(delmax))
   os.chdir("..")
   os.chdir("..")
except:
   os.chdir("..")
   os.chdir("..")

#check for a weekly event
global wef
os.chdir('week')
try:
   re = open("{}.txt".format(dayotwl),"r")
   twevent = re.read()
   wef = 1
except:
   wef = 0
os.chdir("..")

#check for tommorrows weekly event
global weft
os.chdir('week')
try:
   re = open("{}.txt".format(dayotwlt),"r")
   twevento = re.read()
   weft = 1
except:
   weft = 0
os.chdir("..")

#These events are not automatically deleted, you can remove them in manage

#check for a yearly event
global yef
os.chdir('year')
os.chdir(month)
try:
   re = open("{}.txt".format(numday),"r")
   tyevent = re.read()
   yef = 1
except:
   yef = 0
os.chdir("..")
os.chdir("..")
#These events are not automatically deleted, you can remove them in manage

#check for tommorrows yearly event
global yeft
os.chdir('year')
os.chdir(month)
if monthl == 'january':
   dmax = 31
if monthl == 'february':
   if leap == True:
      dmax = 29
   if leap == False:
      dmax = 28
if monthl == 'march':
   dmax = 31
if monthl == 'april':
   dmax = 30
if monthl == 'may':
   dmax = 31
if monthl == 'june':
   dmax = 30
if monthl == 'july':
   dmax = 31
if monthl == 'august':
   dmax = 31
if monthl == 'september':
   dmax = 30
if monthl == 'october':
   dmax = 31
if monthl == 'november':
   dmax = 30
if monthl == 'december':
   dmax = 31
   
if not numday == dmax:
   try:
      re = open("{}.txt".format(numday+1),"r")
      tyevento = re.read()
      yeft = 1
   except:
      yeft = 0
   os.chdir("..")
   os.chdir("..")
else:
   os.chdir("..")
   if monthl == 'january':
      os.chdir('February')
   if monthl == 'february':
      os.chdir('March')
   if monthl == 'march':
      os.chdir('April')
   if monthl == 'april':
      os.chdir('May')
   if monthl == 'may':
      os.chdir('June')
   if monthl == 'june':
      os.chdir('July')
   if monthl == 'july':
      os.chdir('August')
   if monthl == 'august':
      os.chdir('September')
   if monthl == 'september':
      os.chdir('October')
   if monthl == 'october':
      os.chdir('November')
   if monthl == 'november':
      os.chdir('December')
   if monthl == 'december':
      os.chdir('January')
   try:
      re = open("1.txt","r")
      tsevento = re.read()
      yeft = 1
   except:
      yeft = 0
   os.chdir("..")
   os.chdir("..")


#get mothers day date
global mdate
mdate = 'a' #make mdate mean something
hnumber = 1
while mdate.lower() != 'sunday': #while the weeekday is not sunday
   mdatent = datetime.date(year, 5, hnumber)
   mdaten = mdatent.weekday()
   mdate = calendar.day_name[mdaten] #get weekday
   if mdate.lower() != 'sunday':
      hnumber = hnumber + 1 #next day

hnumber = hnumber + 7 #add 7 because mothers day is on the second sunday
if hnumber < 10:
   mdate = '05/0{}'.format(hnumber) #adds a 0 in front if it is less then 10
else:
   mdate = '05/{}'.format(hnumber)#adds no zero


#get thanksgiving day date
global tdate
tdate = 'a' #make tdate mean something
hnumber = 1
while tdate.lower() != 'thursday': #while the weeekday is not thursday
   tdatent = datetime.date(year, 11, hnumber)
   tdaten = tdatent.weekday()
   tdate = calendar.day_name[tdaten] #get weekday
   if tdate.lower() != 'thursday':
      hnumber = hnumber + 1 #next day

hnumber = hnumber + 21 #add 21 because thanksgiving day is on the fourth thursday

tdate = '11/{}'.format(hnumber)#gets final date


#get fathers day date
global fdate
fdate = 'a' #make fdate mean something
hnumber = 1
while fdate.lower() != 'sunday': #while the weeekday is not sunday
   fdatent = datetime.date(year, 6, hnumber)
   fdaten = fdatent.weekday()
   fdate = calendar.day_name[fdaten] #get weekday
   if fdate.lower() != 'sunday':
      hnumber = hnumber + 1 #next day

hnumber = hnumber + 14 #add 14 because fathers day is on the third sunday

fdate = '06/{}'.format(hnumber)#gets final date


#get columbus day date
global cdate
cdate = 'a' #make cdate mean something
hnumber = 1
while cdate.lower() != 'monday': #while the weeekday is not monday
   cdatent = datetime.date(year, 10, hnumber)
   cdaten = cdatent.weekday()
   cdate = calendar.day_name[cdaten] #get weekday
   if cdate.lower() != 'monday':
      hnumber = hnumber + 1 #next day

hnumber = hnumber + 7 #add 7 because columbus day is on the second monday


if hnumber < 10:
   cdate = '10/0{}'.format(hnumber) #adds a 0 in front if it is less then 10
else:
   cdate = '10/{}'.format(hnumber)#adds no zero


#get holidays
global holiday
holiday = 'a'
if hday == '01/01':
   holiday = "New Year's Day"
if hday == '01/20':
   holiday = "Martin Luther King Day"
if hday == '02/02':
   holiday = "Groundhog day"
if hday == '02/14':
   holiday = "Valentines Day"
if hday == '02/17':
   holiday = "Presidents Day"
if hday == '03/17':
   holiday = "Saint Paatrick's Day"
if hday == '05/05':
   holiday = "Cinco de Mayo"
if hday == mdate:
   holiday = "Mother's Day"
if hday == '05/25':
   holiday = "Memorial Day"
if hday == fdate:
   holiday = "Father's Day"
if hday == '07/04':
   holiday = "Independence Day"
if hday == '09/07':
   holiday = "Labor Day"
if hday == cdate:
   holiday = "Columbus Day"
if hday == '10/31':
   holiday = "Halloween"
if hday == '11/11':
   holiday = "Veteran's Day"
if hday == tdate:
   holiday = "Thanksgiving Day"
if hday == '12/24':
   holiday = "Christmas Eve"
if hday == '12/25':
   holiday = "Christmas Day"
if hday == '12/31':
   holiday = "New Year's Eve"




def dayi():
    global day, cday, weekdl, dback, sef, dayil, wef, tseventil, yef, tseventilt, holidayl
    root.unbind("<KeyPress-Left>")
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Down>")
    if menub == 1:
       emptyMenu = Menu(root)
       root.config(menu=emptyMenu)
    neweb.place_forget()
    dayib.place_forget()
    maneb.place_forget()
    exitb.place_forget()
    helpb.place_forget()
    setb.place_forget()
    root.bind("<Return>", lambda e: dayback())
    dayil = Label(text = "Daily Info:", fg = "blue", bg = color, font = ("arial", 30))
    dayil.place(relx = .5, rely = .25, anchor="center")
    cday = Label(root, bg = color, fg = "blue", text = day, font = ("arial", 20))
    cday.place(relx=.5, rely=.4, anchor=  'center')
    weekdl = Label(root, bg = color, fg = "blue", text = dayotw, font = ("arial", 20))
    weekdl.place(relx =.5, rely=.5, anchor = "center")
    tseventil = Label(text = "Events:", bg = color, fg = "blue", font = ("arial", 20))
    tseventil.place(relx = .2, rely = .6, anchor="center")
    tseventilt = Label(text = "Tomorrows Events:", bg = color, fg = "blue", font = ("arial", 20))
    tseventilt.place(relx = .5, rely = .6, anchor="center")
    holidayl = Label(text = "Holidays:", bg = color, fg = "blue", font = ("arial", 20))
    holidayl.place(relx = .8, rely = .6, anchor="center")
    if sef == 1:
       global tseventl   
       tseventl = Label(text = tsevent, bg = color, fg = "blue", font = ("arial", 15))
       tseventl.place(relx = .2, rely = .65, anchor="center")
    if wef == 1:
       global tweventl   
       tweventl = Label(text = twevent, bg = color, fg = "blue", font = ("arial", 15))
       tweventl.place(relx = .2, rely = .7, anchor="center")
    if yef == 1:
       global tyeventl   
       tyeventl = Label(text = tyevent, bg = color, fg = "blue", font = ("arial", 15))
       tyeventl.place(relx = .2, rely = .75, anchor="center")
    if sef == 0 and wef == 0 and yef == 0:
       global noeventb
       noeventb = Label(text = 'No Active Events', bg = color, fg = "blue", font = ("arial", 15))
       noeventb.place(relx = .2, rely = .65, anchor="center")
    if seft == 1:
       global tseventlo   
       tseventlo = Label(text = tsevento, bg = color, fg = "blue", font = ("arial", 15))
       tseventlo.place(relx = .5, rely = .65, anchor="center")
    if weft == 1:
       global tweventlo   
       tweventlo = Label(text = twevento, bg = color, fg = "blue", font = ("arial", 15))
       tweventlo.place(relx = .5, rely = .7, anchor="center")
    if yeft == 1:
       global tyeventlo   
       tyeventlo = Label(text = tyevento, bg = color, fg = "blue", font = ("arial", 15))
       tyeventlo.place(relx = .5, rely = .75, anchor="center")
    if seft == 0 and weft == 0 and yeft == 0:
       global noeventbo
       noeventbo = Label(text = 'No Active Events', bg = color, fg = "blue", font = ("arial", 15))
       noeventbo.place(relx = .5, rely = .65, anchor="center")
    if holiday == 'a':
       global noholidayl
       noholidayl = Label(text = 'No Holidays', bg = color, fg = "blue", font = ("arial", 15))
       noholidayl.place(relx = .8, rely = .65, anchor="center")
    else:
       holidayl = Label(text = holiday, bg = color, fg = "blue", font = ("arial", 15))
       holidayl.place(relx = .8, rely = .7, anchor="center")

    dback = Button(root, bg = "blue", fg = "light grey", text = "Back", font = ("arial", 15), command = dayback)
    dback.place(relx=.5, rely=.8, anchor="center")
    
def dayback():
    global sef
    root.bind("<Return>", lambda e: dayi())
    root.bind("<KeyPress-Left>", lambda e: mainarrowl())
    root.bind("<KeyPress-Right>", lambda e: mainarrowr())
    root.bind("<KeyPress-Down>", lambda e: mainarrowd())
    root.bind("<KeyPress-Up>", lambda e: mainarrowu())
    cday.place_forget()
    weekdl.place_forget()
    dback.place_forget()
    dayil.place_forget()
    if menub == 1:
       root.config(menu=menubar)
    exitb.place(relx = .65, rely = .7, anchor = 'center')
    helpb.place(relx = .5, rely = .7, anchor = 'center')
    neweb.place(relx=.5, rely=.5, anchor="center")
    dayib.place(relx=.3, rely=.5, anchor="center")
    maneb.place(relx=.7, rely=.5, anchor="center")
    setb.place(relx = .35, rely = .7, anchor = 'center')
    tseventil.place_forget()
    tseventilt.place_forget()
    holidayl.place_forget()
    if sef == 1:
       tseventl.place_forget()
    if wef == 1:
       tweventl.place_forget()
    if yef == 1:
       tyeventl.place_forget()
    if sef == 0 and wef == 0 and yef == 0:
       noeventb.place_forget()
    if seft == 1:
       tseventlo.place_forget()
    if weft == 1:
       tweventlo.place_forget()
    if yeft == 1:
       tyeventl.place_forget()
    if seft == 0 and weft == 0 and yeft == 0:
       noeventbo.place_forget()
    if holiday == 'a':
       noholidayl.place_forget()
    else:
       holidayl.place_forget()

def seth():
    global sety, setw, seto, setback, newlogol
    if menub == 1:
       emptyMenu = Menu(root)
       root.config(menu=emptyMenu)
    root.unbind("<KeyPress-Left>")
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Down>")
    neweb.place_forget()
    dayib.place_forget()
    maneb.place_forget()
    logol.pack_forget()
    exitb.place_forget()
    helpb.place_forget()
    setb.place_forget()
    newlogol = Label(root, image = newlogopic, bg = color)
    newlogol.pack(side = TOP, fill = X)
    seto = Button(root, bg = "blue", fg = "Light Grey", font = ("arial", 15), text = "Single Event", command = setnewn)
    seto.place(relx=.5, rely=.3, anchor="center")
    sety = Button(root, fg = "blue", bg = "Light Grey", font = ("arial", 15), text = "Yearly Event", command = setyf)
    sety.place(relx=.5, rely=.4, anchor="center")
    setw = Button(root, fg = "blue", bg = "Light Grey", font = ("arial", 15), text = "Weekly Event", command = setwf)
    setw.place(relx=.5, rely=.5, anchor="center")
    setback = Button(root, fg = "blue", bg = "Light Grey", font = ("arial", 15), text = "Back", command = setbackf)
    setback.place(relx=.5, rely=.6, anchor="center")
    root.bind("<KeyPress-Up>", lambda e: setarrowu())
    root.bind("<KeyPress-Down>", lambda e: setarrowd())
    root.bind("<Return>", lambda e: setnewn())

def setyf():
    global singli, singlme, ssms, subsing, singra, singla, singback, ses
    ssms = 1
    ses = 1
    seto.place_forget()
    sety.place_forget()
    setw.place_forget()
    setback.place_forget()
    root.unbind("<KeyPress-Down>")
    root.unbind("<KeyPress-Up>")
    singli = Label(text = "Choose Your Yearly Event Month:", font = ("airal", 20), bg = color, fg = "blue")
    singli.place(relx = .5, rely = .2, anchor="center")
    singlme = Entry(root, exportselection=0, width = 12, font = ("arial", 15), fg = "Blue", relief = RAISED, bd = 10)
    singlme.place(relx = .5, rely = .4, anchor="center")
    singlme.insert(0, "January")
    subsing = Button(root, text = "Next", font = ("arial", 15), bg = "blue", fg = "light grey", command = setnsday)
    subsing.place(relx = .5, rely = .5, anchor="center")
    singra = Button(root, image = rightapic2, bg = color, relief = FLAT, command = singmar)
    singra.place(relx = .7, rely = .4, anchor="center")
    singla = Button(root, image = leftapic2, bg = color, relief = FLAT, command = singmal)
    singla.place(relx = .3, rely = .4, anchor="center")
    singback = Button(root, text = "Back", font = ("arial", 15), fg = "blue", bg = "light grey", command = setyback)
    singback.place(relx = .5, rely = .6, anchor="center")
    root.bind("<KeyPress-Left>", lambda e: singmal())
    root.bind("<KeyPress-Right>", lambda e: singmar())
    root.bind("<KeyPress-Down>", lambda e: setyad())
    root.bind("<KeyPress-Up>", lambda e: setyau())
    root.bind("<Return>", lambda e: setydc())

def setyback():
    global ssms
    ssms = 1
    root.unbind("<KeyPress-Down>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Left>")
    root.bind("<Return>", lambda e: setyf())
    singli.place_forget()
    singlme.place_forget()
    subsing.place_forget()
    singra.place_forget()
    singla.place_forget()
    singback.place_forget()
    seto.place(relx=.5, rely=.3, anchor="center")
    sety.place(relx=.5, rely=.4, anchor="center")
    setw.place(relx=.5, rely=.5, anchor="center")
    setback.place(relx=.5, rely=.6, anchor="center")
    root.bind("<KeyPress-Up>", lambda e: setarrowu())
    root.bind("<KeyPress-Down>", lambda e: setarrowd())

def setyfd():
    global dmax, sdc, ses
    sdc = 1
    singli.config(text = "Choose Your Yearly Event Day:")
    singlme.delete(0, END)
    singlme.insert(0, '1')
    singra.config(command = setdaycr)
    singla.config(command = setdaycl)
    singback.config(command = setydback)
    subsing.config(command = setydf)
    root.bind("<Return>", lambda e: setydf())
    root.bind("<KeyPress-Right>", lambda e: setdaycr())
    root.bind("<KeyPress-Left>", lambda e: setdaycl())
    root.bind("<KeyPress-Down>", lambda e: setysadt())
    root.bind("<KeyPress-Up>", lambda e: setysaut())

def setydf():
   global dmax, sdc, ses, dinput
   ses = 1
   sdc = 1
   dinputs = singlme.get()
   try:
      dinput = int(dinputs)
      if dinput <= 0:
         singlme.delete(0, END)
         singlme.insert(0, "Invalid Day")
      elif dinput >= dmax:
         singlme.delete(0, END)
         singlme.insert(0, "Invalid Day")
      else:
         setyff()
   except:
      singlme.delete(0, END)
      singlme.insert(0, "Invalid Day")

def setyff():
   global ses
   ses = 1
   singra.place_forget()
   singla.place_forget()
   singli.config(text = "Write Your Yearly Event Name:")
   root.unbind("<KeyPress-Right>")
   root.unbind("<KeyPress-Left>")
   root.bind("<Return>", lambda e: setysub())
   root.bind("<KeyPress-Down>", lambda e: setysadth())
   root.bind("<KeyPress-Up>", lambda e: setysauth())
   singlme.delete(0, END)
   singlme.config(width = 20)
   subsing.config(command = setysub)
   singback.config(command = setyfback)

def setysub():
   global feinfo, event, dinput, yef, tyevent
   event = singlme.get()
   singlme.delete(0, END)
   singlme.place_forget()
   singli.config(text = "You are finished!")
   feinfo = Label(root, text = "To change this yearly event or see event info, go to manage", bg = color, fg = "blue", font = ("arial", 12))
   feinfo.place(relx = .5, rely = .4, anchor='center')
   singback.place_forget()
   ne = open("{}.txt".format(dinput),"w")
   ne.write(event)
   ne.close()
   os.chdir("..")
   os.chdir("..")
   subsing.config(text = "Continue")
   subsing.config(command = setysubback)
   root.bind("<Return>", lambda e: setysubback())
   os.chdir('year')
   os.chdir(month)
   try:
      re = open("{}.txt".format(numday),"r")
      tyevent = re.read()
      yef = 1
   except:
      yef = 0
   os.chdir("..")
   os.chdir("..")

def setysubback():
   subsing.place_forget()
   singli.place_forget()
   feinfo.place_forget()
   root.bind("<KeyPress-Up>", lambda e: setarrowu())
   root.bind("<KeyPress-Down>", lambda e: setarrowd())
   root.bind("<Return>", lambda e: setyf())
   seto.place(relx=.5, rely=.3, anchor="center")
   sety.place(relx=.5, rely=.4, anchor="center")
   setw.place(relx=.5, rely=.5, anchor="center")
   setback.place(relx=.5, rely=.6, anchor="center")

def setyfback():
   global dmax, sdc, ses
   singlme.config(width = 12)
   singlme.delete(0, END)
   singli.config(text = "Choose Your Day:")
   sdc = 1
   ses = 2
   singlme.insert(0, '1')
   singra.config(command = setdaycr)
   singla.config(command = setdaycl)
   singback.config(command = setydback)
   subsing.config(command = setydf)
   root.bind("<Return>", lambda e: setnewndback())
   root.bind("<KeyPress-Right>", lambda e: setdaycr())
   root.bind("<KeyPress-Left>", lambda e: setdaycl())
   root.bind("<KeyPress-Down>", lambda e: setysadt())
   root.bind("<KeyPress-Up>", lambda e: setysaut())
   singra.place(relx = .7, rely = .4, anchor="center")
   singla.place(relx = .3, rely = .4, anchor="center")

def setysadth():
    global ses
    ses = ses + 1
    if ses == 3:
        ses = ses - 1
    if ses == 0:
        ses = ses + 1
    if ses == 1:
        subsing.config(bg = "Blue", fg = "light grey")
        singback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setysub())
    if ses == 2:
        subsing.config(fg = "Blue", bg = "light grey")
        singback.config(bg = "blue", fg = "light grey")
        root.bind("<Return>", lambda e: setyfback())

def setysauth():
    global ses
    ses = ses - 1
    if ses == 3:
        ses = ses - 1
    if ses == 0:
        ses = ses + 1
    if ses == 1:
        subsing.config(bg = "Blue", fg = "light grey")
        singback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setysub())
    if ses == 2:
        subsing.config(fg = "Blue", bg = "light grey")
        singback.config(bg = "blue", fg = "light grey")
        root.bind("<Return>", lambda e: setyfback())

def setydback():
   global ssms, ses
   os.chdir("..")
   os.chdir("..")
   ssms = 1
   ses = 2
   singlme.delete(0, END)
   singlme.insert(0, 'January')
   singli.config(text = "Choose Your Month:")
   singback.config(command = setnewnback)
   singra.config(command = singmar)
   singra.config(command = singmal)
   subsing.config(command = setnsday)
   root.bind("<KeyPress-Left>", lambda e: singmal())
   root.bind("<KeyPress-Right>", lambda e: singmar())
   root.bind("<KeyPress-Down>", lambda e: setyad())
   root.bind("<KeyPress-Up>", lambda e: setyau())
   root.bind("<Return>", lambda e: setyback())

def setysadt():
    global ses
    ses = ses + 1
    if ses == 3:
        ses = ses - 1
    if ses == 0:
        ses = ses + 1
    if ses == 1:
        subsing.config(bg = "Blue", fg = "light grey")
        singback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setydf())
    if ses == 2:
        subsing.config(fg = "Blue", bg = "light grey")
        singback.config(bg = "blue", fg = "light grey")
        root.bind("<Return>", lambda e: setydback())

def setysaut():
    global ses
    ses = ses - 1
    if ses == 3:
        ses = ses - 1
    if ses == 0:
        ses = ses + 1
    if ses == 1:
        subsing.config(bg = "Blue", fg = "light grey")
        singback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setydf())
    if ses == 2:
        subsing.config(fg = "Blue", bg = "light grey")
        singback.config(bg = "blue", fg = "light grey")
        root.bind("<Return>", lambda e: setydback())

def setydc():
    global ses, ssms, dmax, leap
    ses = 1
    ssms = 1
    minputs = singlme.get()
    minput = minputs.lower()
    if minput == 'january':
        dmax = 32
        os.chdir('year')
        os.chdir('January')
        setyfd()
    elif minput == 'february':
        dmax = 30
        os.chdir('year')
        os.chdir('February')
        setyfd()
    elif minput == 'march':
        dmax = 32
        os.chdir('year')
        os.chdir('March')
        setyfd()
    elif minput == 'april':
        dmax = 31
        os.chdir('year')
        os.chdir('April')
        setyfd()
    elif minput == 'may':
        dmax = 32
        os.chdir('year')
        os.chdir('May')
        setyfd()
    elif minput == 'june':
        dmax = 31
        os.chdir('year')
        os.chdir('June')
        setyfd()
    elif minput == 'july':
        dmax = 32
        os.chdir('year')
        os.chdir('July')
        setyfd()
    elif minput == 'august':
        dmax = 32
        os.chdir('year')
        os.chdir('August')
        setyfd()
    elif minput == 'september':
        dmax = 31
        os.chdir('year')
        os.chdir('September')
        setyfd()
    elif minput == 'october':
        dmax = 32
        os.chdir('year')
        os.chdir('October')
        setyfd()
    elif minput == 'november':
        dmax = 31
        os.chdir('year')
        os.chdir('November')
        setyfd()
    elif minput == 'december':
        dmax = 32
        os.chdir('year')
        os.chdir('December')
        setyfd()
    else:
        singlme.delete(0, END)
        singlme.insert(0, "Invalid Month")

def setyad():
    global ses
    ses = ses + 1
    if ses == 3:
        ses = ses - 1
    if ses == 0:
        ses = ses + 1
    if ses == 1:
        subsing.config(bg = "Blue", fg = "light grey")
        singback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setydc())
    if ses == 2:
        subsing.config(fg = "Blue", bg = "light grey")
        singback.config(bg = "blue", fg = "light grey")
        root.bind("<Return>", lambda e: setyback())

def setyau():
    global ses
    ses = ses - 1
    if ses == 3:
        ses = ses - 1
    if ses == 0:
        ses = ses + 1
    if ses == 1:
        subsing.config(bg = "Blue", fg = "light grey")
        singback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setydc())
    if ses == 2:
        subsing.config(fg = "Blue", bg = "light grey")
        singback.config(bg = "blue", fg = "light grey")
        root.bind("<Return>", lambda e: setyback())

def setwf():
    global singli, singlme, subsing, singra, singla, singback, swes, swbs
    swes = 1
    swbs = 1
    seto.place_forget()
    sety.place_forget()
    setw.place_forget()
    setback.place_forget()
    root.unbind("<KeyPress-Down>")
    root.unbind("<KeyPress-Up>")
    singli = Label(text = "Choose Your Day:", font = ("airal", 20), bg = color, fg = "blue")
    singli.place(relx = .5, rely = .2, anchor="center")
    singlme = Entry(root, exportselection=0, width = 12, font = ("arial", 15), fg = "Blue", relief = RAISED, bd = 10)
    singlme.place(relx = .5, rely = .4, anchor="center")
    singlme.insert(0, "Sunday")
    subsing = Button(root, text = "Next", font = ("arial", 15), bg = "blue", fg = "light grey", command = setwnext)
    subsing.place(relx = .5, rely = .5, anchor="center")
    singra = Button(root, image = rightapic2, bg = color, relief = FLAT, command = setwwsr)
    singra.place(relx = .7, rely = .4, anchor="center")
    singla = Button(root, image = leftapic2, bg = color, relief = FLAT, command = setwwsl)
    singla.place(relx = .3, rely = .4, anchor="center")
    singback = Button(root, text = "Back", font = ("arial", 15), fg = "blue", bg = "light grey", command = setwback)
    singback.place(relx = .5, rely = .6, anchor="center")
    root.bind("<KeyPress-Left>", lambda e: setwwsl())
    root.bind("<KeyPress-Right>", lambda e: setwwsr())
    root.bind("<KeyPress-Down>", lambda e: setwarrowd())
    root.bind("<KeyPress-Up>", lambda e: setwarrowu())
    root.bind("<Return>", lambda e: setwnext())

def setwnext():
   global winput
   winputs = singlme.get()
   winput = winputs.lower()
   singlme.delete(0, END)
   if winput.lower() == "monday" or winput.lower() == 'tuesday' or winput.lower() == 'wednesday' or winput.lower() == 'thursday' or winput.lower() == 'friday' or winput.lower() == 'saturday' or winput.lower() == 'sunday':      
      setwe()
   else:
      singlme.insert(0, 'Invalid Day')

def setwe():
   global swbs
   swbs = 1
   singlme.config(width = 20)
   singra.place_forget()
   singla.place_forget()
   root.unbind("<KeyPress-Left>")
   root.unbind("<KeyPress-Right>")
   root.bind("<Return>", lambda e: setwnef())
   root.bind("<KeyPress-Down>", lambda e: setwarrowdt())
   root.bind("<KeyPress-Up>", lambda e: setwarrowut())
   singli.config(text = "Write Your Event Name:")
   singback.config(command = setwebackt)
   subsing.config(command = setwnef)


def setwnef():
   global feinfo, event, dinput, wef, twevent
   event = singlme.get()
   singlme.delete(0, END)
   singlme.place_forget()
   singli.config(text = "You are finished!")
   feinfo = Label(root, text = "To change this event or see event info, go to manage", bg = color, fg = "blue", font = ("arial", 12))
   feinfo.place(relx = .5, rely = .4, anchor='center')
   singback.place_forget()
   os.chdir('week')
   ne = open("{}.txt".format(winput),"w")
   ne.write(event)
   os.chdir("..")
   subsing.config(text = "Continue")
   subsing.config(command = setfsubback)
   root.bind("<Return>", lambda e: setfsubback())
   os.chdir('week')
   try:
      re = open("{}.txt".format(dayotwl),"r")
      twevent = re.read()
      wef = 1
   except:
      wef = 0
   os.chdir("..")
   

def setfsubback():
   subsing.place_forget()
   singli.place_forget()
   feinfo.place_forget()
   root.bind("<KeyPress-Up>", lambda e: setarrowu())
   root.bind("<KeyPress-Down>", lambda e: setarrowd())
   root.bind("<Return>", lambda e: setwf())
   seto.place(relx=.5, rely=.3, anchor="center")
   sety.place(relx=.5, rely=.4, anchor="center")
   setw.place(relx=.5, rely=.5, anchor="center")
   setback.place(relx=.5, rely=.6, anchor="center")

def setwebackt():
    swes = 1
    swbs = 1
    root.unbind("<KeyPress-Down>")
    root.unbind("<KeyPress-Up>")
    singli.config(text = "Choose Your Day:")
    singlme.config(width = 12)
    singlme.insert(0, "Sunday")
    subsing.config(command = setwnext)
    singra.place(relx = .7, rely = .4, anchor="center")
    singla.place(relx = .3, rely = .4, anchor="center")
    singback.config(command = setwback)
    root.bind("<KeyPress-Left>", lambda e: setwwsl())
    root.bind("<KeyPress-Right>", lambda e: setwwsr())
    root.bind("<KeyPress-Down>", lambda e: setwarrowd())
    root.bind("<KeyPress-Up>", lambda e: setwarrowu())
    root.bind("<Return>", lambda e: setwback())

def setwarrowdt():
    global swbs
    swbs = swbs + 1
    if swbs == 3:
        swbs = swbs - 1
    if swbs == 0:
        swbs = swbs + 1
    if swbs == 1:
        subsing.config(bg = "Blue", fg = "light grey")
        singback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setwnef())
    if swbs == 2:
        subsing.config(fg = "Blue", bg = "light grey")
        singback.config(bg = "blue", fg = "light grey")
        root.bind("<Return>", lambda e: setwebackt())

def setwarrowut():
    global swbs
    swbs = swbs - 1
    if swbs == 3:
        swbs = swbs - 1
    if swbs == 0:
        swbs = swbs + 1
    if swbs == 1:
        subsing.config(bg = "Blue", fg = "light grey")
        singback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setwnef())
    if swbs == 2:
        subsing.config(fg = "Blue", bg = "light grey")
        singback.config(bg = "blue", fg = "light grey")
        root.bind("<Return>", lambda e: setwebackt())

def setwarrowd():
    global swbs
    swbs = swbs + 1
    if swbs == 3:
        swbs = swbs - 1
    if swbs == 0:
        swbs = swbs + 1
    if swbs == 1:
        subsing.config(bg = "Blue", fg = "light grey")
        singback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setwnext())
    if swbs == 2:
        subsing.config(fg = "Blue", bg = "light grey")
        singback.config(bg = "blue", fg = "light grey")
        root.bind("<Return>", lambda e: setwback())

def setwarrowu():
    global swbs
    swbs = swbs - 1
    if swbs == 3:
        swbs = swbs - 1
    if swbs == 0:
        swbs = swbs + 1
    if swbs == 1:
        subsing.config(bg = "Blue", fg = "light grey")
        singback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setwnext())
    if swbs == 2:
        subsing.config(fg = "Blue", bg = "light grey")
        singback.config(bg = "blue", fg = "light grey")
        root.bind("<Return>", lambda e: setwback())

def setwback():
    global ssms
    ssms = 1
    root.unbind("<KeyPress-Down>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Left>")
    root.bind("<Return>", lambda e: setwf())
    singli.place_forget()
    singlme.place_forget()
    subsing.place_forget()
    singra.place_forget()
    singla.place_forget()
    singback.place_forget()
    seto.place(relx=.5, rely=.3, anchor="center")
    sety.place(relx=.5, rely=.4, anchor="center")
    setw.place(relx=.5, rely=.5, anchor="center")
    setback.place(relx=.5, rely=.6, anchor="center")
    root.bind("<KeyPress-Up>", lambda e: setarrowu())
    root.bind("<KeyPress-Down>", lambda e: setarrowd())

def setwwsr():
    global swes
    swes = swes + 1
    if swes == 0:
        swes = swes + 1
    if swes == 8:
        swes = swes - 1
    if swes == 1:
        singlme.delete(0, END)
        singlme.insert(0, "Sunday")
    if swes == 2:
        singlme.delete(0, END)
        singlme.insert(0, "Monday")
    if swes == 3:
        singlme.delete(0, END)
        singlme.insert(0, "Tuesday")
    if swes == 4:
        singlme.delete(0, END)
        singlme.insert(0, "Wednesday")
    if swes == 5:
        singlme.delete(0, END)
        singlme.insert(0, "Thursday")
    if swes == 6:
        singlme.delete(0, END)
        singlme.insert(0, "Friday")
    if swes == 7:
        singlme.delete(0, END)
        singlme.insert(0, "Saturday")

def setwwsl():
    global swes
    swes = swes - 1
    if swes == 0:
        swes = swes + 1
    if swes == 8:
        swes = swes - 1
    if swes == 1:
        singlme.delete(0, END)
        singlme.insert(0, "Sunday")
    if swes == 2:
        singlme.delete(0, END)
        singlme.insert(0, "Monday")
    if swes == 3:
        singlme.delete(0, END)
        singlme.insert(0, "Tuesday")
    if swes == 4:
        singlme.delete(0, END)
        singlme.insert(0, "Wednesday")
    if swes == 5:
        singlme.delete(0, END)
        singlme.insert(0, "Thursday")
    if swes == 6:
        singlme.delete(0, END)
        singlme.insert(0, "Friday")
    if swes == 7:
        singlme.delete(0, END)
        singlme.insert(0, "Saturday")

def setnewn():
    global singli, singlme, ssms, subsing, singra, singla, singback, ses
    ssms = 1
    ses = 1
    seto.place_forget()
    sety.place_forget()
    setw.place_forget()
    setback.place_forget()
    root.unbind("<KeyPress-Down>")
    root.unbind("<KeyPress-Up>")
    singli = Label(text = "Choose Your Month:", font = ("airal", 20), bg = color, fg = "blue")
    singli.place(relx = .5, rely = .2, anchor="center")
    singlme = Entry(root, exportselection=0, width = 12, font = ("arial", 15), fg = "Blue", relief = RAISED, bd = 10)
    singlme.place(relx = .5, rely = .4, anchor="center")
    singlme.insert(0, "January")
    subsing = Button(root, text = "Next", font = ("arial", 15), bg = "blue", fg = "light grey", command = setnsday)
    subsing.place(relx = .5, rely = .5, anchor="center")
    singra = Button(root, image = rightapic2, bg = color, relief = FLAT, command = singmar)
    singra.place(relx = .7, rely = .4, anchor="center")
    singla = Button(root, image = leftapic2, bg = color, relief = FLAT, command = singmal)
    singla.place(relx = .3, rely = .4, anchor="center")
    singback = Button(root, text = "Back", font = ("arial", 15), fg = "blue", bg = "light grey", command = setnewnback)
    singback.place(relx = .5, rely = .6, anchor="center")
    root.bind("<KeyPress-Left>", lambda e: singmal())
    root.bind("<KeyPress-Right>", lambda e: singmar())
    root.bind("<KeyPress-Down>", lambda e: setnsad())
    root.bind("<KeyPress-Up>", lambda e: setnsau())
    root.bind("<Return>", lambda e: setnsday())

def setnsday():
    global ses, ssms, dmax, leap
    ses = 1
    ssms = 1
    minputs = singlme.get()
    minput = minputs.lower()
    if minput == 'january':
        dmax = 32
        os.chdir('months')
        os.chdir('January')
        setnewnd()
    elif minput == 'february':
        if leap == True:
            dmax = 30
        elif leap == False:
            dmax = 29
        else:
            tkMessageBox.showwarning("Leap Year Error", "Could not correctly get the leap year dates, please retry")
        os.chdir('months')
        os.chdir('February')
        setnewnd()
    elif minput == 'march':
        dmax = 32
        os.chdir('months')
        os.chdir('March')
        setnewnd()
    elif minput == 'april':
        dmax = 31
        os.chdir('months')
        os.chdir('April')
        setnewnd()
    elif minput == 'may':
        dmax = 32
        os.chdir('months')
        os.chdir('May')
        setnewnd()
    elif minput == 'june':
        dmax = 31
        os.chdir('months')
        os.chdir('June')
        setnewnd()
    elif minput == 'july':
        dmax = 32
        os.chdir('months')
        os.chdir('July')
        setnewnd()
    elif minput == 'august':
        dmax = 32
        os.chdir('months')
        os.chdir('August')
        setnewnd()
    elif minput == 'september':
        dmax = 31
        os.chdir('months')
        os.chdir('September')
        setnewnd()
    elif minput == 'october':
        dmax = 32
        os.chdir('months')
        os.chdir('October')
        setnewnd()
    elif minput == 'november':
        dmax = 31
        os.chdir('months')
        os.chdir('November')
        setnewnd()
    elif minput == 'december':
        dmax = 32
        os.chdir('months')
        os.chdir('December')
        setnewnd()
    else:
        singlme.delete(0, END)
        singlme.insert(0, "Invalid Month")

def setnewnd():
    global dmax, sdc, ses
    sdc = 1
    singli.config(text = "Choose Your Day:")
    singlme.delete(0, END)
    singlme.insert(0, '1')
    singra.config(command = setdaycr)
    singla.config(command = setdaycl)
    singback.config(command = setnewndback)
    subsing.config(command = setnewnds)
    root.bind("<Return>", lambda e: setnewnds())
    root.bind("<KeyPress-Right>", lambda e: setdaycr())
    root.bind("<KeyPress-Left>", lambda e: setdaycl())
    root.bind("<KeyPress-Down>", lambda e: setnsadt())
    root.bind("<KeyPress-Up>", lambda e: setnsaut())

def setnewnds():
   global dmax, sdc, ses, dinput
   ses = 1
   sdc = 1
   dinputs = singlme.get()
   try:
      dinput = int(dinputs)
      if dinput <= 0:
         singlme.delete(0, END)
         singlme.insert(0, "Invalid Day")
      elif dinput >= dmax:
         singlme.delete(0, END)
         singlme.insert(0, "Invalid Day")
      else:
         setnewnf()
   except:
      singlme.delete(0, END)
      singlme.insert(0, "Invalid Day")
   
def setnewnf():
   global ses
   ses = 1
   singra.place_forget()
   singla.place_forget()
   singli.config(text = "Write Your Event Name:")
   root.unbind("<KeyPress-Right>")
   root.unbind("<KeyPress-Left>")
   root.bind("<Return>", lambda e: setnewnsub())
   root.bind("<KeyPress-Down>", lambda e: setnsadth())
   root.bind("<KeyPress-Up>", lambda e: setnsauth())
   singlme.delete(0, END)
   singlme.config(width = 20)
   subsing.config(command = setnewnsub)
   singback.config(command = setnewnfback)

def setnewnsub():
   global feinfo, event, dinput, sef, tsevent
   event = singlme.get()
   singlme.delete(0, END)
   singlme.place_forget()
   singli.config(text = "You are finished!")
   feinfo = Label(root, text = "To change this event or see event info, go to manage", bg = color, fg = "blue", font = ("arial", 12))
   feinfo.place(relx = .5, rely = .4, anchor='center')
   singback.place_forget()
   ne = open("{}.txt".format(dinput),"w")
   ne.write(event)
   os.chdir("..")
   os.chdir("..")
   subsing.config(text = "Continue")
   subsing.config(command = setnewnsubback)
   root.bind("<Return>", lambda e: setnewnsubback())
   os.chdir('months')
   os.chdir(month)
   try:
      re = open("{}.txt".format(numday),"r")
      tsevent = re.read()
      sef = 1
   except:
      sef = 0
   os.chdir("..")
   os.chdir("..")

def setnewnsubback():
   subsing.place_forget()
   singli.place_forget()
   feinfo.place_forget()
   root.bind("<KeyPress-Up>", lambda e: setarrowu())
   root.bind("<KeyPress-Down>", lambda e: setarrowd())
   root.bind("<Return>", lambda e: setnewn())
   seto.place(relx=.5, rely=.3, anchor="center")
   sety.place(relx=.5, rely=.4, anchor="center")
   setw.place(relx=.5, rely=.5, anchor="center")
   setback.place(relx=.5, rely=.6, anchor="center")

def setnewnfback():
   global dmax, sdc, ses
   singlme.config(width = 12)
   singlme.delete(0, END)
   singli.config(text = "Choose Your Day:")
   sdc = 1
   ses = 2
   singlme.insert(0, '1')
   singra.config(command = setdaycr)
   singra.config(command = setdaycl)
   singback.config(command = setnewndback)
   subsing.config(command = setnewnds)
   root.bind("<Return>", lambda e: setnewndback())
   root.bind("<KeyPress-Right>", lambda e: setdaycr())
   root.bind("<KeyPress-Left>", lambda e: setdaycl())
   root.bind("<KeyPress-Down>", lambda e: setnsadt())
   root.bind("<KeyPress-Up>", lambda e: setnsaut())
   singra.place(relx = .7, rely = .4, anchor="center")
   singla.place(relx = .3, rely = .4, anchor="center")

def setnsadth():
    global ses
    ses = ses + 1
    if ses == 3:
        ses = ses - 1
    if ses == 0:
        ses = ses + 1
    if ses == 1:
        subsing.config(bg = "Blue", fg = "light grey")
        singback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setnewnsub())
    if ses == 2:
        subsing.config(fg = "Blue", bg = "light grey")
        singback.config(bg = "blue", fg = "light grey")
        root.bind("<Return>", lambda e: setnewnfback())

def setnsauth():
    global ses
    ses = ses - 1
    if ses == 3:
        ses = ses - 1
    if ses == 0:
        ses = ses + 1
    if ses == 1:
        subsing.config(bg = "Blue", fg = "light grey")
        singback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setnewnsub())
    if ses == 2:
        subsing.config(fg = "Blue", bg = "light grey")
        singback.config(bg = "blue", fg = "light grey")
        root.bind("<Return>", lambda e: setnewnfback())

def setnsadt():
    global ses
    ses = ses + 1
    if ses == 3:
        ses = ses - 1
    if ses == 0:
        ses = ses + 1
    if ses == 1:
        subsing.config(bg = "Blue", fg = "light grey")
        singback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setnewnds())
    if ses == 2:
        subsing.config(fg = "Blue", bg = "light grey")
        singback.config(bg = "blue", fg = "light grey")
        root.bind("<Return>", lambda e: setnewndback())

def setnsaut():
    global ses
    ses = ses - 1
    if ses == 3:
        ses = ses - 1
    if ses == 0:
        ses = ses + 1
    if ses == 1:
        subsing.config(bg = "Blue", fg = "light grey")
        singback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setnewnds())
    if ses == 2:
        subsing.config(fg = "Blue", bg = "light grey")
        singback.config(bg = "blue", fg = "light grey")
        root.bind("<Return>", lambda e: setnewndback())


def setnewndback():
   global ssms, ses
   os.chdir("..")
   os.chdir("..")
   ssms = 1
   ses = 2
   singlme.delete(0, END)
   singlme.insert(0, 'January')
   singli.config(text = "Choose Your Month:")
   singback.config(command = setnewnback)
   singra.config(command = singmar)
   singra.config(command = singmal)
   subsing.config(command = setnsday)
   root.bind("<KeyPress-Left>", lambda e: singmal())
   root.bind("<KeyPress-Right>", lambda e: singmar())
   root.bind("<KeyPress-Down>", lambda e: setnsad())
   root.bind("<KeyPress-Up>", lambda e: setnsau())
   root.bind("<Return>", lambda e: setnewnback())

def setdaycr():
    global sdc, dmax
    sdc = sdc + 1
    if sdc == 0:
        sdc = sdc + 1
    if sdc == dmax:
        sdc = sdc - 1
    singlme.delete(0, END)
    singlme.insert(0, sdc)

def setdaycl():
    global sdc, dmax
    sdc = sdc - 1
    if sdc == 0:
        sdc = sdc + 1
    if sdc == dmax:
        sdc = sdc - 1
    singlme.delete(0, END)
    singlme.insert(0, sdc)
    

def setnsad():
    global ses
    ses = ses + 1
    if ses == 3:
        ses = ses - 1
    if ses == 0:
        ses = ses + 1
    if ses == 1:
        subsing.config(bg = "Blue", fg = "light grey")
        singback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setnsday())
    if ses == 2:
        subsing.config(fg = "Blue", bg = "light grey")
        singback.config(bg = "blue", fg = "light grey")
        root.bind("<Return>", lambda e: setnewnback())

def setnsau():
    global ses
    ses = ses - 1
    if ses == 3:
        ses = ses - 1
    if ses == 0:
        ses = ses + 1
    if ses == 1:
        subsing.config(bg = "Blue", fg = "light grey")
        singback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setnsday())
    if ses == 2:
        subsing.config(fg = "Blue", bg = "light grey")
        singback.config(bg = "blue", fg = "light grey")
        root.bind("<Return>", lambda e: setnewnback())


def setnewnback():
    global ssms
    ssms = 1
    root.unbind("<KeyPress-Down>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Left>")
    root.bind("<Return>", lambda e: setnewn())
    singli.place_forget()
    singlme.place_forget()
    subsing.place_forget()
    singra.place_forget()
    singla.place_forget()
    singback.place_forget()
    seto.place(relx=.5, rely=.3, anchor="center")
    sety.place(relx=.5, rely=.4, anchor="center")
    setw.place(relx=.5, rely=.5, anchor="center")
    setback.place(relx=.5, rely=.6, anchor="center")
    root.bind("<KeyPress-Up>", lambda e: setarrowu())
    root.bind("<KeyPress-Down>", lambda e: setarrowd())
    
    

def singmar():
    global ssms
    ssms = ssms + 1
    if ssms == 0:
        ssms = ssms + 1
    if ssms == 13:
        ssms = ssms - 1
    if ssms == 1:
        singlme.delete(0, END)
        singlme.insert(0, "January")
    if ssms == 2:
        singlme.delete(0, END)
        singlme.insert(0, "February")
    if ssms == 3:
        singlme.delete(0, END)
        singlme.insert(0, "March")
    if ssms == 4:
        singlme.delete(0, END)
        singlme.insert(0, "April")
    if ssms == 5:
        singlme.delete(0, END)
        singlme.insert(0, "May")
    if ssms == 6:
        singlme.delete(0, END)
        singlme.insert(0, "June")
    if ssms == 7:
        singlme.delete(0, END)
        singlme.insert(0, "July")
    if ssms == 8:
        singlme.delete(0, END)
        singlme.insert(0, "August")
    if ssms == 9:
        singlme.delete(0, END)
        singlme.insert(0, "September")
    if ssms == 10:
        singlme.delete(0, END)
        singlme.insert(0, "October")
    if ssms == 11:
        singlme.delete(0, END)
        singlme.insert(0, "November")
    if ssms == 12:
        singlme.delete(0, END)
        singlme.insert(0, "December")

def singmal():
    global ssms
    ssms = ssms - 1
    if ssms == 0:
        ssms = ssms + 1
    if ssms == 13:
        ssms = ssms - 1
    if ssms == 1:
        singlme.delete(0, END)
        singlme.insert(0, "January")
    if ssms == 2:
        singlme.delete(0, END)
        singlme.insert(0, "February")
    if ssms == 3:
        singlme.delete(0, END)
        singlme.insert(0, "March")
    if ssms == 4:
        singlme.delete(0, END)
        singlme.insert(0, "April")
    if ssms == 5:
        singlme.delete(0, END)
        singlme.insert(0, "May")
    if ssms == 6:
        singlme.delete(0, END)
        singlme.insert(0, "June")
    if ssms == 7:
        singlme.delete(0, END)
        singlme.insert(0, "July")
    if ssms == 8:
        singlme.delete(0, END)
        singlme.insert(0, "August")
    if ssms == 9:
        singlme.delete(0, END)
        singlme.insert(0, "September")
    if ssms == 10:
        singlme.delete(0, END)
        singlme.insert(0, "October")
    if ssms == 11:
        singlme.delete(0, END)
        singlme.insert(0, "November")
    if ssms == 12:
        singlme.delete(0, END)
        singlme.insert(0, "December")


def setarrowu():
    global sms
    sms = sms - 1
    if sms == 5:
        sms = sms - 1
    if sms == 0:
        sms = sms + 1
    if sms == 1:
        seto.config(bg = "blue", fg = "light grey")
        sety.config(fg = "blue", bg = "light grey")
        setw.config(fg = "blue", bg = "light grey")
        setback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setnewn())
    if sms == 2:
        sety.config(bg = "blue", fg = "light grey")
        seto.config(fg = "blue", bg = "light grey")
        setw.config(fg = "blue", bg = "light grey")
        setback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setyf())
    if sms == 3:
        setw.config(bg = "blue", fg = "light grey")
        sety.config(fg = "blue", bg = "light grey")
        seto.config(fg = "blue", bg = "light grey")
        setback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setwf())
    if sms == 4:
        setback.config(bg = "blue", fg = "light grey")
        sety.config(fg = "blue", bg = "light grey")
        setw.config(fg = "blue", bg = "light grey")
        seto.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setbackf())

def setarrowd():
    global sms
    sms = sms + 1
    if sms == 5:
        sms = sms - 1
    if sms == 0:
        sms = sms + 1
    if sms == 1:
        seto.config(bg = "blue", fg = "light grey")
        sety.config(fg = "blue", bg = "light grey")
        setw.config(fg = "blue", bg = "light grey")
        setback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setnewn())
    if sms == 2:
        sety.config(bg = "blue", fg = "light grey")
        seto.config(fg = "blue", bg = "light grey")
        setw.config(fg = "blue", bg = "light grey")
        setback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setyf())
    if sms == 3:
        setw.config(bg = "blue", fg = "light grey")
        sety.config(fg = "blue", bg = "light grey")
        seto.config(fg = "blue", bg = "light grey")
        setback.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setwf())
    if sms == 4:
        setback.config(bg = "blue", fg = "light grey")
        sety.config(fg = "blue", bg = "light grey")
        setw.config(fg = "blue", bg = "light grey")
        seto.config(fg = "blue", bg = "light grey")
        root.bind("<Return>", lambda e: setbackf())

def setbackf():
    global sms
    sms = 1
    if menub == 1:
       root.config(menu=menubar)
    newlogol.pack_forget()
    seto.place_forget()
    sety.place_forget()
    setw.place_forget()
    setback.place_forget()
    logol.pack(side = TOP, fill = X)
    neweb.place(relx=.5, rely=.5, anchor="center")
    dayib.place(relx=.3, rely=.5, anchor="center")
    maneb.place(relx=.7, rely=.5, anchor="center")
    exitb.place(relx = .65, rely = .7, anchor = 'center')
    helpb.place(relx = .5, rely = .7, anchor = 'center')
    setb.place(relx = .35, rely = .7, anchor = 'center')
    root.bind("<Return>", lambda e: seth())
    root.bind("<KeyPress-Left>", lambda e: mainarrowl())
    root.bind("<KeyPress-Right>", lambda e: mainarrowr())
    root.bind("<KeyPress-Down>", lambda e: mainarrowd())
    root.bind("<KeyPress-Up>", lambda e: mainarrowu())

def exitf():
   exit()

def helpbackf():
    if menub == 1:
       root.config(menu=menubar)
    helpl.place_forget()
    helpm.place_forget()
    helpbackb.place_forget()
    root.bind("<Return>", lambda e: helpf())
    root.bind("<KeyPress-Left>", lambda e: mainarrowl())
    root.bind("<KeyPress-Right>", lambda e: mainarrowr())
    root.bind("<KeyPress-Down>", lambda e: mainarrowd())
    root.bind("<KeyPress-Up>", lambda e: mainarrowu())
    exitb.place(relx = .65, rely = .7, anchor = 'center')
    helpb.place(relx = .5, rely = .7, anchor = 'center')
    neweb.place(relx=.5, rely=.5, anchor="center")
    dayib.place(relx=.3, rely=.5, anchor="center")
    maneb.place(relx=.7, rely=.5, anchor="center")
    setb.place(relx = .35, rely = .7, anchor = 'center')

def helpf():
    global helpl, helpm, helpbackb
    if menub == 1:
       emptyMenu = Menu(root)
       root.config(menu=emptyMenu)
    root.unbind("<KeyPress-Left>")
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Down>")
    root.bind("<Return>", lambda e: helpbackf())
    neweb.place_forget()
    dayib.place_forget()
    maneb.place_forget()
    exitb.place_forget()
    helpb.place_forget()
    setb.place_forget()
    helpl = Label(root, text = 'Help:', font = ("arial", 25), bg = color, fg = 'blue')
    helpl.place(relx = .5, rely = .2, anchor = 'center')
    helpm = Message(root, text = "Welcome to the Calendar by Fire Dev! The way this works is you set events in the new events area. You can see your current events, tommorrows event, and holidays in the daily info section. In Manage, you can change and delete events. If you ever see a blue background button, that means if you press enter it will select that button. You can change that button with the arrow keys. Also, when you set an event, it does not go directly to daily info, you will have to restart the calendar for that. Thanks!", font = ('arial', 13), bg = color, fg = 'blue')
    helpm.place(relx = .5, rely = .5, anchor = 'center')
    helpbackb = Button(root, text = 'Back', font = ('airal', 15), bg = 'blue', fg = 'light grey', command = helpbackf)
    helpbackb.place(relx = .5, rely = .8, anchor = 'center')

def setf():
    global settingsl, ltheme, dtheme, menubon, menuboff, settingsl, settingsback, css
    css = 1
    if menub == 1:
       emptyMenu = Menu(root)
       root.config(menu=emptyMenu)
    root.unbind("<KeyPress-Left>")
    root.unbind("<KeyPress-Right>")
    root.bind("<Return>", lambda e: lthemef())
    root.bind("<KeyPress-Down>", lambda e: settarrowd())
    root.bind("<KeyPress-Up>", lambda e: settarrowu())
    neweb.place_forget()
    dayib.place_forget()
    maneb.place_forget()
    exitb.place_forget()
    helpb.place_forget()
    setb.place_forget()
    settingsl = Label(root, text = 'Settings:', font = ("arial", 25), bg = color, fg = 'blue')
    settingsl.place(relx = .5, rely = .2, anchor = 'center')
    ltheme = Button(root, text = 'Light Theme', font = ("arial", 15), bg = 'blue', fg = 'light grey', command = lthemef)
    ltheme.place(relx = .5, rely = .3, anchor = 'center')
    dtheme = Button(root, text = 'Dark Theme', font = ("arial", 15), fg = 'blue', bg = 'light grey', command = dthemef)
    dtheme.place(relx = .5, rely = .4, anchor = 'center')
    menuboff = Button(root, text = 'Menu Bar Off', font = ("arial", 15), fg = 'blue', bg = 'light grey', command = menubaroff)
    menuboff.place(relx = .5, rely = .5, anchor = 'center')
    menubon = Button(root, text = 'Menu Bar On', font = ("arial", 15), fg = 'blue', bg = 'light grey', command = menubaron)
    menubon.place(relx = .5, rely = .6, anchor = 'center')
    settingsback = Button(root, text = 'Back', font = ("arial", 15), fg = 'blue', bg = 'light grey', command = setfback)
    settingsback.place(relx = .5, rely = .7, anchor = 'center')

def setfback():
    if menub == 1:
       root.config(menu=menubar)
    ltheme.place_forget()
    dtheme.place_forget()
    menubon.place_forget()
    menuboff.place_forget()
    settingsback.place_forget()
    settingsl.place_forget()
    root.bind("<Return>", lambda e: setf())
    root.bind("<KeyPress-Left>", lambda e: mainarrowl())
    root.bind("<KeyPress-Right>", lambda e: mainarrowr())
    root.bind("<KeyPress-Down>", lambda e: mainarrowd())
    root.bind("<KeyPress-Up>", lambda e: mainarrowu())
    settingsl.place_forget()
    exitb.place(relx = .65, rely = .7, anchor = 'center')
    helpb.place(relx = .5, rely = .7, anchor = 'center')
    neweb.place(relx=.5, rely=.5, anchor="center")
    dayib.place(relx=.3, rely=.5, anchor="center")
    maneb.place(relx=.7, rely=.5, anchor="center")
    setb.place(relx = .35, rely = .7, anchor = 'center')

def settarrowd():
    global css
    css = css + 1
    if css == 6:
       css = css - 1
    if css == 0:
       css = css + 1
    if css == 1:
       ltheme.config(bg = 'blue', fg = 'light grey')
       dtheme.config(fg = 'blue', bg = 'light grey')
       menubon.config(fg = 'blue', bg = 'light grey')
       menuboff.config(fg = 'blue', bg = 'light grey')
       settingsback.config(fg = 'blue', bg = 'light grey')
       root.bind("<Return>", lambda e: lthemef())
    if css == 2:
       dtheme.config(bg = 'blue', fg = 'light grey')
       ltheme.config(fg = 'blue', bg = 'light grey')
       menubon.config(fg = 'blue', bg = 'light grey')
       menuboff.config(fg = 'blue', bg = 'light grey')
       settingsback.config(fg = 'blue', bg = 'light grey')
       root.bind("<Return>", lambda e: dthemef())
    if css == 3:
       menuboff.config(bg = 'blue', fg = 'light grey')
       ltheme.config(fg = 'blue', bg = 'light grey')
       menubon.config(fg = 'blue', bg = 'light grey')
       dtheme.config(fg = 'blue', bg = 'light grey')
       settingsback.config(fg = 'blue', bg = 'light grey')
       root.bind("<Return>", lambda e: menubaroff())
    if css == 4:
       menubon.config(bg = 'blue', fg = 'light grey')
       ltheme.config(fg = 'blue', bg = 'light grey')
       menuboff.config(fg = 'blue', bg = 'light grey')
       dtheme.config(fg = 'blue', bg = 'light grey')
       settingsback.config(fg = 'blue', bg = 'light grey')
       root.bind("<Return>", lambda e: menubaron())
    if css == 5:
       settingsback.config(bg = 'blue', fg = 'light grey')
       ltheme.config(fg = 'blue', bg = 'light grey')
       menuboff.config(fg = 'blue', bg = 'light grey')
       dtheme.config(fg = 'blue', bg = 'light grey')
       menubon.config(fg = 'blue', bg = 'light grey')
       root.bind("<Return>", lambda e: setfback())

def settarrowu():
    global css
    css = css - 1
    if css == 6:
       css = css - 1
    if css == 0:
       css = css + 1
    if css == 1:
       ltheme.config(bg = 'blue', fg = 'light grey')
       dtheme.config(fg = 'blue', bg = 'light grey')
       menubon.config(fg = 'blue', bg = 'light grey')
       menuboff.config(fg = 'blue', bg = 'light grey')
       settingsback.config(fg = 'blue', bg = 'light grey')
       root.bind("<Return>", lambda e: lthemef())
    if css == 2:
       dtheme.config(bg = 'blue', fg = 'light grey')
       ltheme.config(fg = 'blue', bg = 'light grey')
       menubon.config(fg = 'blue', bg = 'light grey')
       menuboff.config(fg = 'blue', bg = 'light grey')
       settingsback.config(fg = 'blue', bg = 'light grey')
       root.bind("<Return>", lambda e: dthemef())
    if css == 3:
       menuboff.config(bg = 'blue', fg = 'light grey')
       ltheme.config(fg = 'blue', bg = 'light grey')
       menubon.config(fg = 'blue', bg = 'light grey')
       dtheme.config(fg = 'blue', bg = 'light grey')
       settingsback.config(fg = 'blue', bg = 'light grey')
       root.bind("<Return>", lambda e: menubaroff())
    if css == 4:
       menubon.config(bg = 'blue', fg = 'light grey')
       ltheme.config(fg = 'blue', bg = 'light grey')
       menuboff.config(fg = 'blue', bg = 'light grey')
       dtheme.config(fg = 'blue', bg = 'light grey')
       settingsback.config(fg = 'blue', bg = 'light grey')
       root.bind("<Return>", lambda e: menubaron())
    if css == 5:
       settingsback.config(bg = 'blue', fg = 'light grey')
       ltheme.config(fg = 'blue', bg = 'light grey')
       menuboff.config(fg = 'blue', bg = 'light grey')
       dtheme.config(fg = 'blue', bg = 'light grey')
       menubon.config(fg = 'blue', bg = 'light grey')
       root.bind("<Return>", lambda e: setfback())

def lthemef():
    global color
    if color.lower() == 'black':
       color = 'white'
       global logopic, devpic, newlogopic, rightapic2, leftapic2, exitpic2, helppic2, setpic2, setpic, helppic, howpic
       settingsl.config(bg = 'white')
       devpic = PhotoImage(file =r"./images/FIREDEV.gif")
       logopic = PhotoImage(file =r"./images/logo.gif")
       newlogopic = PhotoImage(file =r"./images/newlogo.gif")
       rightapic = PhotoImage(file = r"./images/RightArrow.gif")
       rightapic2 = rightapic.subsample(7,7)
       leftapic = PhotoImage(file = r"./images/LeftArrow.gif")
       leftapic2 = leftapic.subsample(7,7)
       exitpic = PhotoImage(file = r"./images/Exit.gif")
       exitpic2 = exitpic.subsample(8,8)
       helppic = PhotoImage(file = r"./images/Help.gif")
       helppic2 = helppic.subsample(8,8)
       setpic = PhotoImage(file = r"./images/Settings.gif")
       setpic2 = setpic.subsample(8,8)
       root.config(bg = color)
       colorwrite = open('./settings/Theme.txt', 'w')
       colorwrite.write('white')
       logol.config(bg = 'white', image = logopic)
       devl.config(bg = 'white', image = devpic)
       exitb.config(image = exitpic2)
       helpb.config(image = helppic2)
       setb.config(image = setpic2)

            

def dthemef():
    global color
    if color.lower() == 'white':
       color = 'black'
       global logopic, devpic, newlogopic, rightapic2, leftapic2, exitpic2, helppic2, setpic2, setpic, helppic, howpic
       settingsl.config(bg = 'black')
       devpic = PhotoImage(file =r"./images/FIREDEVDARK.gif")
       logopic = PhotoImage(file =r"./images/logoDark.gif")
       newlogopic = PhotoImage(file =r"./images/newlogoDark.gif")
       rightapic = PhotoImage(file = r"./images/RightArrowDark.gif")
       rightapic2 = rightapic.subsample(7,7)
       leftapic = PhotoImage(file = r"./images/LeftArrowDark.gif")
       leftapic2 = leftapic.subsample(7,7)
       exitpic = PhotoImage(file = r"./images/ExitDark.gif")
       exitpic2 = exitpic.subsample(8,8)
       helppic = PhotoImage(file = r"./images/HelpDark.gif")
       helppic2 = helppic.subsample(8,8)
       setpic = PhotoImage(file = r"./images/SettingsDark.gif")
       setpic2 = setpic.subsample(8,8)
       root.config(bg = color)
       colorwrite = open('./settings/Theme.txt', 'w')
       colorwrite.write('black')
       logol.config(bg = 'black', image = logopic)
       devl.config(bg = 'black', image = devpic)
       exitb.config(image = exitpic2)
       helpb.config(image = helppic2)
       setb.config(image = setpic2)

def menubaron():
   global menub
   if menub == 0:
      menub = 1
      menuwrite = open('./settings/MenuBar.txt', 'w')
      menuwrite.write('1')
      global menubar, editmenu, filemenu
      menubar = Menu(root)
      menubar.add_command(label="Exit", command = exitf)
      menubar.add_command(label="Daily Info", command = dayi)
      editmenu = Menu(menubar, tearoff=0)
      editmenu.add_command(label="New Event", command=seth)
      editmenu.add_separator()
      editmenu.add_command(label="Single Event", command=singemenu)
      editmenu.add_command(label="Weekly Event", command=weekemenu)
      editmenu.add_command(label="Yearly Event", command=yearemenu)
      menubar.add_cascade(label="New Events", menu=editmenu)
      menubar.add_command(label="Manage", command=manage)
      filemenu = Menu(menubar, tearoff=0)
      filemenu.add_command(label="Remove Menubar", command=rmenub)
      menubar.add_cascade(label="Options", menu=filemenu)
      menubar.add_command(label="Settings", command=setf)
      menubar.add_command(label="Help", command=helpf)


def menubaroff():
   global menub
   if menub == 1:
      menub = 0
      menuwrite = open('./settings/MenuBar.txt', 'w')
      menuwrite.write('0')

def manage():
    global managel, mans, many, manw, manback, mana
    if menub == 1:
       emptyMenu = Menu(root)
       root.config(menu=emptyMenu)
    mana = 1
    root.unbind("<KeyPress-Left>")
    root.unbind("<KeyPress-Right>")
    root.bind("<KeyPress-Up>", lambda e: manau())
    root.bind("<KeyPress-Down>", lambda e: manad())
    root.bind("<Return>", lambda e: mansf())
    neweb.place_forget()
    dayib.place_forget()
    maneb.place_forget()
    exitb.place_forget()
    helpb.place_forget()
    setb.place_forget()
    managel = Label(root, text = 'Manage:', font = ("arial", 25), bg = color, fg = 'blue')
    managel.place(relx = .5, rely = .2, anchor = 'center')
    mans = Button(root, text = 'Single Events', font = ("arial", 15), bg = 'blue', fg = 'light grey', command = mansf)
    mans.place(relx = .5, rely = .3, anchor = 'center')
    many = Button(root, text = 'Yearly Events', font = ("arial", 15), fg = 'blue', bg = 'light grey', command = manyf)
    many.place(relx = .5, rely = .4, anchor = 'center')
    manw = Button(root, text = 'Weekly Events', font = ("arial", 15), fg = 'blue', bg = 'light grey', command = manwf)
    manw.place(relx = .5, rely = .5, anchor = 'center')
    manback = Button(root, text = 'Back', font = ("arial", 15), fg = 'blue', bg = 'light grey', command = manageback)
    manback.place(relx = .5, rely = .6, anchor = 'center')

def manad():
   global mana
   mana = mana + 1
   if mana == 0:
      mana = mana + 1
   if mana == 5:
      mana = mana + 1
   if mana == 1:
      mans.config(bg = 'blue', fg = 'light grey')
      many.config(fg = 'blue', bg = 'light grey')
      manw.config(fg = 'blue', bg = 'light grey')
      manback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: mansf())
   if mana == 2:
      many.config(bg = 'blue', fg = 'light grey')
      mans.config(fg = 'blue', bg = 'light grey')
      manw.config(fg = 'blue', bg = 'light grey')
      manback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manyf())
   if mana == 3:
      manw.config(bg = 'blue', fg = 'light grey')
      many.config(fg = 'blue', bg = 'light grey')
      mans.config(fg = 'blue', bg = 'light grey')
      manback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manwf())
   if mana == 4:
      manback.config(bg = 'blue', fg = 'light grey')
      many.config(fg = 'blue', bg = 'light grey')
      manw.config(fg = 'blue', bg = 'light grey')
      mans.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manageback())

def manau():
   global mana
   mana = mana - 1
   if mana == 0:
      mana = mana + 1
   if mana == 5:
      mana = mana + 1
   if mana == 1:
      mans.config(bg = 'blue', fg = 'light grey')
      many.config(fg = 'blue', bg = 'light grey')
      manw.config(fg = 'blue', bg = 'light grey')
      manback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: mansf())
   if mana == 2:
      many.config(bg = 'blue', fg = 'light grey')
      mans.config(fg = 'blue', bg = 'light grey')
      manw.config(fg = 'blue', bg = 'light grey')
      manback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manyf())
   if mana == 3:
      manw.config(bg = 'blue', fg = 'light grey')
      many.config(fg = 'blue', bg = 'light grey')
      mans.config(fg = 'blue', bg = 'light grey')
      manback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manwf())
   if mana == 4:
      manback.config(bg = 'blue', fg = 'light grey')
      many.config(fg = 'blue', bg = 'light grey')
      manw.config(fg = 'blue', bg = 'light grey')
      mans.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manageback())      

def manyf():
    global monthar, monthal, monthme, dayme, dayal, dayar, ssms, sdc, mannexts, manbacks, msa
    ssms = 1
    sdc = 1
    msa = 1
    root.unbind("<Return>")
    root.bind('<KeyPress-Up>', lambda e: manyau())
    root.bind('<KeyPress-Down>', lambda e: manyad())
    root.bind('<KeyPress-Left>', lambda e: smanmonthl())
    root.bind('<KeyPress-Right>', lambda e: smanmonthr())
    mans.place_forget()
    many.place_forget()
    manw.place_forget()
    managel.config(text = 'Choose Your Yearly Event Date')
    manback.place_forget()
    monthar = Button(root, image = rightapic2, bg = color, relief = FLAT, command = smanmonthr)
    monthal = Button(root, image = leftapic2, bg = color, relief = FLAT, command = smanmonthl)
    monthal.place(relx = .3, rely = .35, anchor = 'center')
    monthar.place(relx = .7, rely = .35, anchor = 'center')
    monthme = Entry(root, exportselection=0, width = 12, font = ("arial", 15), fg = "dark Blue", relief = RAISED, bd = 10)
    monthme.place(relx = .5, rely = .35, anchor="center")
    monthme.insert(0, "January")
    dayme = Entry(root, exportselection=0, width = 12, font = ("arial", 15), fg = "blue", relief = RAISED, bd = 10)
    dayme.place(relx = .5, rely = .50, anchor="center")
    dayme.insert(0, "1")
    dayar = Button(root, image = rightapic2, bg = color, relief = FLAT, command = mansdayr)
    dayal = Button(root, image = leftapic2, bg = color, relief = FLAT, command = mansdayl)
    dayal.place(relx = .3, rely = .50, anchor = 'center')
    dayar.place(relx = .7, rely = .50, anchor = 'center')
    mannexts = Button(root, text = 'Next', font = ('arial', 15), fg = 'blue', bg = 'light grey', command = manyic)
    mannexts.place(relx = .5, rely = .65, anchor = 'center')
    manbacks = Button(root, text = 'Back', font = ('arial', 15), fg = 'blue', bg = 'light grey', command = manyback)
    manbacks.place(relx = .5, rely = .75, anchor = 'center')

def manyep():
    global sed, seets, sede, sedd, dem, manfile, manshback, mansa
    mansa = 1
    managel.config(text = 'Manage:')
    monthar.place_forget()
    monthal.place_forget()
    monthme.place_forget()
    dayme.place_forget()
    dayal.place_forget()
    dayar.place_forget()
    mannexts.place_forget()
    manbacks.place_forget()
    root.bind("<Return>", lambda e: manssubt())
    root.unbind("<KeyPress-Left>")
    root.unbind("<KeyPress-Right>")
    root.bind("<KeyPress-Up>", lambda e: manyharrowu())
    root.bind("<KeyPress-Down>", lambda e: manyharrowd())
    try:
       manfile = open('{}.txt'.format(dinput), mode='r+')
       manfiletext = manfile.read()
       manfile.close()
    except:
       manfiletext = 'No Yearly Event'
    sedd = Label(root, text = '{} {}'.format(minput, dinput), bg = 'white', fg = 'blue', font = ('arial', 20))
    sedd.place(relx = .5, rely = .3, anchor='center')
    sed = Entry(root, width = '15', fg = 'blue', exportselection=0, bd = 10, font = ('arial', 15), relief = RAISED)
    sed.place(relx = .5, rely = .4, anchor='center')
    sed.delete(0, END)
    sed.insert(0, manfiletext)
    seets = Button(root, text = 'Submit Text', font = ('arial', 15), fg = 'light grey', bg = 'blue', command = manysubt)
    seets.place(relx = .5, rely = .5, anchor = 'center')
    sede = Button(root, text = 'Delete Event', font = ('arial', 15), bg = 'light grey', fg = 'blue', command = mansdele)
    sede.place(relx = .5, rely = .6, anchor = 'center')
    dem = Button(root, text = 'Delete All {} Events'.format(minput), font = ('arial', 15), bg = 'light grey', fg = 'blue', command = mansdelm)
    dem.place(relx = .5, rely = .7, anchor = 'center')
    manshback = Button(root, text = 'Back'.format(minput), font = ('arial', 15), bg = 'light grey', fg = 'blue', command = manydcback)
    manshback.place(relx = .5, rely = .8, anchor = 'center')

def manysubt():
   sedtext = sed.get()
   if sedtext == 'No Yearly Event':
      sed.delete(0, END)
      sed.insert(0, 'Invalid Event')
   elif sedtext == 'Invalid Event':
      sed.delete(0, END)
      sed.insert(0, 'Invalid Event')
   else:
      mansfilewrite = open('{}.txt'.format(dinput), mode='w')
      mansfilewrite.write(sedtext)
      messagebox.showinfo("Edit Completed", "Your event has sucsessfully been changed")

def manyharrowu():
   global mansa
   mansa = mansa - 1
   if mansa == 5:
      mansa = mansa - 1
   if mansa == 0:
      mansa = mansa + 1
   if mansa == 1:
      seets.config(bg = 'blue', fg = 'light grey')
      sede.config(fg = 'blue', bg = 'light grey')
      dem.config(fg = 'blue', bg = 'light grey')
      manshback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manysubt())
   if mansa == 2:
      sede.config(bg = 'blue', fg = 'light grey')
      seets.config(fg = 'blue', bg = 'light grey')
      dem.config(fg = 'blue', bg = 'light grey')
      manshback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: mansdele())
   if mansa == 3:
      dem.config(bg = 'blue', fg = 'light grey')
      sede.config(fg = 'blue', bg = 'light grey')
      seets.config(fg = 'blue', bg = 'light grey')
      manshback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: mansdelm())
   if mansa == 4:
      manshback.config(bg = 'blue', fg = 'light grey')
      sede.config(fg = 'blue', bg = 'light grey')
      dem.config(fg = 'blue', bg = 'light grey')
      seets.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manydcback())

def manyharrowd():
   global mansa
   mansa = mansa + 1
   if mansa == 5:
      mansa = mansa - 1
   if mansa == 0:
      mansa = mansa + 1
   if mansa == 1:
      seets.config(bg = 'blue', fg = 'light grey')
      sede.config(fg = 'blue', bg = 'light grey')
      dem.config(fg = 'blue', bg = 'light grey')
      manshback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manysubt())
   if mansa == 2:
      sede.config(bg = 'blue', fg = 'light grey')
      seets.config(fg = 'blue', bg = 'light grey')
      dem.config(fg = 'blue', bg = 'light grey')
      manshback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: mansdele())
   if mansa == 3:
      dem.config(bg = 'blue', fg = 'light grey')
      sede.config(fg = 'blue', bg = 'light grey')
      seets.config(fg = 'blue', bg = 'light grey')
      manshback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: mansdelm())
   if mansa == 4:
      manshback.config(bg = 'blue', fg = 'light grey')
      sede.config(fg = 'blue', bg = 'light grey')
      dem.config(fg = 'blue', bg = 'light grey')
      seets.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manydcback())

def manydcback():
    os.chdir('..')
    os.chdir('..')
    sedd.place_forget()
    sed.place_forget()
    seets.place_forget()
    sede.place_forget()
    dem.place_forget()
    manshback.place_forget()
    mans.place(relx = .5, rely = .3, anchor = 'center')
    manback.place(relx = .5, rely = .6, anchor = 'center')
    manw.place(relx = .5, rely = .5, anchor = 'center')
    many.place(relx = .5, rely = .4, anchor = 'center')
    root.unbind("<KeyPress-Left>")
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Down>")
    root.bind("<KeyPress-Up>", lambda e: manau())
    root.bind("<KeyPress-Down>", lambda e: manad())
    root.bind("<Return>", lambda e: manyf())

def manyic():
    global dmax, leap, minput, ssms, msa
    mansmonth = monthme.get()
    minput = mansmonth.lower()
    if minput == 'january':
        dmax = 32
        manydayv()
    elif minput == 'february':
        if leap == True:
            dmax = 30
        elif leap == False:
            dmax = 29
        else:
            tkMessageBox.showwarning("Leap Year Error", "Could not correctly get the leap year dates, please retry")
        manydayv()
    elif minput == 'march':
        dmax = 32
        manydayv()
    elif minput == 'april':
        dmax = 31
        manydayv()
    elif minput == 'may':
        dmax = 32
        manydayv()
    elif minput == 'june':
        dmax = 31
        manydayv()
    elif minput == 'july':
        dmax = 32
        manydayv()
    elif minput == 'august':
        dmax = 32
        manydayv()
    elif minput == 'september':
        manydayv()
    elif minput == 'october':
        dmax = 32
        manydayv()
    elif minput == 'november':
        dmax = 31
        manydayv()
    elif minput == 'december':
        dmax = 32
        manydayv()
    else:
        monthme.delete(0, END)
        monthme.insert(0, "Invalid Month")

def manydayv():
   global dmax, dinput
   dmax = dmax - 2
   dinputl = dayme.get()
   try:
      dinput = int(dinputl)
      dayint = True
   except ValueError:
      dayint = False
   if dayint == True and dinput > dmax:
      dayme.delete(0, END)
      dayme.insert(0, 'Invalid Day')
   elif dayint == True and dinput < 1:
      dayme.delete(0, END)
      dayme.insert(0, 'Invalid Day')
   elif dayint == False:
      dayme.delete(0, END)
      dayme.insert(0, 'Invalid Day')
   else:
      os.chdir('year')
      os.chdir(minput)
      manyep()

def manyback():
    managel.config(text = 'Manage:')
    monthar.place_forget()
    monthal.place_forget()
    monthme.place_forget()
    dayme.place_forget()
    dayal.place_forget()
    dayar.place_forget()
    mannexts.place_forget()
    manbacks.place_forget()
    mans.place(relx = .5, rely = .3, anchor = 'center')
    manback.place(relx = .5, rely = .6, anchor = 'center')
    manw.place(relx = .5, rely = .5, anchor = 'center')
    many.place(relx = .5, rely = .4, anchor = 'center')
    root.unbind("<KeyPress-Left>")
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Down>")
    root.bind("<KeyPress-Up>", lambda e: manau())
    root.bind("<KeyPress-Down>", lambda e: manad())
    root.bind("<Return>", lambda e: manyf())

def manyad():
    global msa
    msa = msa + 1
    if msa == 0:
       msa = msa + 1
    if msa == 5:
       msa = msa - 1
    if msa == 1:
       monthme.config(fg = 'dark blue')
       dayme.config(fg = 'blue')
       mannexts.config(bg = 'light grey', fg = 'blue')
       manbacks.config(bg = 'light grey', fg = 'blue')
       root.unbind("<Return>")
       root.bind('<KeyPress-Left>', lambda e: smanmonthl())
       root.bind('<KeyPress-Right>', lambda e: smanmonthr())
    if msa == 2:
       dayme.config(fg = 'dark blue')
       monthme.config(fg = 'blue')
       mannexts.config(bg = 'light grey', fg = 'blue')
       manbacks.config(bg = 'light grey', fg = 'blue')
       root.unbind("<Return>")
       root.bind('<KeyPress-Left>', lambda e: mansdayl())
       root.bind('<KeyPress-Right>', lambda e: mansdayr())
    if msa == 3:
       dayme.config(fg = 'blue')
       monthme.config(fg = 'blue')
       mannexts.config(bg = 'blue', fg = 'light grey')
       manbacks.config(bg = 'light grey', fg = 'blue')
       root.bind("<Return>", lambda e: manyic())
       root.unbind('<KeyPress-Left>')
       root.unbind('<KeyPress-Right>')
    if msa == 4:
       dayme.config(fg = 'blue')
       monthme.config(fg = 'blue')
       mannexts.config(fg = 'blue', bg = 'light grey')
       manbacks.config(fg = 'light grey', bg = 'blue')
       root.bind("<Return>", lambda e: manyback())
       root.unbind('<KeyPress-Left>')
       root.unbind('<KeyPress-Right>')

def manyau():
    global msa
    msa = msa - 1
    if msa == 0:
       msa = msa + 1
    if msa == 5:
       msa = msa - 1
    if msa == 1:
       monthme.config(fg = 'dark blue')
       dayme.config(fg = 'blue')
       mannexts.config(bg = 'light grey', fg = 'blue')
       manbacks.config(bg = 'light grey', fg = 'blue')
       root.unbind("<Return>")
       root.bind('<KeyPress-Left>', lambda e: smanmonthl())
       root.bind('<KeyPress-Right>', lambda e: smanmonthr())
    if msa == 2:
       dayme.config(fg = 'dark blue')
       monthme.config(fg = 'blue')
       mannexts.config(bg = 'light grey', fg = 'blue')
       manbacks.config(bg = 'light grey', fg = 'blue')
       root.unbind("<Return>")
       root.bind('<KeyPress-Left>', lambda e: mansdayl())
       root.bind('<KeyPress-Right>', lambda e: mansdayr())
    if msa == 3:
       dayme.config(fg = 'blue')
       monthme.config(fg = 'blue')
       mannexts.config(bg = 'blue', fg = 'light grey')
       manbacks.config(bg = 'light grey', fg = 'blue')
       root.bind("<Return>", lambda e: manyic())
       root.unbind('<KeyPress-Left>')
       root.unbind('<KeyPress-Right>')
    if msa == 4:
       dayme.config(fg = 'blue')
       monthme.config(fg = 'blue')
       mannexts.config(fg = 'blue', bg = 'light grey')
       manbacks.config(fg = 'light grey', bg = 'blue')
       root.bind("<Return>", lambda e: manyback())
       root.unbind('<KeyPress-Left>')
       root.unbind('<KeyPress-Right>')


def manwf():
    global monthar, monthal, monthme, ssms, sdc, mannexts, manbacks, msa
    ssms = 1
    sdc = 1
    msa = 1
    root.bind("<Return>", lambda e: manwic())
    root.bind('<KeyPress-Up>', lambda e: manwau())
    root.bind('<KeyPress-Down>', lambda e: manwad())
    root.bind('<KeyPress-Left>', lambda e: manwsdal())
    root.bind('<KeyPress-Right>', lambda e: manwsdar())
    mans.place_forget()
    many.place_forget()
    manw.place_forget()
    managel.config(text = 'Choose Your Weekly Event Date')
    manback.place_forget()
    monthar = Button(root, image = rightapic2, bg = color, relief = FLAT, command = manwsdar)
    monthal = Button(root, image = leftapic2, bg = color, relief = FLAT, command = manwsdal)
    monthal.place(relx = .3, rely = .35, anchor = 'center')
    monthar.place(relx = .7, rely = .35, anchor = 'center')
    monthme = Entry(root, exportselection=0, width = 15, font = ("arial", 15), fg = "blue", relief = RAISED, bd = 10)
    monthme.place(relx = .5, rely = .35, anchor="center")
    monthme.insert(0, "Sunday")
    mannexts = Button(root, text = 'Next', font = ('arial', 15), bg = 'blue', fg = 'light grey', command = manwic)
    mannexts.place(relx = .5, rely = .50, anchor = 'center')
    manbacks = Button(root, text = 'Back', font = ('arial', 15), fg = 'blue', bg = 'light grey', command = manyback)
    manbacks.place(relx = .5, rely = .60, anchor = 'center')   

def manwep():
    global sed, seets, sede, sedd, manfile, manshback, mansa
    os.chdir('week')
    mansa = 1
    managel.config(text = 'Manage:')
    monthar.place_forget()
    monthal.place_forget()
    monthme.place_forget()
    mannexts.place_forget()
    manbacks.place_forget()
    root.bind("<Return>", lambda e: manwsubt())
    root.unbind("<KeyPress-Left>")
    root.unbind("<KeyPress-Right>")
    root.bind("<KeyPress-Up>", lambda e: manwharrowu())
    root.bind("<KeyPress-Down>", lambda e: manwharrowd())
    try:
       manfile = open('{}.txt'.format(minput.lower()), mode='r')
       manfiletext = manfile.read()
       manfile.close()
    except:
       manfiletext = 'No Weekly Event'
    sedd = Label(root, text = '{}'.format(minput), bg = 'white', fg = 'blue', font = ('arial', 20))
    sedd.place(relx = .5, rely = .3, anchor='center')
    sed = Entry(root, width = 20, fg = 'blue', exportselection=0, bd = 10, font = ('arial', 15), relief = RAISED)
    sed.place(relx = .5, rely = .4, anchor='center')
    sed.delete(0, END)
    sed.insert(0, manfiletext)
    seets = Button(root, text = 'Submit Text', font = ('arial', 15), fg = 'light grey', bg = 'blue', command = manwsubt)
    seets.place(relx = .5, rely = .5, anchor = 'center')
    sede = Button(root, text = 'Delete Event', font = ('arial', 15), bg = 'light grey', fg = 'blue', command = manwdele)
    sede.place(relx = .5, rely = .6, anchor = 'center')
    manshback = Button(root, text = 'Back', font = ('arial', 15), bg = 'light grey', fg = 'blue', command = manwdcback)
    manshback.place(relx = .5, rely = .7, anchor = 'center')

def manwharrowd():
   global mansa
   mansa = mansa + 1
   if mansa == 4:
      mansa = mansa - 1
   if mansa == 0:
      mansa = mansa + 1
   if mansa == 1:
      seets.config(bg = 'blue', fg = 'light grey')
      sede.config(fg = 'blue', bg = 'light grey')
      manshback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manwsubt())
   if mansa == 2:
      sede.config(bg = 'blue', fg = 'light grey')
      seets.config(fg = 'blue', bg = 'light grey')
      manshback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manwdele())
   if mansa == 3:
      manshback.config(bg = 'blue', fg = 'light grey')
      sede.config(fg = 'blue', bg = 'light grey')
      seets.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manwdcback())

def manwharrowu():
   global mansa
   mansa = mansa - 1
   if mansa == 4:
      mansa = mansa - 1
   if mansa == 0:
      mansa = mansa + 1
   if mansa == 1:
      seets.config(bg = 'blue', fg = 'light grey')
      sede.config(fg = 'blue', bg = 'light grey')
      manshback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manwsubt())
   if mansa == 2:
      sede.config(bg = 'blue', fg = 'light grey')
      seets.config(fg = 'blue', bg = 'light grey')
      manshback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manwdele())
   if mansa == 3:
      manshback.config(bg = 'blue', fg = 'light grey')
      sede.config(fg = 'blue', bg = 'light grey')
      seets.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manwdcback())

def manwdcback():
    os.chdir('..')
    sedd.place_forget()
    sed.place_forget()
    seets.place_forget()
    sede.place_forget()
    manshback.place_forget()
    mans.place(relx = .5, rely = .3, anchor = 'center')
    manback.place(relx = .5, rely = .6, anchor = 'center')
    manw.place(relx = .5, rely = .5, anchor = 'center')
    many.place(relx = .5, rely = .4, anchor = 'center')
    root.unbind("<KeyPress-Left>")
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Down>")
    root.bind("<KeyPress-Up>", lambda e: manau())
    root.bind("<KeyPress-Down>", lambda e: manad())
    root.bind("<Return>", lambda e: manwf())

def manwdele():
   delec = messagebox.askquestion("Confirmation","Are you sure you want to delete your event?", icon='warning')
   if 'yes':
      try:
         os.remove('{}.txt'.format(minput.lower()))
         manfiletext = 'No Single Event'
         sed.delete(0, END)
         sed.insert(0, manfiletext)
      except:
         manfiletext = 'No Single Event'
         sed.delete(0, END)
         sed.insert(0, manfiletext)
      messagebox.showinfo("Deletion Completed", "Your event has sucsessfully been deleted")

def manwsubt():
   sedtext = sed.get()
   if sedtext == 'No Weekly Event':
      sed.delete(0, END)
      sed.insert(0, 'Invalid Event')
   elif sedtext == 'Invalid Event':
      sed.delete(0, END)
      sed.insert(0, 'Invalid Event')
   else:
      mansfilewrite = open('{}.txt'.format(minput.lower()), mode='w')
      mansfilewrite.write(sedtext)
      messagebox.showinfo("Edit Completed", "Your event has sucsessfully been changed")

def manwic():
    global dmax, leap, minput, ssms, msa
    mansmonth = monthme.get()
    minput = mansmonth.lower()
    if minput == 'monday':
        minput = 'Monday'
        manwep()
    elif minput == 'tuesday':
        minput = 'Tuesday'
        manwep()
    elif minput == 'wednesday':
        minput = 'Wednesday'
        manwep()
    elif minput == 'thursday':
        minput = 'Thursday'
        manwep()
    elif minput == 'friday':
        minput = 'Friday'
        manwep()
    elif minput == 'saturday':
        minput = 'Saturday'
        manwep()
    elif minput == 'sunday':
        minput = 'Sunday'
        manwep()
    else:
        monthme.delete(0, END)
        monthme.insert(0, "Invalid Weekday")

def manwad():
    global msa
    msa = msa + 1
    if msa == 0:
       msa = msa + 1
    if msa == 3:
       msa = msa - 1
    if msa == 1:
       mannexts.config(bg = 'blue', fg = 'light grey')
       manbacks.config(bg = 'light grey', fg = 'blue')
       root.bind("<Return>", lambda e: manwic())
    if msa == 2:
       mannexts.config(fg = 'blue', bg = 'light grey')
       manbacks.config(fg = 'light grey', bg = 'blue')
       root.bind("<Return>", lambda e: manwback())

def manwau():
    global msa
    msa = msa - 1
    if msa == 0:
       msa = msa + 1
    if msa == 3:
       msa = msa - 1
    if msa == 1:
       mannexts.config(bg = 'blue', fg = 'light grey')
       manbacks.config(bg = 'light grey', fg = 'blue')
       root.bind("<Return>", lambda e: manwic())
    if msa == 2:
       mannexts.config(fg = 'blue', bg = 'light grey')
       manbacks.config(fg = 'light grey', bg = 'blue')
       root.bind("<Return>", lambda e: manwback())
   

def manwsdal():
    global ssms
    ssms = ssms - 1
    if ssms == 0:
        ssms = ssms + 1
    if ssms == 8:
        ssms = ssms - 1
    if ssms == 1:
        monthme.delete(0, END)
        monthme.insert(0, "Sunday")
    if ssms == 2:
        monthme.delete(0, END)
        monthme.insert(0, "Monday")
    if ssms == 3:
        monthme.delete(0, END)
        monthme.insert(0, "Tuesday")
    if ssms == 4:
        monthme.delete(0, END)
        monthme.insert(0, "Wednesday")
    if ssms == 5:
        monthme.delete(0, END)
        monthme.insert(0, "Thursday")
    if ssms == 6:
        monthme.delete(0, END)
        monthme.insert(0, "Friday")
    if ssms == 7:
        monthme.delete(0, END)
        monthme.insert(0, "Saturday")

def manwsdar():
    global ssms
    ssms = ssms + 1
    if ssms == 0:
        ssms = ssms + 1
    if ssms == 8:
        ssms = ssms - 1
    if ssms == 1:
        monthme.delete(0, END)
        monthme.insert(0, "Sunday")
    if ssms == 2:
        monthme.delete(0, END)
        monthme.insert(0, "Monday")
    if ssms == 3:
        monthme.delete(0, END)
        monthme.insert(0, "Tuesday")
    if ssms == 4:
        monthme.delete(0, END)
        monthme.insert(0, "Wednesday")
    if ssms == 5:
        monthme.delete(0, END)
        monthme.insert(0, "Thursday")
    if ssms == 6:
        monthme.delete(0, END)
        monthme.insert(0, "Friday")
    if ssms == 7:
        monthme.delete(0, END)
        monthme.insert(0, "Saturday")

def manwback():
    managel.config(text = 'Manage:')
    monthar.place_forget()
    monthal.place_forget()
    monthme.place_forget()
    mannexts.place_forget()
    manbacks.place_forget()
    mans.place(relx = .5, rely = .3, anchor = 'center')
    manback.place(relx = .5, rely = .6, anchor = 'center')
    manw.place(relx = .5, rely = .5, anchor = 'center')
    many.place(relx = .5, rely = .4, anchor = 'center')
    root.unbind("<KeyPress-Left>")
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Down>")
    root.bind("<KeyPress-Up>", lambda e: manau())
    root.bind("<KeyPress-Down>", lambda e: manad())
    root.bind("<Return>", lambda e: manwf())

def mansf():
    global monthar, monthal, monthme, dayme, dayal, dayar, ssms, sdc, mannexts, manbacks, msa
    ssms = 1
    sdc = 1
    msa = 1
    root.unbind("<Return>")
    root.bind('<KeyPress-Up>', lambda e: mansau())
    root.bind('<KeyPress-Down>', lambda e: mansad())
    root.bind('<KeyPress-Left>', lambda e: smanmonthl())
    root.bind('<KeyPress-Right>', lambda e: smanmonthr())
    mans.place_forget()
    many.place_forget()
    manw.place_forget()
    managel.config(text = 'Choose Your Date')
    manback.place_forget()
    monthar = Button(root, image = rightapic2, bg = color, relief = FLAT, command = smanmonthr)
    monthal = Button(root, image = leftapic2, bg = color, relief = FLAT, command = smanmonthl)
    monthal.place(relx = .3, rely = .35, anchor = 'center')
    monthar.place(relx = .7, rely = .35, anchor = 'center')
    monthme = Entry(root, exportselection=0, width = 12, font = ("arial", 15), fg = "dark Blue", relief = RAISED, bd = 10)
    monthme.place(relx = .5, rely = .35, anchor="center")
    monthme.insert(0, "January")
    dayme = Entry(root, exportselection=0, width = 12, font = ("arial", 15), fg = "blue", relief = RAISED, bd = 10)
    dayme.place(relx = .5, rely = .50, anchor="center")
    dayme.insert(0, "1")
    dayar = Button(root, image = rightapic2, bg = color, relief = FLAT, command = mansdayr)
    dayal = Button(root, image = leftapic2, bg = color, relief = FLAT, command = mansdayl)
    dayal.place(relx = .3, rely = .50, anchor = 'center')
    dayar.place(relx = .7, rely = .50, anchor = 'center')
    mannexts = Button(root, text = 'Next', font = ('arial', 15), fg = 'blue', bg = 'light grey', command = mansic)
    mannexts.place(relx = .5, rely = .65, anchor = 'center')
    manbacks = Button(root, text = 'Back', font = ('arial', 15), fg = 'blue', bg = 'light grey', command = mansback)
    manbacks.place(relx = .5, rely = .75, anchor = 'center')

def mansad():
    global msa
    msa = msa + 1
    if msa == 0:
       msa = msa + 1
    if msa == 5:
       msa = msa - 1
    if msa == 1:
       monthme.config(fg = 'dark blue')
       dayme.config(fg = 'blue')
       mannexts.config(bg = 'light grey', fg = 'blue')
       manbacks.config(bg = 'light grey', fg = 'blue')
       root.unbind("<Return>")
       root.bind('<KeyPress-Left>', lambda e: smanmonthl())
       root.bind('<KeyPress-Right>', lambda e: smanmonthr())
    if msa == 2:
       dayme.config(fg = 'dark blue')
       monthme.config(fg = 'blue')
       mannexts.config(bg = 'light grey', fg = 'blue')
       manbacks.config(bg = 'light grey', fg = 'blue')
       root.unbind("<Return>")
       root.bind('<KeyPress-Left>', lambda e: mansdayl())
       root.bind('<KeyPress-Right>', lambda e: mansdayr())
    if msa == 3:
       dayme.config(fg = 'blue')
       monthme.config(fg = 'blue')
       mannexts.config(bg = 'blue', fg = 'light grey')
       manbacks.config(bg = 'light grey', fg = 'blue')
       root.bind("<Return>", lambda e: mansic())
       root.unbind('<KeyPress-Left>')
       root.unbind('<KeyPress-Right>')
    if msa == 4:
       dayme.config(fg = 'blue')
       monthme.config(fg = 'blue')
       mannexts.config(fg = 'blue', bg = 'light grey')
       manbacks.config(fg = 'light grey', bg = 'blue')
       root.bind("<Return>", lambda e: mansback())
       root.unbind('<KeyPress-Left>')
       root.unbind('<KeyPress-Right>')

def mansau():
    global msa
    msa = msa - 1
    if msa == 0:
       msa = msa + 1
    if msa == 5:
       msa = msa - 1
    if msa == 1:
       monthme.config(fg = 'dark blue')
       dayme.config(fg = 'blue')
       mannexts.config(bg = 'light grey', fg = 'blue')
       manbacks.config(bg = 'light grey', fg = 'blue')
       root.unbind("<Return>")
       root.bind('<KeyPress-Left>', lambda e: smanmonthl())
       root.bind('<KeyPress-Right>', lambda e: smanmonthr())
    if msa == 2:
       dayme.config(fg = 'dark blue')
       monthme.config(fg = 'blue')
       mannexts.config(bg = 'light grey', fg = 'blue')
       manbacks.config(bg = 'light grey', fg = 'blue')
       root.unbind("<Return>")
       root.bind('<KeyPress-Left>', lambda e: mansdayl())
       root.bind('<KeyPress-Right>', lambda e: mansdayr())
    if msa == 3:
       dayme.config(fg = 'blue')
       monthme.config(fg = 'blue')
       mannexts.config(bg = 'blue', fg = 'light grey')
       manbacks.config(bg = 'light grey', fg = 'blue')
       root.bind("<Return>", lambda e: mansic())
       root.unbind('<KeyPress-Left>')
       root.unbind('<KeyPress-Right>')
    if msa == 4:
       dayme.config(fg = 'blue')
       monthme.config(fg = 'blue')
       mannexts.config(fg = 'blue', bg = 'light grey')
       manbacks.config(fg = 'light grey', bg = 'blue')
       root.bind("<Return>", lambda e: mansback())
       root.unbind('<KeyPress-Left>')
       root.unbind('<KeyPress-Right>')

def mansback():
    managel.config(text = 'Manage:')
    monthar.place_forget()
    monthal.place_forget()
    monthme.place_forget()
    dayme.place_forget()
    dayal.place_forget()
    dayar.place_forget()
    mannexts.place_forget()
    manbacks.place_forget()
    mans.place(relx = .5, rely = .3, anchor = 'center')
    manback.place(relx = .5, rely = .6, anchor = 'center')
    manw.place(relx = .5, rely = .5, anchor = 'center')
    many.place(relx = .5, rely = .4, anchor = 'center')
    root.unbind("<KeyPress-Left>")
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Down>")
    root.bind("<KeyPress-Up>", lambda e: manau())
    root.bind("<KeyPress-Down>", lambda e: manad())
    root.bind("<Return>", lambda e: mansf())

def mansep():
    global sed, seets, sede, sedd, dem, manfile, manshback, mansa
    mansa = 1
    managel.config(text = 'Manage:')
    monthar.place_forget()
    monthal.place_forget()
    monthme.place_forget()
    dayme.place_forget()
    dayal.place_forget()
    dayar.place_forget()
    mannexts.place_forget()
    manbacks.place_forget()
    root.bind("<Return>", lambda e: manssubt())
    root.unbind("<KeyPress-Left>")
    root.unbind("<KeyPress-Right>")
    root.bind("<KeyPress-Up>", lambda e: mansharrowu())
    root.bind("<KeyPress-Down>", lambda e: mansharrowd())
    try:
       manfile = open('{}.txt'.format(dinput), mode='r+')
       manfiletext = manfile.read()
       manfile.close()
    except:
       manfiletext = 'No Single Event'
    sedd = Label(root, text = '{} {}'.format(minput, dinput), bg = 'white', fg = 'blue', font = ('arial', 20))
    sedd.place(relx = .5, rely = .3, anchor='center')
    sed = Entry(root, width = '15', fg = 'blue', exportselection=0, bd = 10, font = ('arial', 15), relief = RAISED)
    sed.place(relx = .5, rely = .4, anchor='center')
    sed.delete(0, END)
    sed.insert(0, manfiletext)
    seets = Button(root, text = 'Submit Text', font = ('arial', 15), fg = 'light grey', bg = 'blue', command = manssubt)
    seets.place(relx = .5, rely = .5, anchor = 'center')
    sede = Button(root, text = 'Delete Event', font = ('arial', 15), bg = 'light grey', fg = 'blue', command = mansdele)
    sede.place(relx = .5, rely = .6, anchor = 'center')
    dem = Button(root, text = 'Delete All {} Events'.format(minput), font = ('arial', 15), bg = 'light grey', fg = 'blue', command = mansdelm)
    dem.place(relx = .5, rely = .7, anchor = 'center')
    manshback = Button(root, text = 'Back'.format(minput), font = ('arial', 15), bg = 'light grey', fg = 'blue', command = mansdcback)
    manshback.place(relx = .5, rely = .8, anchor = 'center')

def mansharrowu():
   global mansa
   mansa = mansa - 1
   if mansa == 5:
      mansa = mansa - 1
   if mansa == 0:
      mansa = mansa + 1
   if mansa == 1:
      seets.config(bg = 'blue', fg = 'light grey')
      sede.config(fg = 'blue', bg = 'light grey')
      dem.config(fg = 'blue', bg = 'light grey')
      manshback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manssubt())
   if mansa == 2:
      sede.config(bg = 'blue', fg = 'light grey')
      seets.config(fg = 'blue', bg = 'light grey')
      dem.config(fg = 'blue', bg = 'light grey')
      manshback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: mansdele())
   if mansa == 3:
      dem.config(bg = 'blue', fg = 'light grey')
      sede.config(fg = 'blue', bg = 'light grey')
      seets.config(fg = 'blue', bg = 'light grey')
      manshback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: mansdelm())
   if mansa == 4:
      manshback.config(bg = 'blue', fg = 'light grey')
      sede.config(fg = 'blue', bg = 'light grey')
      dem.config(fg = 'blue', bg = 'light grey')
      seets.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: mansdcback())

def mansharrowd():
   global mansa
   mansa = mansa + 1
   if mansa == 5:
      mansa = mansa - 1
   if mansa == 0:
      mansa = mansa + 1
   if mansa == 1:
      seets.config(bg = 'blue', fg = 'light grey')
      sede.config(fg = 'blue', bg = 'light grey')
      dem.config(fg = 'blue', bg = 'light grey')
      manshback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: manssubt())
   if mansa == 2:
      sede.config(bg = 'blue', fg = 'light grey')
      seets.config(fg = 'blue', bg = 'light grey')
      dem.config(fg = 'blue', bg = 'light grey')
      manshback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: mansdele())
   if mansa == 3:
      dem.config(bg = 'blue', fg = 'light grey')
      sede.config(fg = 'blue', bg = 'light grey')
      seets.config(fg = 'blue', bg = 'light grey')
      manshback.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: mansdelm())
   if mansa == 4:
      manshback.config(bg = 'blue', fg = 'light grey')
      sede.config(fg = 'blue', bg = 'light grey')
      dem.config(fg = 'blue', bg = 'light grey')
      seets.config(fg = 'blue', bg = 'light grey')
      root.bind("<Return>", lambda e: mansdcback())

def mansdcback():
    os.chdir('..')
    os.chdir('..')
    sedd.place_forget()
    sed.place_forget()
    seets.place_forget()
    sede.place_forget()
    dem.place_forget()
    manshback.place_forget()
    mans.place(relx = .5, rely = .3, anchor = 'center')
    manback.place(relx = .5, rely = .6, anchor = 'center')
    manw.place(relx = .5, rely = .5, anchor = 'center')
    many.place(relx = .5, rely = .4, anchor = 'center')
    root.unbind("<KeyPress-Left>")
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Down>")
    root.bind("<KeyPress-Up>", lambda e: manau())
    root.bind("<KeyPress-Down>", lambda e: manad())
    root.bind("<Return>", lambda e: mansf())

def manssubt():
   sedtext = sed.get()
   if sedtext == 'No Single Event':
      sed.delete(0, END)
      sed.insert(0, 'Invalid Event')
   elif sedtext == 'Invalid Event':
      sed.delete(0, END)
      sed.insert(0, 'Invalid Event')
   else:
      mansfilewrite = open('{}.txt'.format(dinput), mode='w')
      mansfilewrite.write(sedtext)
      messagebox.showinfo("Edit Completed", "Your event has sucsessfully been changed")

def mansdele():
   delec = messagebox.askquestion("Confirmation","Are you sure you want to delete your event?", icon='warning')
   if 'yes':
      try:
         os.remove('{}.txt'.format(dinput))
         manfiletext = 'No Single Event'
         sed.delete(0, END)
         sed.insert(0, manfiletext)
      except:
         manfiletext = 'No Single Event'
         sed.delete(0, END)
         sed.insert(0, manfiletext)
      messagebox.showinfo("Deletion Completed", "Your event has sucsessfully been deleted")

def mansdelm():
   delec = messagebox.askquestion("Confirmation","Are you sure you want to delete all your {} events?".format(minput), icon='warning')
   if 'yes':
      eventlist = os.listdir()   
      for event in eventlist:
         os.remove(event)
      messagebox.showinfo("Deletion Completed", "Your events have sucsessfully been deleted")

def mansdayv():
   global dmax, dinput
   dmax = dmax - 2
   dinputl = dayme.get()
   try:
      dinput = int(dinputl)
      dayint = True
   except ValueError:
      dayint = False
   if dayint == True and dinput > dmax:
      dayme.delete(0, END)
      dayme.insert(0, 'Invalid Day')
   elif dayint == True and dinput < 1:
      dayme.delete(0, END)
      dayme.insert(0, 'Invalid Day')
   elif dayint == False:
      dayme.delete(0, END)
      dayme.insert(0, 'Invalid Day')
   else:
      os.chdir('months')
      os.chdir(minput)
      mansep()


def mansic():
    global dmax, leap, minput, ssms, msa
    mansmonth = monthme.get()
    minput = mansmonth.lower()
    if minput == 'january':
        dmax = 32
        mansdayv()
    elif minput == 'february':
        if leap == True:
            dmax = 30
        elif leap == False:
            dmax = 29
        else:
            tkMessageBox.showwarning("Leap Year Error", "Could not correctly get the leap year dates, please retry")
        mansdayv()
    elif minput == 'march':
        dmax = 32
        mansdayv()
    elif minput == 'april':
        dmax = 31
        mansdayv()
    elif minput == 'may':
        dmax = 32
        mansdayv()
    elif minput == 'june':
        dmax = 31
        mansdayv()
    elif minput == 'july':
        dmax = 32
        mansdayv()
    elif minput == 'august':
        dmax = 32
        mansdayv()
    elif minput == 'september':
        mansdayv()
    elif minput == 'october':
        dmax = 32
        mansdayv()
    elif minput == 'november':
        dmax = 31
        mansdayv()
    elif minput == 'december':
        dmax = 32
        mansdayv()
    else:
        monthme.delete(0, END)
        monthme.insert(0, "Invalid Month")
    
def mansdayr():
    global sdc
    sdc = sdc + 1
    if sdc == 0:
        sdc = sdc + 1
    if sdc == 32:
        sdc = sdc - 1
    dayme.delete(0, END)
    dayme.insert(0, sdc)

def mansdayl():
    global sdc
    sdc = sdc - 1
    if sdc == 0:
        sdc = sdc + 1
    if sdc == 32:
        sdc = sdc - 1
    dayme.delete(0, END)
    dayme.insert(0, sdc)

def smanmonthr():
    global ssms
    ssms = ssms + 1
    if ssms == 0:
        ssms = ssms + 1
    if ssms == 13:
        ssms = ssms - 1
    if ssms == 1:
        monthme.delete(0, END)
        monthme.insert(0, "January")
    if ssms == 2:
        monthme.delete(0, END)
        monthme.insert(0, "February")
    if ssms == 3:
        monthme.delete(0, END)
        monthme.insert(0, "March")
    if ssms == 4:
        monthme.delete(0, END)
        monthme.insert(0, "April")
    if ssms == 5:
        monthme.delete(0, END)
        monthme.insert(0, "May")
    if ssms == 6:
        monthme.delete(0, END)
        monthme.insert(0, "June")
    if ssms == 7:
        monthme.delete(0, END)
        monthme.insert(0, "July")
    if ssms == 8:
        monthme.delete(0, END)
        monthme.insert(0, "August")
    if ssms == 9:
        monthme.delete(0, END)
        monthme.insert(0, "September")
    if ssms == 10:
        monthme.delete(0, END)
        monthme.insert(0, "October")
    if ssms == 11:
        monthme.delete(0, END)
        monthme.insert(0, "November")
    if ssms == 12:
        monthme.delete(0, END)
        monthme.insert(0, "December")

def smanmonthl():
    global ssms
    ssms = ssms - 1
    if ssms == 0:
        ssms = ssms + 1
    if ssms == 13:
        ssms = ssms - 1
    if ssms == 1:
        monthme.delete(0, END)
        monthme.insert(0, "January")
    if ssms == 2:
        monthme.delete(0, END)
        monthme.insert(0, "February")
    if ssms == 3:
        monthme.delete(0, END)
        monthme.insert(0, "March")
    if ssms == 4:
        monthme.delete(0, END)
        monthme.insert(0, "April")
    if ssms == 5:
        monthme.delete(0, END)
        monthme.insert(0, "May")
    if ssms == 6:
        monthme.delete(0, END)
        monthme.insert(0, "June")
    if ssms == 7:
        monthme.delete(0, END)
        monthme.insert(0, "July")
    if ssms == 8:
        monthme.delete(0, END)
        monthme.insert(0, "August")
    if ssms == 9:
        monthme.delete(0, END)
        monthme.insert(0, "September")
    if ssms == 10:
        monthme.delete(0, END)
        monthme.insert(0, "October")
    if ssms == 11:
        monthme.delete(0, END)
        monthme.insert(0, "November")
    if ssms == 12:
        monthme.delete(0, END)
        monthme.insert(0, "December")
    
def manageback():
    if menub == 1:
       root.config(menu=menubar)
    mans.place_forget()
    many.place_forget()
    manw.place_forget()
    managel.place_forget()
    manback.place_forget()
    root.bind("<Return>", lambda e: manage())
    root.bind("<KeyPress-Left>", lambda e: mainarrowl())
    root.bind("<KeyPress-Right>", lambda e: mainarrowr())
    root.bind("<KeyPress-Down>", lambda e: mainarrowd())
    root.bind("<KeyPress-Up>", lambda e: mainarrowu())
    exitb.place(relx = .65, rely = .7, anchor = 'center')
    helpb.place(relx = .5, rely = .7, anchor = 'center')
    neweb.place(relx=.5, rely=.5, anchor="center")
    dayib.place(relx=.3, rely=.5, anchor="center")
    maneb.place(relx=.7, rely=.5, anchor="center")
    setb.place(relx = .35, rely = .7, anchor = 'center')
         

#images
devpic = PhotoImage(file =r"./images/FIREDEV.gif")
if color.lower() == 'black':
   devpic = PhotoImage(file =r"./images/FIREDEVDARK.gif")

logopic = PhotoImage(file =r"./images/logo.gif")
if color.lower() == 'black':
   logopic = PhotoImage(file =r"./images/logoDark.gif")

newlogopic = PhotoImage(file =r"./images/newlogo.gif")
if color.lower() == 'black':
   newlogopic = PhotoImage(file =r"./images/newlogoDark.gif")

rightapic = PhotoImage(file = r"./images/RightArrow.gif")
if color.lower() == 'black':
   rightapic = PhotoImage(file = r"./images/RightArrowDark.gif")
rightapic2 = rightapic.subsample(7,7)

leftapic = PhotoImage(file = r"./images/LeftArrow.gif")
if color.lower() == 'black':
   leftapic = PhotoImage(file = r"./images/LeftArrowDark.gif")
leftapic2 = leftapic.subsample(7,7)

exitpic = PhotoImage(file = r"./images/Exit.gif")
if color.lower() == 'black':
   exitpic = PhotoImage(file = r"./images/ExitDark.gif")
exitpic2 = exitpic.subsample(8,8)

helppic = PhotoImage(file = r"./images/Help.gif")
if color.lower() == 'black':
   helppic = PhotoImage(file = r"./images/HelpDark.gif")
helppic2 = helppic.subsample(8,8)

setpic = PhotoImage(file = r"./images/Settings.gif")
if color.lower() == 'black':
   setpic = PhotoImage(file = r"./images/SettingsDark.gif")
setpic2 = setpic.subsample(8,8)

#starting screen
devl = Label(root, image = devpic, bg = color)
devl.pack(side = BOTTOM, fill = X)

logol = Label(root, image = logopic, bg = color)
logol.pack(side = TOP, fill = X)

neweb = Button(root, text = "New Event", font = ("arial", 15),  bg = "blue", fg = "light grey", command = seth)
neweb.place(relx=.5, rely=.5, anchor="center")

dayib = Button(root, text = "Daily Info", font = ("arial", 15),  fg = "blue", bg = "light grey", command = dayi)
dayib.place(relx=.3, rely=.5, anchor="center")

maneb = Button(root, text = "Manage", font = ("arial", 15),  fg = "blue", bg = "light grey", command = manage)
maneb.place(relx=.7, rely=.5, anchor="center")

exitb = Button(root, image = exitpic2, fg = 'light grey', bd = 10, bg = 'light grey', command = exitf)
exitb.place(relx = .65, rely = .7, anchor = 'center')

helpb = Button(root, image = helppic2, fg = 'light grey', bd = 10, bg = 'light grey', command = helpf)
helpb.place(relx = .5, rely = .7, anchor = 'center')

setb = Button(root, image = setpic2, bd = 10, bg = 'light grey', command = setf)
setb.place(relx = .35, rely = .7, anchor = 'center')


#key binds
root.bind("<KeyPress-Left>", lambda e: mainarrowl())
root.bind("<KeyPress-Down>", lambda e: mainarrowd())
root.bind("<KeyPress-Up>", lambda e: mainarrowu())
root.bind("<KeyPress-Right>", lambda e: mainarrowr())
root.bind("<Return>", lambda e: seth())

def mainarrowl():
    global mas, suds
    mas = mas - 1
    if mas == 4:
        mas = mas - 1
    if mas == 0:
        mas = mas + 1
    if mas == 1 and suds == 1:
        dayib.config(bg = "blue", fg = "light grey")
        neweb.config(fg = "blue", bg = "light grey")
        maneb.config(fg = "blue", bg = "light grey")
        exitb.config(fg = 'light grey', bg = 'light grey')
        setb.config(fg = 'light grey', bg = 'light grey')
        helpb.config(fg = 'light grey', bg = 'light grey')
        root.bind("<Return>", lambda e: dayi())
    if mas == 2 and suds == 1:
        neweb.config(bg = "blue", fg = "light grey")
        dayib.config(fg = "blue", bg = "light grey")
        maneb.config(fg = "blue", bg = "light grey")
        exitb.config(fg = 'light grey', bg = 'light grey')
        setb.config(fg = 'light grey', bg = 'light grey')
        helpb.config(fg = 'light grey', bg = 'light grey')
        root.bind("<Return>", lambda e: seth())
    if mas == 3 and suds == 1:
        maneb.config(bg = "blue", fg = "light grey")
        dayib.config(fg = "blue", bg = "light grey")
        neweb.config(fg = "blue", bg = "light grey")
        exitb.config(fg = 'light grey', bg = 'light grey')
        setb.config(fg = 'light grey', bg = 'light grey')
        helpb.config(fg = 'light grey', bg = 'light grey')
        root.bind("<Return>", lambda e: manage())
    if mas == 1 and suds == 2:
       setb.config(bg = 'blue')
       helpb.config(fg = 'light grey', bg = 'light grey')
       exitb.config(fg = 'light grey', bg = 'light grey')
       dayib.config(fg = "blue", bg = "light grey")
       neweb.config(fg = "blue", bg = "light grey")
       maneb.config(fg = "blue", bg = "light grey")
       root.bind("<Return>", lambda e: setf())
    if mas == 2 and suds == 2:
       helpb.config(bg = 'blue')
       exitb.config(fg = 'light grey', bg = 'light grey')
       setb.config(fg = 'light grey', bg = 'light grey')
       dayib.config(fg = "blue", bg = "light grey")
       neweb.config(fg = "blue", bg = "light grey")
       maneb.config(fg = "blue", bg = "light grey")
       root.bind("<Return>", lambda e: helpf())
    if mas == 3 and suds == 2:
       exitb.config(bg = 'blue')
       helpb.config(fg = 'light grey', bg = 'light grey')
       setb.config(fg = 'light grey', bg = 'light grey')
       dayib.config(fg = "blue", bg = "light grey")
       neweb.config(fg = "blue", bg = "light grey")
       maneb.config(fg = "blue", bg = "light grey")
       root.bind("<Return>", lambda e: exitf())
       

def mainarrowd():
    global mas, suds
    suds = suds + 1
    if suds == 3:
        suds = suds - 1
    if suds == 0:
        suds = suds + 1
    if mas == 1 and suds == 1:
        dayib.config(bg = "blue", fg = "light grey")
        neweb.config(fg = "blue", bg = "light grey")
        maneb.config(fg = "blue", bg = "light grey")
        exitb.config(fg = 'light grey', bg = 'light grey')
        setb.config(fg = 'light grey', bg = 'light grey')
        helpb.config(fg = 'light grey', bg = 'light grey')
        root.bind("<Return>", lambda e: dayi())
    if mas == 2 and suds == 1:
        neweb.config(bg = "blue", fg = "light grey")
        dayib.config(fg = "blue", bg = "light grey")
        maneb.config(fg = "blue", bg = "light grey")
        exitb.config(fg = 'light grey', bg = 'light grey')
        setb.config(fg = 'light grey', bg = 'light grey')
        helpb.config(fg = 'light grey', bg = 'light grey')
        root.bind("<Return>", lambda e: seth())
    if mas == 3 and suds == 1:
        maneb.config(bg = "blue", fg = "light grey")
        dayib.config(fg = "blue", bg = "light grey")
        neweb.config(fg = "blue", bg = "light grey")
        exitb.config(fg = 'light grey', bg = 'light grey')
        setb.config(fg = 'light grey', bg = 'light grey')
        helpb.config(fg = 'light grey', bg = 'light grey')
        root.bind("<Return>", lambda e: manage())
    if mas == 1 and suds == 2:
       setb.config(bg = 'blue')
       helpb.config(fg = 'light grey', bg = 'light grey')
       exitb.config(fg = 'light grey', bg = 'light grey')
       dayib.config(fg = "blue", bg = "light grey")
       neweb.config(fg = "blue", bg = "light grey")
       maneb.config(fg = "blue", bg = "light grey")
       root.bind("<Return>", lambda e: setf())
    if mas == 2 and suds == 2:
       helpb.config(bg = 'blue')
       exitb.config(fg = 'light grey', bg = 'light grey')
       setb.config(fg = 'light grey', bg = 'light grey')
       dayib.config(fg = "blue", bg = "light grey")
       neweb.config(fg = "blue", bg = "light grey")
       maneb.config(fg = "blue", bg = "light grey")
       root.bind("<Return>", lambda e: helpf())
    if mas == 3 and suds == 2:
       exitb.config(bg = 'blue')
       helpb.config(fg = 'light grey', bg = 'light grey')
       setb.config(fg = 'light grey', bg = 'light grey')
       dayib.config(fg = "blue", bg = "light grey")
       neweb.config(fg = "blue", bg = "light grey")
       maneb.config(fg = "blue", bg = "light grey")
       root.bind("<Return>", lambda e: exitf())

def mainarrowu():
    global mas, suds
    suds = suds - 1
    if suds == 3:
        suds = suds - 1
    if suds == 0:
        suds = suds + 1
    if mas == 1 and suds == 1:
        dayib.config(bg = "blue", fg = "light grey")
        neweb.config(fg = "blue", bg = "light grey")
        maneb.config(fg = "blue", bg = "light grey")
        exitb.config(fg = 'light grey', bg = 'light grey')
        setb.config(fg = 'light grey', bg = 'light grey')
        helpb.config(fg = 'light grey', bg = 'light grey')
        root.bind("<Return>", lambda e: dayi())
    if mas == 2 and suds == 1:
        neweb.config(bg = "blue", fg = "light grey")
        dayib.config(fg = "blue", bg = "light grey")
        maneb.config(fg = "blue", bg = "light grey")
        exitb.config(fg = 'light grey', bg = 'light grey')
        setb.config(fg = 'light grey', bg = 'light grey')
        helpb.config(fg = 'light grey', bg = 'light grey')
        root.bind("<Return>", lambda e: seth())
    if mas == 3 and suds == 1:
        maneb.config(bg = "blue", fg = "light grey")
        dayib.config(fg = "blue", bg = "light grey")
        neweb.config(fg = "blue", bg = "light grey")
        exitb.config(fg = 'light grey', bg = 'light grey')
        setb.config(fg = 'light grey', bg = 'light grey')
        helpb.config(fg = 'light grey', bg = 'light grey')
        root.bind("<Return>", lambda e: manage())
    if mas == 1 and suds == 2:
       setb.config(bg = 'blue')
       helpb.config(fg = 'light grey', bg = 'light grey')
       exitb.config(fg = 'light grey', bg = 'light grey')
       dayib.config(fg = "blue", bg = "light grey")
       neweb.config(fg = "blue", bg = "light grey")
       maneb.config(fg = "blue", bg = "light grey")
       root.bind("<Return>", lambda e: setf())
    if mas == 2 and suds == 2:
       helpb.config(bg = 'blue')
       exitb.config(fg = 'light grey', bg = 'light grey')
       setb.config(fg = 'light grey', bg = 'light grey')
       dayib.config(fg = "blue", bg = "light grey")
       neweb.config(fg = "blue", bg = "light grey")
       maneb.config(fg = "blue", bg = "light grey")
       root.bind("<Return>", lambda e: helpf())
    if mas == 3 and suds == 2:
       exitb.config(bg = 'blue')
       helpb.config(fg = 'light grey', bg = 'light grey')
       setb.config(fg = 'light grey', bg = 'light grey')
       dayib.config(fg = "blue", bg = "light grey")
       neweb.config(fg = "blue", bg = "light grey")
       maneb.config(fg = "blue", bg = "light grey")
       root.bind("<Return>", lambda e: exitf())

def mainarrowr():
    global mas, suds
    mas = mas + 1
    if mas == 4:
        mas = mas - 1
    if mas == 0:
        mas = mas + 1
    if mas == 1 and suds == 1:
        dayib.config(bg = "blue", fg = "light grey")
        neweb.config(fg = "blue", bg = "light grey")
        maneb.config(fg = "blue", bg = "light grey")
        exitb.config(fg = 'light grey', bg = 'light grey')
        setb.config(fg = 'light grey', bg = 'light grey')
        helpb.config(fg = 'light grey', bg = 'light grey')
        root.bind("<Return>", lambda e: dayi())
    if mas == 2 and suds == 1:
        neweb.config(bg = "blue", fg = "light grey")
        dayib.config(fg = "blue", bg = "light grey")
        maneb.config(fg = "blue", bg = "light grey")
        exitb.config(fg = 'light grey', bg = 'light grey')
        setb.config(fg = 'light grey', bg = 'light grey')
        helpb.config(fg = 'light grey', bg = 'light grey')
        root.bind("<Return>", lambda e: seth())
    if mas == 3 and suds == 1:
        maneb.config(bg = "blue", fg = "light grey")
        dayib.config(fg = "blue", bg = "light grey")
        neweb.config(fg = "blue", bg = "light grey")
        exitb.config(fg = 'light grey', bg = 'light grey')
        setb.config(fg = 'light grey', bg = 'light grey')
        helpb.config(fg = 'light grey', bg = 'light grey')
        root.bind("<Return>", lambda e: manage())
    if mas == 1 and suds == 2:
       setb.config(bg = 'blue')
       helpb.config(fg = 'light grey', bg = 'light grey')
       exitb.config(fg = 'light grey', bg = 'light grey')
       dayib.config(fg = "blue", bg = "light grey")
       neweb.config(fg = "blue", bg = "light grey")
       maneb.config(fg = "blue", bg = "light grey")
       root.bind("<Return>", lambda e: setf())
    if mas == 2 and suds == 2:
       helpb.config(bg = 'blue')
       exitb.config(fg = 'light grey', bg = 'light grey')
       setb.config(fg = 'light grey', bg = 'light grey')
       dayib.config(fg = "blue", bg = "light grey")
       neweb.config(fg = "blue", bg = "light grey")
       maneb.config(fg = "blue", bg = "light grey")
       root.bind("<Return>", lambda e: helpf())
    if mas == 3 and suds == 2:
       exitb.config(bg = 'blue')
       helpb.config(fg = 'light grey', bg = 'light grey')
       setb.config(fg = 'light grey', bg = 'light grey')
       dayib.config(fg = "blue", bg = "light grey")
       neweb.config(fg = "blue", bg = "light grey")
       maneb.config(fg = "blue", bg = "light grey")
       root.bind("<Return>", lambda e: exitf())

#menubar
def rmenub():
   global menub
   emptyMenu = Menu(root)
   root.config(menu=emptyMenu)
   menub = 0

def singemenu():
    global singli, singlme, ssms, subsing, singra, singla, singback, ses, newlogol, seto, sety, setw, setback
    ssms = 1
    ses = 1
    emptyMenu = Menu(root)
    root.config(menu=emptyMenu)
    root.unbind("<KeyPress-Left>")
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Down>")
    neweb.place_forget()
    dayib.place_forget()
    maneb.place_forget()
    exitb.place_forget()
    helpb.place_forget()
    setb.place_forget()
    logol.pack_forget()
    newlogol = Label(root, image = newlogopic, bg = color)
    newlogol.pack(side = TOP, fill = X)
    setback = Button(root, fg = "blue", bg = "Light Grey", font = ("arial", 15), text = "Back", command = setbackf)
    setw = Button(root, fg = "blue", bg = "Light Grey", font = ("arial", 15), text = "Weekly Event", command = setwf)
    sety = Button(root, fg = "blue", bg = "Light Grey", font = ("arial", 15), text = "Yearly Event", command = setyf)
    seto = Button(root, bg = "blue", fg = "Light Grey", font = ("arial", 15), text = "Single Event", command = setnewn)
    root.unbind("<KeyPress-Down>")
    root.unbind("<KeyPress-Up>")
    singli = Label(text = "Choose Your Month:", font = ("airal", 20), bg = color, fg = "blue")
    singli.place(relx = .5, rely = .2, anchor="center")
    singlme = Entry(root, exportselection=0, width = 12, font = ("arial", 15), fg = "Blue", relief = RAISED, bd = 10)
    singlme.place(relx = .5, rely = .4, anchor="center")
    singlme.insert(0, "January")
    subsing = Button(root, text = "Next", font = ("arial", 15), bg = "blue", fg = "light grey", command = setnsday)
    subsing.place(relx = .5, rely = .5, anchor="center")
    singra = Button(root, image = rightapic2, bg = color, relief = FLAT, command = singmar)
    singra.place(relx = .7, rely = .4, anchor="center")
    singla = Button(root, image = leftapic2, bg = color, relief = FLAT, command = singmal)
    singla.place(relx = .3, rely = .4, anchor="center")
    singback = Button(root, text = "Back", font = ("arial", 15), fg = "blue", bg = "light grey", command = setnewnback)
    singback.place(relx = .5, rely = .6, anchor="center")
    root.bind("<KeyPress-Left>", lambda e: singmal())
    root.bind("<KeyPress-Right>", lambda e: singmar())
    root.bind("<KeyPress-Down>", lambda e: setnsad())
    root.bind("<KeyPress-Up>", lambda e: setnsau())
    root.bind("<Return>", lambda e: setnsday())

def weekemenu():
    global singli, singlme, subsing, singra, singla, singback, swes, swbs, seto, sety, setw, setback, newlogol, sms
    swes = 1
    swbs = 1
    sms = 3
    emptyMenu = Menu(root)
    root.config(menu=emptyMenu)
    root.unbind("<KeyPress-Left>")
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Down>")
    neweb.place_forget()
    dayib.place_forget()
    maneb.place_forget()
    exitb.place_forget()
    helpb.place_forget()
    setb.place_forget()
    logol.pack_forget()
    setback = Button(root, fg = "blue", bg = "Light Grey", font = ("arial", 15), text = "Back", command = setbackf)
    setw = Button(root, fg = "light grey", bg = "blue", font = ("arial", 15), text = "Weekly Event", command = setwf)
    sety = Button(root, fg = "blue", bg = "Light Grey", font = ("arial", 15), text = "Yearly Event", command = setyf)
    seto = Button(root, bg = "light grey", fg = "blue", font = ("arial", 15), text = "Single Event", command = setnewn)
    newlogol = Label(root, image = newlogopic, bg = color)
    newlogol.pack(side = TOP, fill = X)
    singli = Label(text = "Choose Your Day:", font = ("airal", 20), bg = color, fg = "blue")
    singli.place(relx = .5, rely = .2, anchor="center")
    singlme = Entry(root, exportselection=0, width = 12, font = ("arial", 15), fg = "Blue", relief = RAISED, bd = 10)
    singlme.place(relx = .5, rely = .4, anchor="center")
    singlme.insert(0, "Sunday")
    subsing = Button(root, text = "Next", font = ("arial", 15), bg = "blue", fg = "light grey", command = setwnext)
    subsing.place(relx = .5, rely = .5, anchor="center")
    singra = Button(root, image = rightapic2, bg = color, relief = FLAT, command = setwwsr)
    singra.place(relx = .7, rely = .4, anchor="center")
    singla = Button(root, image = leftapic2, bg = color, relief = FLAT, command = setwwsl)
    singla.place(relx = .3, rely = .4, anchor="center")
    singback = Button(root, text = "Back", font = ("arial", 15), fg = "blue", bg = "light grey", command = setwback)
    singback.place(relx = .5, rely = .6, anchor="center")
    root.bind("<KeyPress-Left>", lambda e: setwwsl())
    root.bind("<KeyPress-Right>", lambda e: setwwsr())
    root.bind("<KeyPress-Down>", lambda e: setwarrowd())
    root.bind("<KeyPress-Up>", lambda e: setwarrowu())
    root.bind("<Return>", lambda e: setwnext())

def yearemenu():
    global singli, singlme, ssms, subsing, singra, singla, singback, ses, sms, newlogol, seto, sety, setw, setback
    ssms = 1
    ses = 1
    sms = 2
    emptyMenu = Menu(root)
    root.config(menu=emptyMenu)
    root.unbind("<KeyPress-Left>")
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Down>")
    setback = Button(root, fg = "blue", bg = "Light Grey", font = ("arial", 15), text = "Back", command = setbackf)
    setw = Button(root, bg = "light grey", fg = "blue", font = ("arial", 15), text = "Weekly Event", command = setwf)
    sety = Button(root, bg = "blue", fg = "Light Grey", font = ("arial", 15), text = "Yearly Event", command = setyf)
    seto = Button(root, bg = "light grey", fg = "blue", font = ("arial", 15), text = "Single Event", command = setnewn)
    newlogol = Label(root, image = newlogopic, bg = color)
    neweb.place_forget()
    dayib.place_forget()
    maneb.place_forget()
    exitb.place_forget()
    helpb.place_forget()
    setb.place_forget()
    logol.pack_forget()
    newlogol.pack(side = TOP, fill = X)
    singli = Label(text = "Choose Your Yearly Event Month:", font = ("airal", 20), bg = color, fg = "blue")
    singli.place(relx = .5, rely = .2, anchor="center")
    singlme = Entry(root, exportselection=0, width = 12, font = ("arial", 15), fg = "Blue", relief = RAISED, bd = 10)
    singlme.place(relx = .5, rely = .4, anchor="center")
    singlme.insert(0, "January")
    subsing = Button(root, text = "Next", font = ("arial", 15), bg = "blue", fg = "light grey", command = setnsday)
    subsing.place(relx = .5, rely = .5, anchor="center")
    singra = Button(root, image = rightapic2, bg = color, relief = FLAT, command = singmar)
    singra.place(relx = .7, rely = .4, anchor="center")
    singla = Button(root, image = leftapic2, bg = color, relief = FLAT, command = singmal)
    singla.place(relx = .3, rely = .4, anchor="center")
    singback = Button(root, text = "Back", font = ("arial", 15), fg = "blue", bg = "light grey", command = setyback)
    singback.place(relx = .5, rely = .6, anchor="center")
    root.bind("<KeyPress-Left>", lambda e: singmal())
    root.bind("<KeyPress-Right>", lambda e: singmar())
    root.bind("<KeyPress-Down>", lambda e: setyad())
    root.bind("<KeyPress-Up>", lambda e: setyau())
    root.bind("<Return>", lambda e: setydc())


#menubar
if menub == 1:
   menubar = Menu(root)
   menubar.add_command(label="Exit", command = exitf)
   menubar.add_command(label="Daily Info", command = dayi)
   editmenu = Menu(menubar, tearoff=0)
   editmenu.add_command(label="New Event", command=seth)

   editmenu.add_separator()

   editmenu.add_command(label="Single Event", command=singemenu)
   editmenu.add_command(label="Weekly Event", command=weekemenu)
   editmenu.add_command(label="Yearly Event", command=yearemenu)
   menubar.add_cascade(label="New Events", menu=editmenu)

   menubar.add_command(label="Manage", command=manage)

   filemenu = Menu(menubar, tearoff=0)
   filemenu.add_command(label="Remove Menubar", command=rmenub)
   filemenu.add_command(label="Not Permanent")
   menubar.add_cascade(label="Options", menu=filemenu)
   menubar.add_command(label="Settings", command=setf)
   menubar.add_command(label="Help", command=helpf)
   root.config(menu=menubar)

root.iconbitmap('./images/icon.ico')
root.minsize(600, 500)
root.config(bg = color)
root.title("Calendar")
root.geometry("1000x800")
root.mainloop()
