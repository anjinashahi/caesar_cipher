"""
    Name = Anjina Shahi
    Student number =2330781
    This program encrypts and decrypts text using Caesar Cipher.
"""
def welcome():
    """
        Welcomes users to the program
    """
    print("Welcome to Caesar Cipher")
    print("This program encrypts and decrypts text using Caesar Cipher")

def enter_message():#function to take mode and text messag eform the user
    """
    asks user to enter text which he/she wants to encrypt or decrypt.
    """
    mode = input("Do you want to encrypt or decrypt the text? (E/D): ").upper()
    #asks user to if they want to encrypt or decrypt
    message ="" #creating an empty variable
    if mode == "E":
        message = str(input("Enter the text you want to encrypt: ").upper())
        # take the text input to encrypt
    elif mode == "D":
        message = input("Enter the text you want to decrypt: ").upper()
        # take the text input to encrypt
    else:
        print("invalid input")# print invalid if the user enter any value except E/D
        valid_input = enter_message() #loop runs from function enter_message
        mode = valid_input[0]
        message = valid_input[1]
    return(mode, message)#returning the values as tuple

def encrypt(message_container,shift):
    """
       encrypts the text
    """
    result = ""
    for char in message_container:
        char_to_num = ord(char)# converting characters into ascii value
        if char.isalpha(): #
            shifted_num = char_to_num + shift # adding the shift number to ascii value to increase
            if shifted_num>90: # if the shifted number is mnore than 90 then it is decresed by 26
                shifted_num -= 26
            num_to_char = chr(shifted_num)
            #the shifted number to changed into character that is from number to character
        result += num_to_char
    return result

def decrypt(message_container, shift): # a parameter is passed
    """
        decrypts the text
    """
    result = ""
    for char in message_container: # loops runs until
        char_to_num = ord(char)# converting characters into ascii value
        if char.isalpha():
            shifted_num = char_to_num - shift
            # sudtracting the shift number from ascii value to increase
            if shifted_num < 65: #if the shifted number is less than 65 then it is decresed by 26
                shifted_num += 26
            num_to_char = chr(shifted_num)
            #the shifted number to changed into character that is from number to character
        result += num_to_char
    return result

def main():
    """
    all the functions are called here
    """
    welcome()#welcome function is called
    message = enter_message()#("D", "asdfsdfasdf")
    shift = int(input("Enter how many numbers you want to shift: ")) % 26
     #take shift input from the user
    res = ""
    if message[0] == "E":
        res = encrypt(message[1], shift) #takes text from message as its index is 1
    else:
        res = decrypt(message[1], shift)
    print(res)
    again = input("Do you want encrypt or decrypt again(Y/N): ").upper()
    #asks users if they want to run this program again
    if again == "Y":
        main()# main will be called again
    else:
        print("Thank you for using this program.")#program will end here.
main()# calling main
