def checkpassword(password):
    upperchars=0
    lowerchars=0
    specialchars=0
    digits=0
    length=0
    length=len(password)

    if (length < 8):
        print("Password must be 8 characters long! \n ")
    else:
        for i in range(0,length):
            if (password[i].isupper()):
                upperchars +=1
            elif (password[i].islower()):
                lowerchars +=1
            elif (password[x].isdigit()):
                digits +=1
            else:
                specialchars +=1

    if (upperchars !=0 , lowerchars !=0 ,digits !=0 ,specialchars !=0):
        if(length >= 10):
            print("Complexity of Entered Password is Strong! ")
        else:
            print("Complexity of Entered Password is Medium")
    else:
        if (upperchars ==0):
            print("Password must contain atleast 1 Uppercase letter \n")
        if (lowerchars ==0):
            print("Password must contain atleast 1 Lowercase letter \n")
        if (specialchars == 0):
            print("Password must contain atleast 1 Special Character \n")
        if (digits ==0):
            print("Password must contain atleast 1 digit")


password = input("Please enter password: ")
checkpassword(password)

# def checkPassword(password):
#     upperChars, lowerChars, specialChars, digits, length = 0, 0, 0, 0, 0
#     length = len(password)
#
#     if (length < 6):
#         print("Password must be at least 6 characters long!\n")
#     else:
#         for i in range(0, length):
#             if (password[i].isupper()):
#                 upperChars += 1
#             elif (password[i].islower()):
#                 lowerChars += 1
#             elif (password[i].isdigit()):
#                 digits += 1
#             else:
#                 specialChars += 1
#
#     if (upperChars != 0 and lowerChars != 0 and digits != 0 and specialChars != 0):
#         if (length >= 10):
#             print("The strength of password is strong.\n")
#         else:
#             print("The strength of password is medium.\n")
#     else:
#         if (upperChars == 0):
#             print("Password must contain at least one uppercase character!\n")
#         if (lowerChars == 0):
#             print("Password must contain at least one lowercase character!\n")
#         if (specialChars == 0):
#             print("Password must contain at least one special character!\n")
#         if (digits == 0):
#             print("Password must contain at least one digit!\n")
#
#
# password = input("Please enter password: ")
# checkPassword(password)