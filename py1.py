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

def greet(person):
    return f"hellow there, {person}"

def divide(a,b):
    if type(a) is int and type(b) is int:
     return a/b
    else:
       return "you dummy"
    
def three_things(a,b,c):
   print("hi")