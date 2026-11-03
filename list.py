import os
import time
# wait for another update 

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

myway = ["apple 111", "banana 222", "cherry 333", "date 444", "elderberry 555"]
ready = []

while True:
    ask = int(input("\nenter 1 to add an item \nenter 2 to display your items \nenter 3 to exit: "))
    
    if ask == 1:
        user = input("\nEnter the code of the item here: ")
        for item in myway:
            if user in item:
                ready.append(item)
                break
                
    elif ask == 2:
        clean()
        print("\nYour items are... \n")
        time.sleep(2)
        for item in ready:
            print(item)
            
    elif ask == 3:
        clean()
        print("Exiting the program.")
        time.sleep(2)
        break  