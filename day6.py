import re
with open('data/my_input/6.in') as f:
    lines = [  line.strip() for line in f]

def part1(vlines):
#turn off 199,133 through 461,193 
#toggle 537,781 through 687,941
#turn on 226,196 through 599,390
    d=dict()
    num=lambda s : re.findall('\d+',s)
    for line in vlines:
        numbers=num(line) 
        off,on,toggle=False,False,False
        if 'off' in line:
            off=True
        elif 'toggle' in line:
            toggle =True
        elif 'on' in line:
            on=True
        for i in range(int(numbers[0]),int(numbers[2])+1):
            for j in range(int(numbers[1]),int(numbers[3])+1):
                if off:
                    d[(i,j)]=0
                elif on :
                    d[(i,j)]=1
                elif toggle:
                    if (i,j) in d and d[(i,j)]==1:
                        d[(i,j)]=0
                    elif (i,j) in d and d[(i,j)]==0:
                        d[(i,j)]=1
                    elif (i,j) not in d:
                        d[(i,j)]=1 
    return sum([v for k,v in d.items()])

def part2(vlines):
    d=dict()
    num=lambda s : re.findall('\d+',s)
    for line in vlines:
        numbers=num(line) 
        off,on,toggle=False,False,False
        if 'off' in line:
            off=True
        elif 'toggle' in line:
            toggle =True
        elif 'on' in line:
            on=True
        for i in range(int(numbers[0]),int(numbers[2])+1):
            for j in range(int(numbers[1]),int(numbers[3])+1):
                if (i,j) not in d:
                    d[(i,j)]=0

                if off and d[(i,j)]!=0:
                    d[(i,j)]-=1
                elif on :
                    d[(i,j)]+=1
                elif toggle:
                    d[(i,j)]+=2 
    return sum([v for k,v in d.items()])

print(part1(lines)) #400410
print(part2(lines)) #15343601