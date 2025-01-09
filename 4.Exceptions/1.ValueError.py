'''   Try , Except and Value Error  '''

# try: 
#     x = int(input("Enter the value of x ? "))
#     print(f"Entered no  is {x}")
# except ValueError:
#     print("It is not a integer.")    


try: 
    x = int(input("Enter the value of x ? "))
    
except ValueError:
    print("It is not a integer.")    

else:
    print(f"Entered no  is {x}")