
text_to_write = input("Enter text to write to the file: ")
file = open("output.txt", "w")
file.write(text_to_write + "\n")
file.close()
print("Data successfully written to output.txt.")


text_to_append = input("Enter additional text to append: ")
file = open("output.txt", "a")
file.write(text_to_append + "\n")
file.close()
print("Data successfully appended.")


print("\nFinal content of output.txt:")
file = open("output.txt", "r")
content = file.read()
file.close()
print(content)

