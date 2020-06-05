1.	  Write a NumPy program to create a 3X4 array using and iterate over it.

import numpy as np
a = np.arange(10,22).reshape((3, 4))
print(a)
for i in np.nditer(a):
  print(i,end=" ")
  
2.	Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.

import numpy as np
a = np.arange(15,55)
print(a)
print(a[1:-1])

3.	Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.

import numpy as np
a = np.arange(21)
print(a)
a[(a >= 9) & (a <= 15)] *= -1
print(a)
4.	 Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.

import numpy as np
a = np.random.randint(0, 11, 5)
print(a)

5.	Write a NumPy program to multiply the values of two given vectors.

import numpy as np
a = np.array([1, 2, 3, 4])
print(a)
b= np.array([1,5, 6, 4])
print(b)
result = a * b
print(result)

6.	Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.

import numpy as np
a= np.arange(10,22).reshape((3, 4))
print(a)

7.	 Write a NumPy program to find the number of rows and columns of a given matrix.

import numpy as np
a= np.arange(10,22).reshape((3, 4))
print(a)
print(a.shape)

8.	Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0.

import numpy as np
a = np.eye(3)
print(a)

9.	 Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.

import numpy as np
a = np.ones((10, 10))
a[1:-1, 1:-1] = 0
print(a)

10.	Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.

import numpy as np
a = np.diag([1, 2, 3, 4, 5])
print(a)

11.	Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.

import numpy as np
a = np.zeros((4, 4))
a[::2, 1::2] = 1
a[1::2, ::2] = 1
print(a)

12.	Write a NumPy program to create a 3x3x3 array filled with arbitrary values.

import numpy as np
a = np.random.random((3, 3, 3))
print(a)

13.	Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of a given array. 

import numpy as np
a = np.array([[0,1],[2,3]])
print(a)
print(np.sum(a))
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))

14.	Write a NumPy program to compute the inner product of two given vectors.

import numpy as np
a = np.array([4, 5])
b = np.array([7, 10])
print(a)
print(b)
print(np.dot(a, b))

15.	Write a NumPy program to add a vector to each row of a given matrix

import numpy as np
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
b = np.array([1, 0, 2])
print(a)
print(b)
c = np.empty_like(a) 
for i in range(4):
  c[i, :] = a[i, :] + b
print(c)
