import pandas as pd
import numpy as np
data = pd.DataFrame({'team':['A','A','A','A','B','B','B','B'],
                     'points': [10,10,12,12,15,17,20,20],
                     'assists': [5,5,7,9,12,9,6,6]})
print(data)
print(data[data.duplicated()])
team = data.duplicated(['team'])
print(data[team])
print(data)
team_pts = data.duplicated(['team','points'])
print(data[team_pts])
print(data.drop_duplicates())
print(data.drop_duplicates(['team']))
print(data.drop_duplicates(['team','points']))
values = [1,2,3,4,5,6,9,10,12,55,60]
print(values)
Q1 = np.percentile(values,25)
print(Q1)
Q3 = np.percentile(values,75)
print(Q3)
IQR = Q3 - Q1
print(IQR)
low = Q1 - 1.5 * IQR
upp = Q1 + 1.5 * IQR
print(low,upp)
outliers = []
print(values)
for i in values:
        if((i > upp) or (i<low)):
            outliers.append(i)
print(outliers)
for i in values:
      if i not in outliers:
            print(i)
values = [i for i in values if i not in outliers]
print(values)
print(outliers)