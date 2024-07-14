# 1. A program to convert the first character uppercase in a sentence and if apart from the first character if any other character is in Uppercase then convert it into Lowercase.


text="hi all HoW aRe yOU doinG"
out=text[0].upper()+text[1::].lower()
print(out)
