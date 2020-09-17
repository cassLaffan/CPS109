'''
Write a function that takes as inputs the a,b and c coefficients of a quadratic equation
of the form ax^2 + bc + c = 0 and calculates and prints the roots. Round the output to the nearest hundredth  
Otherwise, if there are no roots, print 'Has no solution'

Recall: The quadratic formula https://en.wikipedia.org/wiki/Quadratic_formula
Recall: You can check if a quadratic's roots do not exist by checking if the discriminant (the part under the square root sign) is negative.
'''

def getRoots(a,b,c):
  disc = b**2 - 4*a*c
  if disc >= 0:
      v1 = (-b + (disc)**0.5) / (2*a)
      v2 = (-b - (disc)**0.5) / (2*a)
    print(round(v1,2),round(v2,2))
   else:
      print('Has no solution')
      
a,b,c = 1,1,-12
d,e,f = 1,0,1

getRoots(a,b,c) #3.00,-4.00
getRoots(d,e,f) #Has no solution


  
