def read_and_modify_file():
    filename = input("Enter the filename to read: ")

    try:
      
        with open(filename, 'r') as file:
            content = file.read()

       
        modified_content = content.upper()

       
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename.")
    except PermissionError:
        print("Error: Permission denied. Cannot open the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


read_and_modify_file()

