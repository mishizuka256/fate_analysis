from table import convert_table

def main():
    print("Welcome to fate analyzer")
    debug = True
    birthyear,birthmonth,birthday = 0,0,0
    if debug == True:
        birthyear = 1982
        birthmonth = 12
        birthday = 24
    else:
        birthyear = int(input())
        print("birthyear(1873~2076): ",end="")
        birthmonth = int(input())
        print("birthmonth(1~12): ",end="")
        birthday = int(input())
        print("birthday(1~31): ",end="")
    print(birthyear,birthmonth,birthday)

    print(convert_table.yearlist(birthyear))



if __name__ == "__main__":
    main()
