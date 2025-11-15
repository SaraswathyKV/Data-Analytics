import pandas as pd
data = pd.DataFrame({
    'Name' : ['Ankit','Aishwarya','Sanket','Shivangi','Saiprasad','Rishika','Pratisksha'],
    'Age' : [23,21,22,21,22,21,20],
    'University' : ['BHU','JNU','DU','BHU','SPPU','SPPU','DU'],
                    })
data.to_csv('students.csv', index = False)
students = pd.read_csv('D:/UM/Data Analyst & Data Science-20251010T044752Z-1-001/students.csv')
print(students)
grouped = students.groupby('University')
sppu = grouped.get_group('SPPU')
print(sppu)
print(students['Age'].mean())
data['City'] = ['Delhi', 'Banglore', 'Chennai', 'Patna', 'Pune','Pune','Mumbai']
#print(data)
data.columns = ['First Name','Current Age','College University','Location']
#data.columns = data.columns.str.strip()
data.drop(['Current Age'], axis = 1)
print(data)
data.drop(['Current Age'], axis = 1, inplace = True)
print(data)
data['Marks'] = [201,210,195,183,225,203,190]
print(data)
data['Marks'] = data['Marks'].apply(lambda x:x/5)
print(data)
data.columns = ['First Name','College Univerrsity','Location','Marks/Subject']
print(data)
data.index=[10,28,64,7,1,6,15]
print(data)
data.sort_index(ascending = False, inplace=True)
print(data)
data.sort_values(by = 'Marks/Subject', ascending = False, inplace=True)
print(data)