import pandas as pd
# Read the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')


# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)

print(s)

print(s[2])     # Access the element with label 2 (value 30)
print(s.iloc[3]) # Access the element at position 3 (value 40)
print(s[1:4])   # Access a range of elements by label

import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

print(df)

print(df['Name'])  # Access the 'Name' column
print(df.iloc[2])   # Access the third row by position
print(df.loc[1])    # Access the second row by label
print(df[['Name', 'Age']])  # Select specific columns
print(df[1:3])             # Select specific rows

unique_dates = df['Age'].unique()

high_above_102 = df[df['Age'] > 25]

df.to_csv('trading_data.csv', index=False)

#----------------------------------------------------


#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
df

#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
x

#check the type of x
type(x)

#Retrieving the Department, Salary and ID columns and assigning it to a variable z

z = df[['Department','Salary','ID']]
z



x = {'Student': ['David','Samuel', 'Terry', 'Evan'], 'Age': [27,24,22,32], 'Country': ["UK","Canada","China","USA"], 'Course': ['Python', 'Data Structures', 'Machine Learning', 'Web Development'], 
      'Marks':[85,72,89,76]}
df1 = pd.DataFrame(x)
df1
b = df1[["Marks"]]
b
c = df1[["Country", "Course"]]
c
x = df1['Student']
x
type(x)
df.iloc[0, 0]
df.iloc[0,2]
df.loc[0, 'Salary']

df2=df
df2=df2.set_index("Name")
#To display the first 5 rows of new dataframe
df2.head()

#Now, let us access the column using the name
df2.loc['Jane', 'Salary']

df2.loc["Jane","Department"]
df2.iloc[3,2]

#Slicing
df.iloc[0:2, 0:3]
df.loc[0:2,'ID':'Department']
df2.loc['Rose':'Jane', 'ID':'Department']

#--------------------------------------------------------

# Read data from CSV file

# csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
# df = pd.read_csv(csv_path)

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv"
df = pd.read_csv(filename)

# Print first five rows of the dataframe
df.head()

# Access to the column Length
x = df[['Length']]
x

# Get the column as a series
x = df['Length']
x

# Get the column as a dataframe
x = df[['Artist']]
type(x)

# Access to multiple columns
y = df[['Artist','Length','Genre']]
y

# Access the value on the first row and the first column
df.iloc[0, 0]

# Access the value on the second row and the first column
df.iloc[1,0]

# Access the value on the first row and the third column
df.iloc[0,2]

# Access the value on the second row and the third column
df.iloc[1,2]

# Access the column using the name
df.loc[1, 'Artist']

# Access the column using the name
df.loc[0, 'Released']

# Slicing the dataframe
df.iloc[0:2, 0:3]

# Slicing the dataframe using name
df.loc[0:2, 'Artist':'Released']