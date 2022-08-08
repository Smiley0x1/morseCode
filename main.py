#This is the main file for the WIP project morseCode
import encode
import decode
def main():
    print("Welcome to Smil3y's Morse encoder/decoder\n")
    whatToDo = int(input("What do you want to do?\n1)Encode\n2)Decode\n"))
    if whatToDo == 1:
        encode.main()
    if whatToDo == 2:
        decode.main()  
main()