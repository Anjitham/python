# leap years from 1500-2024
start_year=2000
current_year=2023

for year in range(start_year,current_year,1):
    if ( year%100==0 and year%400==0 or year%100!=0 and year%4==0):
        print(year)
    

