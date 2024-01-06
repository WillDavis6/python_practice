# num = 0

# while num <= 100:
#     if num == 50:
#         break
#     print(num)
#     num += 10

# print("all Done")

# target = 4
# guess = None

# while guess != target:
#     guess = input("Please enter a guess...")
#     if guess == 'q' or guess == 'quit':
#         break
#     guess = int(guess)

# print("ALL DONE")

# things = ["banana", "licker", "pekachu"]
# for items in things:
#     print(items)

fruit = {"banana", "orange", "potatoe"}
vegie = {"potatoe", "tomatoe"}

def greet(person):
    return f"hellow there, {person}"

def divide(a,b):
    if type(a) is int and type(b) is int:
     return a/b
    else:
       return "you dummy"
    
def three_things(a,b,c):
   print("hi")

def send_email(to_email, from_email, subject, cc, bcc, bosy):
   email="""
    to: {to_email}
    from
"""

def multiply(a,b):
   return a * b


def gen_board(size,inital_val=None):
   return [[intial]]

names = ['charlie', 'lucie']

name1, name2 = names

def getd(person):
   '''
   >>> getd(3)
   0
   
   '''
   try:
      print(3/person)
   except TypeError:
      print('Type error: try another entry')
   except:
      print('something else went wrong')

from math import sqrt
class Triange:
   '''
   a class used to represent a triangle
   '''
   def __init__(self,a,b):
      self.a = a
      self.b = b

   @classmethod
   def random(cls):
      print(cls)


   def get_hypot(self):
      return sqrt(self.a ** 2 + self.b ** 2)
