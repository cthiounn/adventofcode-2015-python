import re

with open('data/my_input/7.in') as f:
    lines = [  line.strip() for line in f]

globdict=dict()

def graphdep(vlines):
    aa = re.compile(r'(.*) (.*) (.*) -> (.*)', re.IGNORECASE)
    aa3 = re.compile(r'(.*) (.*) -> (.*)', re.IGNORECASE)
    aa2 = re.compile(r'(.*) -> (.*)', re.IGNORECASE)
    d=dict()
    for line in vlines: 
        bb=aa.match(line)
        bb2=aa2.match(line)
        bb3=aa3.match(line)
        if bb:
            a,b,c,e=bb.groups()
            d[e]=(a,b,c)
        elif bb3:
            a,b,c=bb3.groups()
            d[c]=(a,b)
        elif bb2:
            a,b=bb2.groups()
            d[b]=(0,0,0,a)
            if a.isnumeric(): globdict[b]=int(a)
    return d

def calculate(a,dd): 
    if a in globdict: return globdict[a]
    if a in dd:
        tt=dd[a]
    else:
        return a
    if len(tt)==4:
        if tt[3].isnumeric(): t2=int(tt[3])
        else: t2=calculate(tt[3],dd)
        globdict[a]=t2
        return t2
    elif len(tt)==2:
        if tt[1].isnumeric(): t2=int(tt[1])
        else:  t2=~calculate(tt[1],dd)
        globdict[a]=t2
        return t2
    elif len(tt)==3:
        if tt[0].isnumeric(): t1=int(tt[0])
        else: t1=calculate(tt[0],dd)
        if tt[2].isnumeric():  t2=int(tt[2])
        else:  t2=calculate(tt[2],dd)
        op=tt[1]
        if 'AND'==op: res=t1&t2
        elif 'RSHIFT'==op: res=t1>>t2
        elif 'LSHIFT'==op: res=t1<<t2         
        elif 'OR'==op: res=t1|t2
        globdict[a]=res
        return res
    return int(tt)

def part1and2(vlines):
    dd=graphdep(vlines)
    part1result= calculate('a',dd)
    print("part1",part1result)

    globdict.clear()
    dd2=graphdep(vlines)
    globdict['b']=part1result
    
    print("part2",calculate('a',dd2))

part1and2(lines)
