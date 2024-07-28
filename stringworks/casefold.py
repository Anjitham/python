# class "string" methods
company="LUMINAR"
print(company.casefold()) #converts to lower
print(company.lower()) #converts to lower
# casefold advanced than lower
print(company.swapcase()) #convert lower to upper and vice versa

name="anjitha"
print(name.capitalize())# converts to first letter to capital
name2="luminar"
print(name2.upper()) # converts to upper

company="2cars"   
print(company.isalpha()) #to chack entire string has alpabets 

company="25658162487" #to chack entire string has digits
print(company.isdigit())

company="4548hello"
print(company.isalnum()) #check number and alphabets

name2="hoAnjithaho"
print(name2.strip("ho")) #removes ho from both sides

name2="hoAnjithaho"
print(name2.rstrip("ho")) # removes from right

name2="hoAnjithaho"
print(name2.lstrip("ho")) #removes from left

name2="thankgyou"
print(name2.split("g"))


text="abcZd123@"
# ind=0
# s=[int(i) for i in text if i.isdigit()]
for i in text:
    if i.isupper():
        break
print(i)

# sorted() is a function