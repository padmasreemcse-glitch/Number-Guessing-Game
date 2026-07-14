import random
rno=random.randint(1,100)
count=0
def guess(rno):
    print("Welcome to the number guessing game🎯")
    while True:
        global count
        no=int(input())
        count+=1
        try:
            if no<rno:
                print("⬇️Too low")
                print("❌ Wrong guess. Try again!")
            elif no>rno:
                print("⬆️Too high")
                print("❌ Wrong guess. Try again!")
            elif rno==no:
                print("-------🎉 Congratulations! You found the number-------")
                print("No of trials:",count)
                break
        except:
            print("Please enter a valid integer.")
guess(rno)



