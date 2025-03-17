# file_path = 'example.txt'

# try:
#     file = open(file_path, 'r')
#     # Perform operations on the file
# finally:
#     file.close()
# # Reading from a file using read() method
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)


# # Moving the file cursor using seek()
# with open('example.txt', 'r') as file:
#     file.seek(10)  # Move to the 10th byte
#     content = file.read()

#     # Truncating a file
# with open('example.txt', 'a') as file:
#     file.truncate(20)  # Limit the file size to 20 bytes


sent_message = "Hey there! This is a secret message."

with open('sent_message.txt', 'w') as file:
    file.write(sent_message)

with open('sent_message.txt', 'r+') as file:
    original_message = file.read()

    file.seek(0)

    unsent_message = "This message has been unsent."

    file.truncate(len(unsent_message))

    file.write(unsent_message)

print("Original Message:", original_message)
print("Unsent Message:", unsent_message)
