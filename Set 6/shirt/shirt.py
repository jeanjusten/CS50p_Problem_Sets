from PIL import Image, ImageOps
import sys
import os

valid_formats = [".jpg",".jpeg",".png"]

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    first_arg = sys.argv[1].lower()
    f_arg = os.path.splitext(first_arg)
    second_arg = sys.argv[2].lower()
    s_arg = os.path.splitext(second_arg)

    if f_arg[1] in valid_formats and s_arg[1] in valid_formats:
        if f_arg[1] == s_arg[1]:
            try:
                photo = Image.open(sys.argv[1])
                shirt = Image.open("shirt.png")
                shirt_size = shirt.size

                resized_photo = ImageOps.fit(photo, shirt_size) # readjusting the uploaded photo size to match the png shirt image size
                resized_photo.paste(shirt, shirt) # pasting the png shirt image into the uploaded original image
                resized_photo.save(sys.argv[2])

            except FileNotFoundError:
                sys.exit("Input does not exist")
        else:
            sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid output")