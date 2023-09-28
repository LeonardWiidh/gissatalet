import os 
os.system('cls')

#if är villkor. tänk på if såhär: om (det här händer) gör (såhär)

lives = 7
import random
run_game = True
secret_number = random.randint(1, 100)

#print("secret number", secret_number)

print("ayy gissa nummret")
while True:
    try:
        number = int(input("enter number 0 < x < 101: "))
    except:
        print("nah uh")
    if number > secret_number:
        print("AYYY sänk farten")
        lives -= 1
        print("lives left " , lives)
    if number < secret_number:
        print("nah för lågt")
        lives -= 1
        print("lives left " , lives)
    if number == secret_number:
        print('''
        ================
        abow du har rätt
        ================
        ''')
        svar1 = input("Börja om? Y/N ")
        if svar1 == "N":
            break
        if svar1 == "Y":
            lives = 7
            secret_number = random.randint(1,100)
        else:
            print("VA????")
            break
    if lives == 0:
        print('''
             =========== 
              Game Over
             ===========
              ''')
        svar = input("Börja om? Y/N ")
        if svar == "N":
            break
        if svar == "Y":
            lives = 7
            secret_number = random.randint(1,100)
        else:
            print("VA????")
            break