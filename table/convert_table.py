def create_list_from_file(file):
    with open(file, "r")as f:
        t_table = f.readlines()
    ret_table = []
    for line in t_table:
        line = line.rstrip("\n")
        ret_table.append(line)
    return ret_table

def yearlist(input_year):
    tenchusatu_table = []
    tenchusatu_table = create_list_from_file("table/tenchusatu_table.csv")
    print(tenchusatu_table)
    
    init_year = 1873 # Gregorian Calendar
    start_tenchusatu_num = 10-1 # 0 origin
    end_year = 2076
    print("init_year:", \
          init_year,tenchusatu_table[start_tenchusatu_num])

    yearlist = []
    tenchusatu_num = start_tenchusatu_num
    for year in list(range(init_year, end_year)):
        print(year, tenchusatu_table[tenchusatu_num])

        if input_year == year:
            print("*" * 10 + " " + str(year) + " " + "*" * 10)
            exit()

        tenchusatu_num += 1
        if tenchusatu_num >= len(tenchusatu_table):
            tenchusatu_num = 0
    # yearlist = [1873,"癸酉"]

