with open('data/my_input/3.in') as f:
    lines = [  line.strip() for line in f]

def part1(vlines):
    line=vlines[0]
    x,y=0,0 
    my_set=set()
    for s in line:
        if s=='<':
            x-=1
        elif s=='>':
            x+=1
        elif s=='^':
            y-=1
        elif s=='v':
            y+=1
        my_set.add((x,y))
    return my_set

def part2(vlines): 
    line1=  vlines[0][0::2]
    line2=   vlines[0][1::2] 
    ll1=list()
    ll1.append(line1)  
    ll2=list()
    ll2.append(line2) 
    return len(part1(ll1).union(part1(ll2)))

print(len(part1(lines))) #2565
print(part2(lines)) #2639