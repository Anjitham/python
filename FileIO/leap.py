# read all years from years.txt and find leapsyears and write to leapyears.txt
r_path="C:\\Users\\User\\Desktop\\Py-Dj\\Python works\\FileIO\\years.txt"
fr=open(r_path,"r")
w_path="C:\\Users\\User\\Desktop\\Py-Dj\\Python works\\FileIO\\leap_yr.txt"
fw=open(w_path,"w")

for line in fr:
    yr=int(line.rstrip("\n"))
    if yr%100==0 and yr%400==0 or yr%100!=0 and yr%4==0:
        fw.write(str(yr)+"\n")