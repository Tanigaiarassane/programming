import time 

file_h = open("timeprint.txt", "a")
file_h.write(time.asctime() + "\n")
file_h.close()


file_r = open("timeprint.txt","r")
print file_r.read()
file_r.close()
