# TDP015 Inlämningsuppgift 4

# Författaren Lewis Carroll, mest känd för hans bock Alice i
# Underlandet, var även en begåvad matematiker. Han utvecklade
# bl.a. en algoritm som beräknar ett datums veckodag:
#
# http://www.cs.usyd.edu.au/~kev/pp/TUTORIALS/1b/carroll.html
#
# Er uppgift är att implementera denna algoritm i Python. Resultatet
# ska vara en funktion day_of_the_week(y, m, d) som tar ett årtal y
# (t.ex. 2016), en månad m (t.ex. 4 för april) och en dag d i denna
# månad och returnerar rätt element från följande lista:

DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

# Ni får inte använda några moduler, endast basfunktioner. (Carroll's
# beskrivning skiljer mellan old style och new style datum. Ni behöver
# bara hantera new style datum.)

def century(current):
    current = current % 4
    current = 3 - current
    current = 2 * current
    return current

def year(current):
    dozens = current // 12
    overplus = current % 12
    fours = overplus // 4
    return dozens + overplus + fours

def month(current):
    #The riddle states:
    #The month numbers are related to the number of days in the previous month.
    #If we calculate all months, we get:
    ##January: 0
    ##February: 31
    ##March: 59
    ##April: 90
    ##May: 120
    ##June: 151
    ##July: 181
    ##August: 212
    ##September: 243
    ##October: 273
    ##November: 304
    ##December: 334
    #By then casting out the 7s (mod 7) we get the correct list
    ##January: 0
    ##February: 3
    ##March: 3
    ##April: 6
    ##May: 1
    ##June: 4
    ##July: 6
    ##August: 2
    ##September: 5
    ##October: 0
    ##November: 3
    ##December: 5
    #Why do we cast out the 7s? Because Lewis himself said so in the beginning of the algorithm:
    ##When an item or total exceeds 7, divide by 7, and keep the remainder only.

    #If the next class who has this class,
    #don't understand the "month-item" I would just refer to the second parahraph in the algorithm,
    #people forget that the paragraph applies to everything in the algorithm, even the months.

    #Or did I just get lucky and found a loophole?

    items = {"January":0,
             "February":3,
             "March": 3,
             "April": 6,
             "May": 1,
             "June": 4,
             "July": 6,
             "August": 2,
             "September": 5,
             "October": 0,
             "November": 3,
             "December": 5}
    if current == 1:
        current = items["January"]
    elif current == 2:
        current = items["February"]
    elif current == 3:
        current = items["March"]
    elif current == 4:
        current = items["April"]
    elif current == 5:
        current = items["May"]
    elif current == 6:
        current = items["June"]
    elif current == 7:
        current = items["July"]
    elif current == 8:
        current = items["August"]
    elif current == 9:
        current = items["September"]
    elif current == 10:
        current = items["October"]
    elif current == 11:
        current = items["November"]
    elif current == 12:
        current = items["December"]
    return current

def day(year, month, day):
    if month == 1 or month == 2:
        #typical leap year calc
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            #if the total becomes 0, add 7 to day
            if (day - 1) == 0:
                day = day + 7
            #remove 1 from day as it says in the riddle
            day = day - 1
    return day

def divide_by_seven(current, total):
    total = total + current
    if total > 7:
        total = total % 7
    return total


def day_of_week(y, m, d):
    #init vars
    current, total = 0, 0

    #strip the needed digits from the year
    century_begin = str(y)[:2]
    century_begin = int(century_begin)
    year_last_digits = y % 100

    #calc century
    current = century(century_begin)
    total = divide_by_seven(current, total)

    #calc year
    current = year(year_last_digits)
    total = divide_by_seven(current, total)

    #calc month
    current = month(m)
    total = divide_by_seven(current, total)
    
    #calc day
    current = day(y, m, d)
    total = divide_by_seven(current, total)

    #return weekday
    return DAYS[total]


print("1783-09-18: " + day_of_week(1783, 9, 18))
print("2017-05-07: " + day_of_week(2017, 5, 7))
print("2017-12-01: " + day_of_week(2017, 12, 1))
print("2017-12-31: " + day_of_week(2017, 12, 31))
print("LEAP 2016-02-29: " + day_of_week(2016, 2, 29))
print("LEAP 2020-02-29: " + day_of_week(2020, 2, 29))
print("LEAP 2032-02-29: " + day_of_week(2032, 2, 29))

# Ledning
#
# Carrolls egen beskrivning av algoritmen är formulerad som en gåta.
#
# Den del som kanske är svårast att förstå är "The Month-item":
#
# 'If it begins or ends with a vowel, subtract the number, denoting
# its place in the year, from 10. This, plus its number of days, gives
# the item for the following month. The item for January is "0"; for
# February or March, "3"; for December, "12".'
#
# Detta betyder alltså att talen för januari (0), februari (3), mars
# (3) och december (12) är direkt givna; och att talen för en månad
# vars namn (på engelska) inte börjar eller slutar med en vokal kan
# räknas ut från föregående månads "Month-item" genom att man plussar
# på antalet dagar som denna föregående månad har.
#
# Det som kanske är minst tydligt är hur talen för de resterande
# månaderna ska räknas ut, dvs. månader vars namn börjar eller slutar
# med en vokal. Men det står egentligen explicit i första meningen:
#
# 'If it begins or ends with a vowel, subtract the number, denoting
# its place in the year, from 10.'
#
# Detta ger alltså t.ex. 6 för april eftersom 10 - 4 = 6.
#
# Med detta så kan ni alltså räkna ut alla "Month-items". Mitt förslag
# är att ni räknar ut dem endast en gång och sedan helt enkelt lagrar
# dem i en lista eller liknande.