import matplotlib.pyplot as plt
import math


#Find number of words and unique words manually in txt. file
###############################################################
text_file = open('TGG.txt', 'r')
text = text_file.read()

#Tokenizing 
text = text.lower()
words = text.split()
words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]

#Get total number of words
def get_total(list):
    count = 0
    for element in words:
        count += 1
    return count

totalWords= get_total(words)

#Find the unique words
unique = []
for word in words:
    if word not in unique:
        unique.append(word)
        
#Get total number of unique words     
def get_number_of_elements(list):
    count = 0
    for element in unique:
        count += 1
    return count

uniqueWords= get_number_of_elements(unique)

#Create collection sizes based on number of total words

x= [round(totalWords/4), round(totalWords/2),round((totalWords*3)/4), totalWords]


#Create new list of words based on collection sizes and find the number of unique words within those respective collections. 
p1 = []
u1 = []
p2= []
u2 =[]
p3=[]
u3=[]
p4 =[]
u4=[]

a= x[0]
b= x[1]
c= x[2]
d= x[3]

p1= words[:a]
p2= words[:b]
p3= words[:c]
p4= words[:d]

for e in p1:
    if e not in u1:
        u1.append(e)
        
for e in p2:
    if e not in u2:
        u2.append(e)

for e in p3:
    if e not in u3:
        u3.append(e)

for e in p4:
    if e not in u4:
        u4.append(e)


y =[]
y.append(len(u1))
y.append(len(u2))
y.append(len(u3))
y.append(len(u4))

#Estimation based on Heap's Law Formula
#The Formula:  V(n) = K n^β  => log V(n) = β log(n) + K

B= (math.log(y[1])- math.log(y[2]))/(math.log(x[1])- math.log(x[2]))
K= (y[1]/(x[1]**B))

V= K*float(totalWords)**B

y2=[]

for e in x:
    V= K*float(e)**B
    y2.append(V)

#Plotting the data    
print("In this document, there are", totalWords, "total words with", uniqueWords, "of them being unique.")
print("Estimated K value: ", K)
print("Estimated β value is ", B)
print("Estimated V(n) value is", V)

plt.xlim(x[0], x[3])
plt.ylim(y[0], y[3])

plt.xlabel("n (Total Words)")
plt.ylabel("V(n) (Distinct Words)")
plt.title("Heap's Law Analysis")


#plot calculated values
plt.plot(x,y, 'r', label= "Calculated Values")

#plot heap's law values
plt.plot(x,y2, 'b', label= "Heap's Law Values")

plt.legend(loc="upper left")
plt.show()