import re
floorlist = open("input.txt", "r").read()
openparenRegex = re.compile(r'[(]')
closingparenRegex = re.compile(r'[)]')

floor = len(openparenRegex.findall(floorlist)) - len(closingparenRegex.findall(floorlist))
print(floor)