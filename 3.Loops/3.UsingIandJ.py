'''Using i and j in the for loop  '''
def main():
    a = int(input("Enter the size of block : "))
    gameBlock(a)


def gameBlock(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()


main()