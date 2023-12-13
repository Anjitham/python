# print all non century
year=int(input("Enter year:"))
current_year=2023
while(year<=current_year):
    if (year%100!=0):
        print(year)
    year+=1