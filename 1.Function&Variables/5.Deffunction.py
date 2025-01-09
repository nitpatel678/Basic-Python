''' def = define (used for creating a function) '''

# def hello ():
#     print("Hello")

# name = input("Whats your name ?")
# hello()
# print(name)


'''

ANOTHER WAY OF DOING IT
def hello (to):
    print("Hello", to)

name = input("Enter your name : ")
hello(name)

     Same Result     


'''



# def hello(to="world"):
#     print("Hello", to)

# hello()
# name = input("Enter your name : ")
# hello(name)



def main():
    name = input("Enter your name :")
    hello(name)


def hello(to="world"):
    print("Hello", to)

main()