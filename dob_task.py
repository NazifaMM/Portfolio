# Storing information (Names and birthdates) in a file 

#File path to open dob task 
file_path = r"C:\Users\nazif\Desktop\DOB.txt"

names = []               # name list to store names
birthdates = []          # birthday list to store birthdates

with open(file_path, 'r') as file:        # Opens DOB file 
    for line in file:
        parts = line.split(' ')           # Splits the line 
        name = ' '.join(parts[:-3])       # Join the name parts
        birthdate = ' '.join(parts[-3:])  # Join the birthdate parts
        names.append(name)                # Adds all the names
        birthdates.append(birthdate)      # Adds all the birthdays

        # # # Print Names in one section
        print("Names:")
        for name in names:
            print(name)

        print()   # Gives space 

        # # # Print Birthdates in one sections
        print("Birthdatess:")
        for birthdate in birthdates:
            print(birthdate)


         
    

