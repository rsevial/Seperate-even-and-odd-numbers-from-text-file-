# Programmed by: Rebekah Joy E. Sevial
# Problem 1 of Assignment 3
# Seperate even and odd numbers from text file

# Define seperated numbers
def seperated_number():
# Open text file
    with open("numbers.txt") as file_numbers:
        # For loop to read each line of the text file
        for line in file_numbers:
            # If statement for converting string into a integer
            if line.strip:
                input_numbers = int(line)
    # If-else statement that determines if the number in the text file is even or odd number
                # If the number is even
                    # Create new text file for even numbers as even.txt      
                # Else
                # Create new text file for odd numbers as odd.txt
# Process that will end the program
