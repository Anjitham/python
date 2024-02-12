# find cube
cube=lambda n:n**3
print(cube(3))

# positive/neg
num_chk=lambda n:"positive" if n>0 else "negative" if n<0 else "zero"
print(num_chk(0))

# max of two numbers
max_two=lambda n1,n2:n1 if n1>n2 else n2
print(max_two(4,15))

# odd or even
odd_even_chk=lambda n:"even" if n%2==0 else "odd"
print(odd_even_chk(15))

# sort and print acsndng order of length of string
text="good evening all"
words=text.split(" ")
srt_words=sorted(words,key=lambda w:len(w),reverse=True)
print(srt_words)


# python doesnot support function overloading-->same name for many functions
# * accept many no of parameter,
def product(*args):
    print(args)
# args--->accept as tuple 

#  *-->args-->tuple
#  **-->kwargs-->dictionary