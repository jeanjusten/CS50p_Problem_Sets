import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    um_list = re.findall(r"((\s)+|(\b)|(\.)+|(\?)+|(,)+)(um)+((\s)+|(\.)+|(\?)+|(,)+|(\b)+)",s, re.IGNORECASE)
    #um_list = re.findall(r"[^\w]um*[^\w]",s)
    i = int((len(um_list)))
    return i

if __name__ == "__main__":
    main()