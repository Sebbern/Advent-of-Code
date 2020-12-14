import re

batchlist = open("input.txt", "r").read().split("\n\n")
passports = []
valid = 0
credentials = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
details = re.compile(r'(\w+):')

for i in batchlist:
    passports.append([x for x in i.split()])

for u in passports:
    check = re.findall(details, str(u))
    if all(x in check for x in credentials) == True:
        valid += 1

print(valid)