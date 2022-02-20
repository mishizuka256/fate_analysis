from table import convert_table

def enter_birthday(birthyear=1982, birthmonth=12, birthday=24):
    print("Enter your birthyear(1873~2076): ",end="")
    birthyear = int(input())
    print("Enter your birthmonth(1~12): ",end="")
    birthmonth = int(input())
    print("Enter your birthday(1~31): ",end="")
    birthday = int(input())
    print(birthyear,birthmonth,birthday)


    return birthyear, birthmonth, birthday
    

def main():
    print("Welcome to fate analyzer")

    birthyear, birthmonth, birthday = enter_birthday()

    print(convert_table.yearlist(birthyear))


if __name__ == "__main__":
    main()
