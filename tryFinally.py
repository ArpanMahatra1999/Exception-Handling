try:
    fh = open("testFile.txt","w")
    fh.write("This is test file for exception handling.")
except:
    print("Error")
finally:
    fh.close()