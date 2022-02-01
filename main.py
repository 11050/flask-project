import time
from tkinter import *

def click():
    print('hellow rold')

windows=Tk()

entry=Entry(windows,
            font=("Arial",50),
            show='*'
            )
entry.pack()
submit_button=Button(windows,text='submit',command='submit',state=ACTIVE)

submit_button.pack()

windows.mainloop()


jamol=['Jamol','Sarvar','Diyor']
for i in jamol:
    print(f'{i.title()} hi {i}')
    print(f'actually i cant see you my gorgesous friends{i.lower()}')

food=['mcdonalds','burgerking','kfs']
for i in food:
    print(f'{i.title()}')
    print('i love that food')

animal=['tiger','cat','folk']
for i in animal:
    print(f'every {i.title()} is has own outstanding trait')
    print(f'And i really enjoys with {i}')

for value in range(1,21):
    print(value)
for values in range(1,3,30):
    print(values)

def  favorite_book(name,surname,lastname):
     jamol={
         'name':name,
         'surname':surname,
         'lastname':lastname
     }
     return jamol

nas=favorite_book('jamolldin','sodikov','sayfuddin')
print(nas)

def describe_pet(animal_type,pet_name):
    print(f'{animal_type}')
    print(f'{pet_name.title()}')

describe_pet('tiger','john')
describe_pet('jamol','diyora')
def indicate_name(name,surname,lastname,university):
    print(f'{name.title()} and {surname.lower()}{lastname} {university.title()}')

indicate_name(name='jamol',surname='Sodikov',lastname='sayfuddin',university='wiut')
class dog:

    def __init__(self,name,type,nationality):
                self.name=name
                self.type=type
                self.nationality=nationality


    def say_somthing(self):
        print(f'{self.name} just sit')


    def play_fast(self):
        print(f'{self.name} {self.type} and say please your {self.nationality}')


jamol=dog('dog','deutch','usa')

print(jamol.play_fast())
dog_jamol=dog('name','surnaem','')
dog_jamol.play_fast()

name=dog('jamol','humble','uzbek')
name.play_fast()

class restaraunt:
    def __init__(self,restaruant_type,restaurant_name):
                 self.restaruant_type=restaruant_type
                 self.restaurant_name=restaurant_name


    def describe_restaraunt(self):
        print(f'{self.restaurant_name}{self.restaruant_type}')

    def open_restaraunt(self):
        print(f'{self.restaurant_name}{self.restaruant_type}')


restaraunts=restaraunt('marvarid','italian')
restaraunts.describe_restaraunt()
restaraunt2=restaraunt('basri_baba','turkey')
print(restaraunt2)

jamol=restaraunt('somsaxona','uzbek')
jamol.describe_restaraunt()
jamols=restaraunt('shibildoq','kazax')
jamols.describe_restaraunt()
top=restaraunt('lagmana','china')
top.open_restaraunt()

class car:
    def __init__(self,model,make):
                self.make=make
                self.model=model
                self.re_odemeter=0


    def re_odemeters(self):
        print(f'just calculate{self.re_odemeter}')






say=car('italy','21')
print(say)
say.re_odemeters()
say.re_odemeter=21
say.re_odemeters()


class name:



    def __init__(self,name,surname):
                self.name=name
                self.surname=surname
                self.result=0
                self.miles=2



    def outcome_exams(self):
        print(f'he got we got mistake{self.result}')



wiut=name('jamolldin','sodikov')

wiut.result=20

wiut.outcome_exams()




class new_car:

    def __init__(self,name,model):
                self.name=name
                self.model=model
                self.read_miles=0


    def read_odemeter(self):
        print(f'{self.read_miles}')

    def increment_miles(self,miles):
        self.read_miles += miles

names=new_car('feraray','fast')
print(names)

names.increment_miles(32)
names.read_odemeter()

class number_servered:

     def __init__(self,guest):
             self.guest=guest
             self.serverd=0

     def number_servered(self):
         print(f'{self.serverd}')


jamol=number_servered('jamolldun')
jamol.serverd=21
jamol.number_servered()

class car_service:
    def __init__(self,location,quality):
               self.location=location
               self.quality=quality
               self.server=0

    def how_many_serviced(self):
         print(f'{self.location}{self.server} {self.quality}')




nice=car_service('chilanzar','high')
nice.server=20
nice.how_many_serviced()


class cars:

       def __init__(self,name,price,year):
           self.name=name
           self.price=price
           self.year=year
           self.miles=0



       def get_introduce(self):
         jamol=f'{self.name}{self.price}{self.year}'
         return jamol.title()


       def route_page(self):
           print(f'{self.miles}')



class elector_cars(cars):
    def __init__(self,name,price,year):
        super().__init__(name,price,year)
        self.power=0

    def get_battery(self):
        print(f'{self.power}')

my_tesla=elector_cars('italy',40000,2022)
print(my_tesla.get_introduce())
my_tesla.miles=200
my_tesla.route_page()
my_tesla2=elector_cars('modelx',212,2000)

my_tesla2.power=180
my_tesla2.get_battery()

class Jamol:

    def __init__(self,name,surname,university,batter_car=75):
                self.name=name
                self.surname=surname
                self.university=university
                self.miles=0
                self.batter_car=batter_car
                self.range=0



    def get_kow(self):
        jamol=f'{self.name} {self.surname} {self.university} '


        return  jamol.title()

    def low_income(self):

        print(f'{self.miles}')
    def check_out_power(self):
        if self.batter_car==100:
            range=50
        elif self.batter_car==140:
             range=67
        print(f'{self.range}')





class new_car_jamol(Jamol):

    def __init__(self,name,surname,university):
        super().__init__(name,surname,university)


    def fill_tank(self):
        print(f'this car doesnt have tank to fill')


Sevn=new_car_jamol('jamol','sodikov','wiut')
print(Sevn)
Sevn.miles=100
Sevn.low_income()
Sevn.fill_tank()

Sevn.check_out_power()

class tesla():
      def __init__(self,name,surname):
                 self.name=name
                 self.surname=surname
                 self.read_km=0

      def  read_ls(self):
          print(f'{self.read_km}')

      def  read_info(self):
           stay=f'{self.name}{self.surname}'

           return stay.title()

class tesla_1(tesla):
    def __init__(self,name,surname):
        super().__init__(name,surname)

    def get_fill_tank(self):
        print(f'{self.name} {self.surname} {self.read_km}')


class new_pay():
      def __init__(self,name,type):
                 self.name=name
                 self.type=type
                 self.world=0

      def get_in(self):
           print(f'{self.world}')


class new_pay1(new_pay):
      def __init__(self,name,surname):
          super().__init__(name,surname)

      def get_fill(self):
          print(f'{self.name} {self.surname}{self.world}')
from random import choice

car_type=['tesla','malibu','equinox','tahoy']
ca=choice(car_type)
print(ca)
jamol=21
sarvar=22
shokjahon=25
if jamol>=21:
    print('you accept to fill aplication work travel jamol')
elif sarvar>=21:
    print('you accept to fill aplication to work travel sarcaar')
else:
    print('its horriabl none of aged 21')
jamol=['Shakzoda','Diyora','Beknora']
if 'Diyoras' in jamol:
    print('hi Diyora')
elif 'Beknoras' in jamol:
    print('hi Beknora')
else: print('hi Shakzoda')

alien_color=['green','yellow','red']
if 'green' in alien_color:
    print('you earn 5')
elif 'yellow' in alien_color:
    print('you earn 10')
else:
    print('you earn red')

age=14

if age>=2:
    print('you are boy')
elif age>=4:
    print('you are child')
elif age>=8:
    print('you school boy')
elif age>=13:
    print('you are teeneger')
else:print('you dumb')

fruets=['banana','orange','apple','pineapple']
if 'banana' in fruets:
    print('you really like banana')
elif 'cherry' in fruets:
    print('you really like cherry')
elif 'orange' in fruets:
        print('you like orange')

else:
    print('you really like apple')

korea=['xuan','lee','jackli']
for i in korea:
    print(f'{korea}')

course=['java','python','C#']
for i in course:
 if i=='java':
    print('sorry we are currently dont have course')
else:
    print(f'but we have course{course[1]} {course[2]} ')

gap=[]
if gap:
    for i in gap:
        print(f'{gap}')
    else:
        print('can you fill please apllcation cuz it is empty')


available=['Jamol','Diyora','Beknora','Shakzoda','Iroda']
busy=['ulfat','aziza','dishi','Beknora']
for i in busy:
    if i in available:
        print(f'adding{i}')
    else:print('tugadi chopildin')

jamol=21

if jamol>=21:
    print('hi Jamol')
elif jamol<=25:
    print('hi child')
else:
    print('hi go')