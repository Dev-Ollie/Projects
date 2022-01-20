import random
import time

#Defining variables needed
x = True
chose_key = False
option_options = ["e", "d"]
y_or_n = ['yes', 'no', 'Yes', 'No', 'YES', 'NO']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
wait_time = 1
invalid_option = "\nERROR! INVALID OPTION ENTERED\n"
encryption = []
decryption = []

while x == True: #Creates a loop that will repeat the process 
    entered_key = False
    chose_key = False
    x = False
    print("Welcome to the Caesar Cipher in Python, this program will encrypt and decrypt any messages!\n")#Into message
    time.sleep(wait_time)
    option = str(input("Please enter either of the following; \n\n'e' to encrypt a message or \n'd' to decrypt a mesasge.\n\nEnter your choice: "))#Enter chosen method
    if option in option_options:
        if option == 'e':
            plaintext = str(input("\nPlease enter a message to encrypt: "))#Enter the message to encrypt
            while chose_key == False:
                choose_key = str(input("\nWould you like to use a randomly generated caesar shift key?\n\n'yes' for YES\n'no' for NO\n\nPlease enter your option: "))#Decide if they want to use a randomly generated key
                if choose_key in y_or_n:
                    chose_key = True
                    if choose_key in ["NO", "no", "No"]:
                        while entered_key == False: #Repeats until they enter a valid int
                            entered_key = True
                            encrypt_key = int(input("\nPlease enter a caesar shift key between 1 and 26: "))#If they chose to enter a key, they can do so
                            if encrypt_key >= 1 and encrypt_key <= 26: #Checks what they entered is in the range
                                time.sleep(wait_time)
                            else:
                                print("\nPlease enter a valid caesar shift key between 1 and 26 as an INT.")#Error message if they enter an incorrect value
                                time.sleep(wait_time)
                                entered_key = False
                    else:
                        encrypt_key = random.randint(1, 27) #Generates a number between 1 and 25
                        time.sleep(wait_time)
                else:
                    print(invalid_option)
                    time.sleep(wait_time)
                    chose_key = False

                for i in plaintext: #Loops through the plaintext
                    if i in uppercase:
                        index = uppercase.index(i)
                        crypting = (index + encrypt_key) % 26
                        encryption.append(uppercase[crypting]) #Shifts the uppercase letters adding them to the output
                    elif i in lowercase:
                        index = lowercase.index(i)
                        crypting = (index + encrypt_key) % 26
                        encryption.append(lowercase[crypting]) #Shifts the lowercase letter adding them to the output
                    elif i.isspace():
                        encryption.append(" ") # Adds spaces to the output
                output = ''.join(str(e) for e in encryption)
                print("\nSHIFT KEY:", encrypt_key, "\nPLAINTEXT:", plaintext, "\nCIPHER MESSAGE:", output, "\n") #Returns the encrypted messge with plaintext and the key
                x = True

        elif option == 'd':
            plaintext = str(input("\nPlease enter a message to decrypt: ")) #Enter a message to decrypt
            while chose_key == False:
                choose_key = str(input("\nWould you like to use brute force to decrypt?\n\n'yes' for YES\n'no' for NO\n\nPlease enter your option: ")) #Choose if they want to use brute force
                if choose_key in y_or_n:
                    chose_key = True
                    if choose_key in ["NO", "no", "No"]: #Checks if they entered no
                        entered_key = False
                        while entered_key == False:
                            entered_key = True
                            encrypt_key = int(input("\nPlease a caesar shift key between 1 and 26, if you know what it is: ")) #Enter a key in the range
                            if encrypt_key >= 1 and encrypt_key <= 26:
                                time.sleep(wait_time)
                            else:
                                print("\nPlease enter a valid caesar shift key between 1 and 26 as an INT.") #Return error message
                                time.sleep(wait_time)
                                entered_key = False
                                
                else:
                    print(invalid_option)
                    time.sleep(wait_time)
                    chose_key = False

                #Decrypt using the entered key
                if entered_key == True:
                    for i in plaintext:
                        if i in uppercase:
                            index = uppercase.index(i)
                            decrypting = (index - encrypt_key) % 26
                            decryption.append(uppercase[decrypting])
                        elif i in lowercase:
                            index = lowercase.index(i)
                            decrypting = (index - encrypt_key) % 26
                            decryption.append(lowercase[decrypting])
                        elif i.isspace():
                            decryption.append(" ")
                #Decrypt using brute force (trying all combos)
                elif entered_key == False:
                    for n in range(1, 27): #Trying all shift keys 1-26
                        for i in plaintext:
                            if i in uppercase:
                                index = uppercase.index(i) #Finds the index off the encrpyted letter
                                decrypting = (index - n) % 26 #Calculates the actual letter
                                decryption.append(uppercase[decrypting]) #Adds this to the result
                            elif i in lowercase:
                                index = lowercase.index(i)
                                decrypting = (index - n) % 26
                                decryption.append(lowercase[decrypting])
                            elif i.isspace():
                                decryption.append(" ")
                        output = ''.join(str(e) for e in decryption)
                        print("Caesar key:", n, " | Ciphered Message:", output) #Print all the attempted shift keys and the result, the user can determin what the key was
                        decryption = []
                if option == 'e':
                    output = ''.join(str(e) for e in decryption)
                    print("\nPlainText:", plaintext, "\nCiphered Message:", output) # Returns the output from the earlier encrypt method
                print("\n")
                x = True #Repeats the process, re-enables the first loop
                
                
    else:
        print(invalid_option) #Returns error
        time.sleep(wait_time)
        x = True #Response validation, repeats the program until they enter a valid option
