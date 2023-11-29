num = 2
latest_num = 0
total = 0

while num < 4000000:
    temp = num
    total+= num
    num = num*4 + latest_num
    latest_num = temp

print(total)