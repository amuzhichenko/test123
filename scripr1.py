# a = "Minsk"
# b = "Gomel"

# print(a)
# print(b)

# print(a + " " + b)

# for x in range (100):
#     print(x)
#---------------------------------------------------

# country = ['belarus', 'cuba', 'lesson3']
# for x in country:
#     print(x.upper())



# a = "lesson"
# if a == "lesson":
#     print("yes")
# else:
#     print("no")

#-----------------------------------------------------
# word='laptop'

# new_word=word.replace('l','k')
# print(new_word)

#-----------------functions----------------------------------------

# def name():
#     print("sasha")
#     print("max")

# def summa(x,y):
#     print(x+y)

# name()
# summa(11,44)




#-------------------------Random paswword ---with random library------------------------------------------

# import random

# password = "abcdABCD1234!@#$"
# lenght_password = int(input("Enter the lenght pf password: "))

# a = "".join(random.sample(password,lenght_password))

# print (f'your password is {a}')



#--------------sort -----------------------------------------

# unsort_list = [2,5,3,8,5,22,4,787]
# unsort_list.sort()

# print("NOW IT IS SORTED:", unsort_list)


#-----------------------print numbers less than 8-------------------
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b=[]
# for i in a :
#     if i < 8 :
#         b.append(i)
# print(b)

#--------------------сумма цифр  числа введенного с клавиатуры-------------------------------------

# your_num = input("Enter your number: ")

# sum = 0
# for i in your_num:
#     sum = sum + int(i)

# print(sum)


#----------------------------отправлять письма по адресам из эксель таблицы-------------

# import pandas as pd 
# import smtplib

# SenderAddress = "muzhichenkoalex@gmail.com"
# password = "ehlqvkpniyggtqju"


# e = pd.read_excel("emails.xlsx")
# emails = e['Emails'].values

# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()
# server.login(SenderAddress,password)


# msg = "Alert of script, server is down"
# subject = "ALARM!!!"

# body = "Subject:{}\n\n{}".format(subject,msg)

# for email in emails:
#     server.sendmail(SenderAddress, email, body)

# server.quit()


#--------------Encrypt file---------------------------------------


# from cryptography.fernet import Fernet

# # key generation
# key = Fernet.generate_key()

# # string the key in a file
# with open('filekey.key', 'wb') as filekey:
#   filekey.write(key)

# # opening the key
# with open('filekey.key', 'rb') as filekey:
# 	key = filekey.read()

# # using the generated key
# fernet = Fernet(key)

# # opening the original file to encrypt
# with open('test1.txt', 'rb') as file:
# 	original = file.read()
	
# # encrypting the file
# encrypted = fernet.encrypt(original)

# # opening the file in write mode and 
# # writing the encrypted data
# with open('test1.txt', 'wb') as encrypted_file:
# 	encrypted_file.write(encrypted)

