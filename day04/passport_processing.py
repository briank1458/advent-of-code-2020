f = open('input.txt', 'r')
input = f.read()
input = input.split('\n\n') # Remove empty lines

# Remove line continues, clean data
def passport_processing():
    input_clean = []
    for i in input:
        j = i.replace('\n', ' ')
        for item in j:
            k = j.split(' ')
        input_clean.append(k)

    valid_count = 0
    for item in input_clean:
        if len(item) == 8:
            valid_count += 1
        elif len(item) == 7 and not any('cid' in i for i in item):
            valid_count += 1
        else:
            pass

    print(valid_count)

# Second problem
def passport_processing2():
    input_clean = []
    for i in input:
        j = i.replace('\n', ' ')
        for item in j:
            k = j.split(' ')
        input_clean.append(k)

    valid_count = 0
    for item in input_clean:
        if len(item) == 8:
            for i in item:
                if 'byr' in i:
                    if int(i[4:])>=1920 and int(i[4:])<=2002:
                        pass
                    else:
                        continue
                elif 'iyr' in i:
                    if int(i[4:])>=2010 and int(i[4:])<=2020:
                        pass
                    else:
                        continue
                elif 'eyr' in i:
                    if int(i[4:])>=2020 and int(i[4:])<=2030:
                        pass
                    else:
                        continue
                elif 'hgt' in i:
                    if i[-2:] == 'cm':
                        if int(i[4:-2])>=150 and int(i[4:-2])<=193:
                            pass
                        else:
                            continue
                    elif i[-2:] == 'in':
                        if int(i[4:-2])>=59 and int(i[4:-2])<=76:
                            pass
                        else:
                            continue
                elif 'hcl' in i:
                    if not any(value in ['0','1','2','3','4','5','6','7','8','9'] for value in i) or not any(value in ['a','b','c','d','e','f'] for value in i):
                        continue
                    else:
                        pass
                elif 'ecl' in i:
                    for color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        if color in i:
                            pass
                        else:
                            continue
                elif 'pid' in i:
                    if len(i) == 13:
                        pass
                    else:
                        continue
                    valid_count += 1
        elif len(item) == 7 and not any('cid' in i for i in item):
            for i in item:
                if 'byr' in i:
                    if int(i[4:])>=1920 and int(i[4:])<=2002:
                        pass
                    else:
                        continue
                elif 'iyr' in i:
                    if int(i[4:])>=2010 and int(i[4:])<=2020:
                        pass
                    else:
                        continue
                elif 'eyr' in i:
                    if int(i[4:])>=2020 and int(i[4:])<=2030:
                        pass
                    else:
                        continue
                elif 'hgt' in i:
                    if i[-2:] == 'cm':
                        if int(i[4:-2])>=150 and int(i[4:-2])<=193:
                            pass
                        else:
                            continue
                    elif i[-2:] == 'in':
                        if int(i[4:-2])>=59 and int(i[4:-2])<=76:
                            pass
                        else:
                            continue
                elif 'hcl' in i:
                    if not any(value in ['0','1','2','3','4','5','6','7','8','9'] for value in i) and not any(value in ['a','b','c','d','e','f'] for value in i):
                        pass
                    else:
                        continue
                elif 'ecl' in i:
                    for color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        if color in i:
                            continue
                        else:
                            pass
                elif 'pid' in i:
                    if len(i) == 13:
                        pass
                    else:
                        continue
                    valid_count += 1
        else:
            pass

    print(valid_count)

passport_processing2()
# 190, too high
# 181, too high
# 157, too high
# 125, nope