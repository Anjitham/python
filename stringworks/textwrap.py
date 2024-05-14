import textwrap

text = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
wrapped_text = textwrap.wrap(text,width=4)

for line in wrapped_text:
    print(line)