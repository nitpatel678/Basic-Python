'''  LIAST {Similar to array}  '''
# for i in [0 , 1 ,2]:
#     print("Meow")


'''
for i in range(3):
    print("Meow")

for _ in range(3):
    print("Lolf")
'''

# x = int(input("Enter the no of times for meow: "))
# for _ in range(x):
#     print("Meow")


names = ["Nitin", "Anuj","Chico"]
for i in range(len(names)):
    print(i+1,names[i])



companies = {
    "Realme" : "Smartphone",
    "Xiaomi" : "Smartphone",
    "Boat"   :  "Watch"
}

for product in companies:
    print(product, companies[product])

'''   :  is used for dictionary     '''

def main():
    a = int(input("Enter the number question blocks : "))
    rows(a)

def rows(n):
    for i in range(n):
        print("?", end="")

main()

