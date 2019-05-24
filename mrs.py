
import pandas as pd
data=pd.read_csv('E:\\MLP\\MRS\\Final\\movie_liking.csv')
udata=pd.read_csv('E:\\MLP\\MRS\\Final\\user_liking.csv')

print("Enter user id")
u=int(input())

dataset=pd.read_csv('E:\\MLP\\MRS\\Final\\dataset.csv')
userratings=pd.read_csv('E:\\MLP\\MRS\\Final\\user_ratings.csv')

myratings=(userratings.loc[u].dropna())
row=data.shape[0]
myratings=myratings.to_frame()

myratings=myratings.T
mw=list(myratings.columns)

for i in range(row-1,0,-1) :
    if(data.iat[i,1] in mw) :
        data=data.drop(data.index[i])

g1=udata.iat[u-1,20]
g2=udata.iat[u-1,21]
g3=udata.iat[u-1,22]

a1=data.iloc[:,[0,1,3,g1+4]]
a2=data.iloc[:,[0,1,3,g2+4]]
a3=data.iloc[:,[0,1,3,g3+4]]

b1=list(a1.columns)
b2=list(a2.columns)
b3=list(a3.columns)
str1=b1[3]
str2=b2[3]
str3=b3[3]

a1=a1.sort_values(by=[str1],ascending=False)
a2=a2.sort_values(by=[str2],ascending=False)
a3=a3.sort_values(by=[str3],ascending=False)

ans=[]
for i in range(5) :
    ans.append(a1.iat[i,1])
for i in range(3) :
    ans.append(a2.iat[i,1])
for i in range(2) :
    ans.append(a3.iat[i,1])
for i in range(len(ans)) :
    print(ans[i])
