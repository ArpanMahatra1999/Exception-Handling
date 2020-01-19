try:
    with open("file.log") as file:
        read_data = file.read()
except:
    print("No file.log")