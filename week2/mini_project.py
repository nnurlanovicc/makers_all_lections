# import random


# nums=[1,2,3,4,5,6,7,8,9,10]
# comp = random.choice(nums)
# name = input('enter your name: ')
# print(f'Hello {name},do you wont to play?')

# while True:
#     wish = input('(yes or no): ')
#     if wish == 'yes':
#         print('u have to guess the number!')
#         while True:
#             num = int(input('enter the number from 1 to 10: ')) 
#             trying = 0
#             if num != comp:
#                 print('try again!')
#                 trying += 1
#             elif num == comp:
#                 print(f'you win!!! my number was {comp}!you guessed it on  {trying} try')
#                 continue
#     elif wish != 'no' and 'yes':
#        print('write only yes or no')
#     elif wish == 'no':
#         print('ok,bey bey!')
#         break

  

# import random

# nums=[1,2,3,4,5,6,7,8,9,10]
# comp = random.choice(nums)
# name = input('enter your name: ')
# print(f'Hello {name},do you wont to play?')

# while True:
#     wish = input('(yes or no): ')
#     if wish == 'yes':
#         print('u have to guess the number!')
#         num = int(input('enter the number from 1 to 10: '))
#         trying = 0
#         while num != comp:
#                 print('try again!')
#                 num = int(input('enter the number from 1 to 10: ')) 
#                 trying += 1
#         print(f'you win!!! my number was {comp}!you guessed it on  {trying} try')
          
                

#     elif wish != 'no' and 'yes':
#        print('write only yes or no')
#     elif wish == 'no':
#         print('ok,bey bey!')
#         break











    




# num = range(1,10)
# print(num)
# ran_num = num
#   inp4 = input('again?: ')












# if inp3 != comp:
        #     inp4  = input('do you wanna play again?  (yes or no)')
        #     if inp4 == 'yes':

# from random import randint
# name = input("Write you name:")
# wish = "Do you want to play?:\n Write: 'yes' or 'no'"

# while True:
#     trying = 0
#     rand = randint(1,10)
#     print(wish)
#     choice = input(":")
#     if choice == 'yes':
#         print("I mad a number, and you need to find my number,\n so choose ONE number from 1 to 10:\n  ")
#         se = int(input("Enter the num:"))
#         trying += 1

#         while se != rand:
#             se = int(input("Enter the num:"))
#             trying += 1

        
#         print("My number is:", rand)
#         print(f'you guessed it on  {trying} try')

#     elif choice == 'no':
#         print("See you!")
#         break
#     else:
#         print("print only 'yes' or 'no'!!!")




# import random

# def guess_number():
#     name = input("Привет! Как тебя зовут? ")
#     print(f"Привет, {name}!")
    
#     while True:
#         print("Я загадал число от 1 до 100. Попробуй угадать!")
#         secret_number = random.randint(1, 100)
#         attempts = 0
        
#         while True:
#             guess = int(input("Введи свою догадку: "))
#             attempts += 1
            
#             if guess < secret_number:
#                 print("Загаданное число больше.")
#             elif guess > secret_number:
#                 print("Загаданное число меньше.")
#             else:
#                 print(f"Поздравляю, {name}! Ты угадал число {secret_number} за {attempts} попыток.")
#                 break
        
#         play_again = input("Хочешь сыграть еще раз? (да/нет): ")
#         if play_again.lower() == "нет":
#             break
    
#     print("Спасибо за игру! До свидания!")

# guess_number()






