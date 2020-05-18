# show ticket pricing 
# 0 to 3   -- free 
# 4 to 10  -- 150
# 11 to 60 -- 250 
# above 60 -- 200

age = int(input("please enter your age :- ").strip())

if 0<age<=3:
    print("FREE")
elif 3<age<=10:
    print("Ticket price is 150")
elif 10<age<=60:
    print("Ticket price is 250")
else:
    print("Ticket price is 200")