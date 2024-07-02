import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    youtube_short = "https://youtu.be/"
    match = re.search(r"^(<iframe){1}.+?(src=\"https?://){1}(www\.)?(youtube\.com/embed/)+?([\w]+)(\"){1}.+$",s)

    if match:
        return youtube_short + match.group(5)
    else:
        return "None"

if __name__ == "__main__":
    main()