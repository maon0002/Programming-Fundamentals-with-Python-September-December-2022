#     3.  Extract File
# Write a program that reads the path to a file and subtracts the file name and its extension.
input_path = input().split("\\")
file_name, file_ext = input_path[-1].split(".")
print(f"File name: {file_name}")
print(f"File extension: {file_ext}")
