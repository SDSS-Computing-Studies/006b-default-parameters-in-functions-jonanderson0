#! python3

import math

def tempConversion(degrees, unit="C"):
  deg1=(degrees*1.8)+32
  if unit=="F":
    deg1=((degrees-32)*(5/9))
  deg1=round(deg1,1)
  return deg1



def factorPair(num,a):
  b = int(num/a)
  answer = [a,b]
  answer.sort()
  return answer



def cosineLaw(a,b,c,oppositeSide=True):
  c = toRadians(c)
  if oppositeSide == True:
    ans2 = (a ** 2)-(b ** 2)
    s = quadratic(a1,b1,c1)
    x = solution(s)
    return x
  if b < a:
    a1 = 1
    b1 = -2 * (b) * (math.cos(c))
    c1 = (b **2)-(a ** 2)
    s = quadratic(a1,b1,c1)
    x = solution(s)
    return x
 

def toRadians(angled):
  radians=(angled*math.pi)/180
  return radians

def solution(solution):
  solutions.sort()
  x2 = solutions[1]
  return x2

def quadratic(a,b,c):
  x1 = (-b + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
  x2 = (-b - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
  quadAnswer = [x1,x2]
  quadAnswer.sort()
  return quadAnswer

