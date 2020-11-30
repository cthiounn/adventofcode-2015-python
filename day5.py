import re 
from collections import Counter

with open('data/my_input/5.in') as f:
    lines = [  line.strip() for line in f]

def hasdouble(line):
    double_letter = re.compile(r'.*(.)\1.*', re.IGNORECASE)
    match= double_letter.match(line)
    if match:
        return True
    return False

def containthreevow(line):
    c=[ v for (k,v) in  Counter(line).items()  if k in 'aeiou']
    if sum(c) >=3:
        return True 
    return False

def notcontain(line):
    if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line :
        return False
    return True

def isnice(line):
    nice=0
    if hasdouble(line) and containthreevow(line) and notcontain(line):
        nice=1
    return nice 
def part1(vlines):
    return sum(map(isnice,vlines))

def match_req_part_2(line):
    double_letter_with_something = re.compile(r'.*(.).\1.*', re.IGNORECASE)
    match= double_letter_with_something.match(line)
    double_letter_with_something = re.compile(r'.*(..).*\1.*', re.IGNORECASE)
    match2= double_letter_with_something.match(line)
    if match and match2:
        return 1
    return 0

def part2(vlines):
    return sum(map(match_req_part_2,vlines))

print(part1(lines)) # 238
print(part2(lines)) # 69