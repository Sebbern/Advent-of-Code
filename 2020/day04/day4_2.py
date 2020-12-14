import re

batchlist = open("input.txt", "r").read().split("\n\n")
passports = []
valid = 0
credentials = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
abc = 0

for i in batchlist:
    passports.append([x for x in str(i).split()])

details = re.compile(r'(\w+):')
information = re.compile(r'(\w+):(\S+)')

for u in passports:
    check = re.findall(details, str(u))
    test = 0
    if all(x in check for x in credentials) == True:
        check = re.findall(information, str(u))
        for a, b in check:
            b = re.sub(r"[\',\]]", "", b)
            if a == 'byr':
                if 1920 <= int(b) <= 2002:
                    test += 1
            elif a == 'iyr':
                if 2010 <= int(b) <= 2020:
                    test += 1
            elif a == 'eyr':
                if 2020 <= int(b) <= 2030:
                    test += 1
            elif a == 'hgt':
                if str(b).endswith("cm"):
                    if 150 <= int(b[:-2]) <= 193:
                        test += 1
                if str(b).endswith("in"):
                    if 59 <= int(b[:-2]) <= 76:
                        test += 1
            elif a == 'hcl':
                if bool(re.fullmatch(r'#[0-9a-f]{6}', b)):
                    test += 1
            elif a == 'ecl':
                if b in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    test += 1
            elif a == 'pid':
                if bool(re.fullmatch(r'[0-9]{9}', b)):
                    test += 1

        if test == 7:
            valid += 1
               
print(valid)