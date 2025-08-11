try:
    file1=open('sample.txt','r')
    readingfile=file1.read()
    print(readingfile)
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
finally:
    print()