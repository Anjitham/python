# write all years from 1800 to 2025

path="C:\\Users\\User\\Desktop\\Python works\\FileIO\\years.txt"

f=open(path,"w")

for year in range(1800,2025):
    f.write(str(year)+"\n")