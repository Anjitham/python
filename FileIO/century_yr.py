# write all century years from 1800 t0 2024 to century_years.txt
path="C:\\Users\\User\\Desktop\\Python works\\FileIO\\century_years.txt"

f=open(path,"w")

for year in range(1800,2025):
    if year%100==0:
        f.write(str(year)+"\n")

