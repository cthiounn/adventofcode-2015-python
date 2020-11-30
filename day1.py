with open('data/my_input/1.in') as f:
    lines = [  line.strip() for line in f]
    line=lines.pop()

def part1(s):
    return s.count('(')-s.count(')')

def part2(line):
    count=0
    index=0
    for s in line :
        if s == '(':
            count+=1
        elif s== ')':
            count-=1
        index+=1
        if count==-1: 
            break
    return index

print(part1(line)) #138
print(part2(line)) #1771