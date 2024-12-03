import math
result=0
rlist=[]
llist=[]
score=0
def readdata():
    r = []
    l =[]
    f = open("day1.txt",'r')
    d = []
    for line in f:
        d.append(line.rstrip().split())
    d.pop()
    for  i in d:
        rlist.append(int(i[1]))
        llist.append(int(i[0]))
    global datar
    global datal
    llist.sort() 
    rlist.sort()



def calculate():
    global result
    for i in range(len(rlist)):
         result += math.fabs((rlist[i]-llist[i]))
    print(math.floor(result))


#part2
def similar():
    for i in rlist:
        count = llist.count(i)
        global score
        score += i*count
        count=0
    print(score)







readdata()

calculate()
similar()

