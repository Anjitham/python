# non century years

start_year=int(input("Enter an year:"))
curent_year=2023

for year in range(start_year,curent_year,1):
    if ( year%100!=0):
        print(year)


