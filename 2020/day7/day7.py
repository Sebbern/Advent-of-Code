import re

rulelist = open("input.txt", "r").read().strip().split("\n")

rules = {}
shinybag = 0

bagkey = re.compile(r"(\w+\s\w+) bags contain")
bagvalue = re.compile(r"(\d+\s\w+\s\w+) bag|bags$")

for i in rulelist:
    findkeys = re.findall(bagkey, str(i))
    findvalues = re.findall(bagvalue, str(i))
    rules[str(findkeys)] = findvalues

for u in rules:
    for y in rules[u]:
        strippedy = re.sub(r"\d+\s", "", y)
        strippedy = "[\'"+strippedy+"\']"

        for t in rules[strippedy]:
            rules[u].append(t)
    #print(u, rules[u])

    if "shiny gold" in str(rules[u]):
        shinybag += 1

print(shinybag) # This takes ~ 5 minutes to run lmao