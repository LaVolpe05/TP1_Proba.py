import math
from random import random
import random as rd




def question1B(tirage,M):
    a = 0
    b = 1
    S = 0
    for i in range(tirage):
        x = rd.uniform(a,b)
        y = rd.uniform(0,M)
        if( y <= math.sqrt(M**2-x**2)):
            S += 1
    return (S*(b-a)*M)/(tirage)

def question1A(tirage,a,b):
    S = 0
    for i in range(tirage):
        x = rd.uniform(a,b)
        S += math.sqrt(1-x**2)
    return (S*(b-a))/tirage

def question2A1():
    n = 0
    while(not n > 1):
        n += rd.uniform(0,1)

    return n
def question2A2(N):
    sum = 0
    for i in range(N):
        sum +=question2A1()

    return 2*sum/N

if __name__ == "__main__":

    #print(Pi)
    #print(4*question1A(100000000,0,1))
    #print(4*question1B(100000000,1))
    print(question2A2(1000000))