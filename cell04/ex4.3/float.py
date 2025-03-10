#!/usr/bin/env python3

def main():
    num = input("Give me a number: ")
    
    # เช็คว่าเป็นจำนวนทศนิยมหรือไม่
    if '.' in num:
        print("This number is a decimal.")
    else:
        print("This number is an integer.")

if __name__ == "__main__":
    main()
