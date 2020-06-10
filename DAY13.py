1.	Write a Pandas program to create and display a one-dimensional array-like object containing an array of data.

import pandas as pd
s = pd.Series([3, 5, 6, 9, 1])
print(s)

2.	Write a Pandas program to create and display a one-dimensional array-like object containing an array of data.

import pandas as pd
s = pd.Series([3, 5, 6, 9, 1])
print(s)

3.	Write a Pandas program to create and display a one-dimensional array-like object containing an array of data.

import pandas as pd
s = pd.Series([3, 5, 6, 9, 1])
print(s)

4.	Write a Pandas program to compare the elements of the two Pandas Series.

import pandas as pd
s1 = pd.Series([12, 24, 36, 48, 60])
s2 = pd.Series([13, 26, 39, 52, 65])
print(s1)
print(s2)
print(s1 == s2)
print(s1 > s2)
print(s1 < s2)

5.	Write a Pandas program to convert a dictionary to a Pandas series.Sample dictionary: 
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}

import pandas as pd
d = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
print(d)
pan_series = pd.Series(d)
print(pan_series)

6.	Write a Pandas program to convert a NumPy array to a Pandas series.

import numpy as np
import pandas as pd
num_array = np.array([1, 2, 3, 4, 5])
print(num_array)
pan_series = pd.Series(num_array)
print(pan_series)

7.	Write a Pandas program to change the data type of given a column or a Series.

import pandas as pd
s1 = pd.Series(['10', 'how', '15', '20', 'doing'])
print(s1)
s2 = pd.to_numeric(s1, errors='coerce')
print(s2)

8.	Write a Python Pandas program to convert the first column of a DataFrame as a Series.

import pandas as pd
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
df = pd.DataFrame(data=d)
print(df)
s1 = df.ix[:,0]
print(s1)
print(type(s1))

d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
9.	Write a Pandas program to convert a given Series to an array.

import pandas as pd
import numpy as np
s1 = pd.Series(['10', 'how', '15', '20', 'doing'])
print(s1)
x = np.array(s1)
print (x)

10.	Write a Pandas program to sort a given Series.
(['100', '200', 'python', '300.12', '400'])

import pandas as pd
s1 = pd.Series(['10', 'how', '15', '20', 'doing'])
print(s1)
s2 = pd.Series(s1).sort_values()
print(s2)
