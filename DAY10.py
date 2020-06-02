1.	Write a NumPy program to get the numpy version and show numpy build configuration.
import numpy as np
print(np.__version__)
print(np.show_config())


2.	Write a NumPy program to test element-wise for complex number, real number of a given array. Also test whether a given number is a 
scalar type or not.

import numpy as np
a = np.array([10,20,30,60,2+1j,1+0j,2.25,2j])
print("Array",a)
print(np.iscomplex(a))
print(np.isreal(a))
print(np.isscalar(1))
print(np.isscalar([3]))

3.	Write a NumPy program to test whether none of the elements of a given array is zero.
import numpy as np
a = np.array([10, 20, 30, 40])
print("Array",a)
print(np.all(a))

4.	Write a NumPy program to test whether any of the elements of a given array is non-zero.
import numpy as np
a = np.array([10, 20, 0, 0])
print("Array",a) 
print(np.any(a))


5.	Write a NumPy program to test element-wise for NaN of a given array.
import numpy as np
a = np.array([10, 0, np.nan])
print("Array",a)
print(np.isnan(a))

6.	Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.
import numpy as np
a = np.array([10, 50])
b = np.array([20, 50])
print(a)
print(b)
print(np.greater(a,b))
print(np.greater_equal(a,b))
print(np.less(a,b))
print(np.less_equal(a,b)


7.	Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.
Input:
x = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])

import numpy as np
x = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
print(np.allclose(x,y))

8.	Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.

import numpy as np
a = np.array([1, 7, 13, 105])
print(a)
print("%d bytes" % (a.size * a.itemsize))

9.	Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives.

import numpy as np
a=np.zeros(10)
print(a)
a=np.ones(10)
print(a)
a=np.ones(10)*5
print(a)

10.	Write a NumPy program to create an array of the integers from 30 to 70.

import numpy as np
a=np.arange(30,71)
print(a)

11.	Write a NumPy program to create an array of all the even integers from 30 to 70.

import numpy as np
a=np.arange(30,71,2)
print(a)

12.	Write a NumPy program to create a 3x3 identity matrix.

import numpy as np
a=np.identity(3)
print(a)

13.	Write a NumPy program to generate a random number between 0 and 1.

import numpy as np
a= np.random.normal(0,1,1)
print(a)

14.	Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution.

import numpy as np
a = np.random.normal(0,1,15)
print(a)

15.	Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.

import numpy as np
a = np.arange(15,55)
print(a)
print(a[1:-1])
