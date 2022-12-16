# import pandas as pd 
# import numpy as np 
# info = np.array(['P','a','n','d','a','s']) 
# a = pd.Series(info) 
# print(a)


# import pandas as pd 
# # a list of strings 
# x = ['Python', 'Pandas'] 
 
# # Calling DataFrame constructor on list 
# df = pd.DataFrame(x) 
# print(df) 

# import pandas as pd 
# x = pd.Series() 
# print (x) 

# import pandas as pd 
# import numpy as np 
# info = np.array(['P','a','n','d','a','s','m','n']) 
# a = pd.Series(info) 
# print(a) 

# import pandas as pd;
# info = {'x' : 0., 'y' : 1., 'z' : 2.} 
# a = pd.Series(info) 
# print (a) 

# x = pd.Series("m", index=[0, 1, 2, 3]) 
# print (x) 

# x = pd.Series([1,2,3],index = ['a','b','c']) 
#retrieve the first element 
# print (x[2])

# a=pd.Series.size(['x',0, 'y', 1, 'z' ,2])
# print(a) 

# import numpy as np 
# import pandas as pd 
# a=pd.Series(data=[1,2,3,4]) 
# b=pd.Series(data=[4.9,8.2,5.6], 
# index=['x','y','z']) 
# print(a.dtype) 
# print(a.itemsize) 
# print(b.dtype) 
# print(b.itemsize) 

# print(a.shape) 
# # print(b.shape) 
# a=pd.Series(data=[1,2,3,np.NaN]) 
# b=pd.Series(data=[4.9,8.2,5.6],index=['x','y','z']) 
# c=pd.Series()
# print(a.ndim, b.ndim) 
# print(a.size, b.size) 
# print(a.nbytes, b.nbytes)
# print(a.empty,b.empty,c.empty) 
# print(a.hasnans,b.hasnans,c.hasnans) 
# print(len(a),len(b)) 
# print(a.count( ),b.count( )) 

# index = pd.Index([2, 1, 1, np.nan, 3]) 
# index.value_counts()
# print(index)

# a={1,2,3,4,6}
# a=[1,2,4,5,76]
# b=a.pop()
# print(a)
# print(b)