per1 = input()

per1_age = int(per1.split()[0])
per1_sex = per1.split()[1]

per2 = input()

per2_age = int(per2.split()[0])
per2_sex = per2.split()[1]

if (per1_age >= 19 and per1_sex == 'M') or (per2_age >= 19 and per2_sex == 'M'):
    print('1')
else:
    print('0')