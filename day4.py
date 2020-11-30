
import hashlib 

with open('data/my_input/4.in') as f:
    lines = [  line.strip() for line in f]

 

def part1(vlines,string_to_match):
    i=0
    stop=0
    while stop==0:
        i+=1
        s=vlines[0]+str(i)
        if hashlib.md5(s.encode('utf-8')).hexdigest().startswith(string_to_match) : 
            stop=1
    return  i

print(part1(lines,'00000')) #117946
print(part1(lines,'000000')) #3938038