import validators

email = input("What's your email adress? ")
validate_email = validators.email(email)
if validate_email:
    print("Valid")
else:
    print("Invalid")
