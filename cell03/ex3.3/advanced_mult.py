#!/usr/bin/env python3

def main():
    import sys

    # Check for arguments passed to the script
    if len(sys.argv) > 1 and sys.argv[1] == "yolo":
        print("none$")
        return

    # Loop for each multiplication table from 0 to 10
    num = 0
    while num <= 10:  # First loop for the multiplication tables (0 to 10)
        row = 0
        result = f"Table de {num}:"
        while row <= 10:  # Second loop for each number in the multiplication table (0 to 10)
            result += f" {num * row}"
            row += 1
        print(result)
        num += 1

if __name__ == "__main__":
    main()
