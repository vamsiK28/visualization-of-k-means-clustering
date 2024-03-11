import matplotlib.pyplot as plt

def distanceBTW(c1,c2):
    #print(c1,c2)
    n=((c1[0]-c2[0])**2)+((c1[1]-c2[1])**2)
    n=n**(1/2)
    return n

def whereToGo(c,c1):
    #print(c,c1)
    n=len(c)
    box=[]
    for i in range(n):
        box.append(distanceBTW(c[i],c1))
    mar=min(box)
    #print(box,mar)
    for i in range(n):
        if(mar==box[i]):
            return i
         
def plotCenteroids(o):
    plt.scatter(o[0][1]['x'], o[0][1]['y'], color = "c", marker = "o", s = 30)
    plt.scatter(o[0][0][0] , o[0][0][1], c='c', marker='x', s=100)
    plt.scatter(o[1][1]['x'], o[1][1]['y'], color = "m", marker = "o", s = 30)
    plt.scatter(o[1][0][0] , o[1][0][1], c='m', marker='x', s=100)
    plt.scatter(o[2][1]['x'], o[2][1]['y'], color = "y", marker = "o", s = 30)
    plt.scatter(o[2][0][0] , o[2][0][1], c='y', marker='x', s=100)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show(block=False)
    plt.pause(0.001)
    
    

def divideIntoCenteroids(c,l):
    #print(2)
    k=len(c)
    o=[]
    for i in range(k):
        o.append([c[i],{'x':[],'y':[]}])
    for i in range(len(l[1])):
        m=whereToGo(c,(l[0][i],l[1][i]))
        o[m][1]['x'].append(l[0][i])
        o[m][1]['y'].append(l[1][i])
    return o
 
    
def mean(l):
    n=len(l)
    return sum(l)/n
    
    
def new_centeroids(o):
    cio=[]
    for i in o:
        #print(i)
        cio.append([mean(i[1]['x']),mean(i[1]['y'])])
    #print(cio)
    return cio

def compareEqulas(c1,c2):
    n=len(c1)
    #print(c1,c2)
    for i in range(n):
        if(c1[i][0]!=c2[i][0] or c1[i][1]!=c2[i][1]):
            return False
    return True

def compareClustures(o1,o2):
    n=len(o1)
    for i in range(n):
        x1=o1[i][1]['x']
        y1=o1[i][1]['y']
        x2=o2[i][1]['x']
        y2=o2[i][1]['y']
        xl=len(x1)
        #print(n)
        #print(x1,x2)
        #print(y1,y2)
        if(xl!=len(x2) or len(y1)!=len(y2)):
            #print("chnage in len",len(x1),len(x2),len(y1),len(y2))
            return False
        for i in range(xl):
            if(x1[i]!=x2[i] or y1[i]!=y2[i]):
                #print("not equal:",(x1[i],y1[i]),(x2[i],y2[i]))
                return False
    return True


l=[[6.8,0.8,1.2,2.8,3.8,4.4,4.8,6.8,6.2,7.6,7.8,6.6,8.2,8.4,9.0,9.6],[12.6,9.8,11.6,9.6,9.9,6.5,1.1,19.9,18.5,17.4,12.2,7.7,4.5,6.9,3.4,11.1]]
k=3
centeroid=[[l[0][6],l[1][6]],[l[0][5],l[1][5]],[l[0][10],l[1][10]]]
#centeroid=[[3.8,9.9],[6.2,18.5],[7.8,12.2]]
#print(centeroid)
o=divideIntoCenteroids(centeroid,l)
#print(o)
print("First Clusture: ")
plotCenteroids(o)
oold=centeroid
bold=o
for i in range(10):
    cnew=new_centeroids(o)
    o=divideIntoCenteroids(cnew,l)
    
    if(compareClustures(bold,o)):
        print('No chnage in clustures')
        break
    bold=o
    if(compareEqulas(oold,cnew)):
        break
    oold=cnew
    print((i+1),"th iteration Clusture")
    plotCenteroids(o)
    
        


