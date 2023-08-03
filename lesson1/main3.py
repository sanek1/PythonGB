

year  = 1900

if(year %4 ==0 and year % 100 != 0) or year == 0 :
    result = "Yes"
else:
    result = "No"

print(result)