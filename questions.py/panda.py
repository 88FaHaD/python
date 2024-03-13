import pandas as pd

data = {
    'name': ['harry', 'john', 'july', 'sam'],  
    'marks': [90, 80, 30, 85],
    'city': ['calafornia', 'london', 'dubai', 'sydney']
}

df = pd.DataFrame(data)
print(df)

df.to_csv('friends.csv')
df.to_csv('newfriends.csv',index=False)

print(df.head(2)) #prints top 2 elements
print(df.tail(2)) #prints bottom 2 elements
print()
print(df.describe()) # calculats count standard deviation mean and other stuff

#changing the marks
ff=pd.read_csv('friends.csv')
ff['marks'][0]=50
print(ff)