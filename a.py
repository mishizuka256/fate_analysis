init_month = 2
month = init_month
turned = False
for i in list(range(1873,2076)):
    for _ in range(1, 13):
        print(str(i)+","+str(month))
        month += 1
        if month > 12:
            month = 1
            turned = True
        elif month == init_month:
            turned = False
            continue
        else:
            pass



