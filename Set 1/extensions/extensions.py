# Prompts the user for the name of a file
userInput = input("File name: ").lower().strip()

# Outputs the file’s media type if the file’s name ends
if userInput.endswith(".gif"):
    print("image/gif")

elif userInput.endswith(".jpeg") | userInput.endswith(".jpg"):
    print("image/jpeg")

elif userInput.endswith(".png"):
    print("image/png")

elif userInput.endswith(".pdf"):
    print("application/pdf")

elif userInput.endswith(".txt"):
    print("text/plain")

elif userInput.endswith(".zip"):
    print("application/zip")

# If media type is different from the above
else:
    print("application/octet-stream")
