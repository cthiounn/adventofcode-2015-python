with open('data/my_input/2.in') as f:
    lines = [  line.strip() for line in f]


def calculus1(l,w,h):
    return 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l)
 

def calculus(s):
    l =list(map(int,s.split('x')))
     
    return calculus1(*l)
 

def calculus2(l,w,h):
    ll=list()
    ll.extend([l,w,h]) 
    return l*w*h+2*min(l,w,h)+2*sorted(ll)[1]

def calculus22(s):
    l =list(map(int,s.split('x')))
     
    return calculus2(*l)

def part1(vlines):
    return sum(map(calculus,vlines))

def part2(vlines):
    return sum(map(calculus22,vlines))

print(part1(lines)) #1588178
print(part2(lines)) #3783758