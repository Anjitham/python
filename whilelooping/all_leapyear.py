starting_year=int(input("Enter a starting year:"))
current_year=2023

while(starting_year<=current_year):
    if (starting_year%100==0 and starting_year%400==0 or starting_year%100!=0 and starting_year%4==0):
        print(starting_year)
    starting_year+=1