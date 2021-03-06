#! python3

import math

def tempConversion(degrees, unit="C"):
  if unit== "C":
    answer = (degrees * 9/5) + 32
  if unit== "F":
    answer = (degrees - 32) * 5/9
    
  answer = round(answer,1)
  return answer



def factorPair(num,a):
  b = int(num/a)
  answer = [a,b]
  answer.sort()
  return answer



def cosineLaw(a,b,c,oppositeSide=True):
  c = toRadians(c)
  if oppositeSide == True:
    ans2 = (a ** 2) + (b ** 2) - 2 * a * b * math.cos(c)
    s = math.sqrt(ans2)
    return s
  else:
    if a > b:
      a1 = 1
      b1 = -2 * (a) * (math.cos(c))
      c1 = (a ** 2)-(b ** 2)
      s = quadratic(a1,b1,c1)
      x = solution(s)
      return x
 

def toRadians(angled):
  radians=(angled*math.pi)/180
  return radians

def solution(solution):
  solution.sort()
  x2 = solution[1]
  return x2

def quadratic(a,b,c):
  x1 = (-b + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
  x2 = (-b - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
  quadAnswer = [x1,x2]
  quadAnswer.sort()
  return quadAnswer

