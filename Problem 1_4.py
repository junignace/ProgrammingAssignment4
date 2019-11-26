import pandas as pd

math = {'Student' : ['Ice Bear', 'Panda', 'Grizzly'], 'Math': [80,95,79]}
electronics = {'Student' :  ['Ice Bear', 'Panda', 'Grizzly'], 'Electronics':[
        85,81,83]}
geas= {'Student' : ['Ice Bear', 'Panda', 'Grizzly'], 'GEAS': [90,79,93]}
esat = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'ESAT': [93,89,88]}

df1= pd.DataFrame(math, columns = ['Student', 'Math'])
df2= pd.DataFrame(electronics, columns = ['Student', 'Electronics'])
df3= pd.DataFrame(geas, columns = ['Student', 'GEAS'])
df4= pd.DataFrame(esat, columns= ['Student', 'ESAT'])

m1= pd.merge(df1,df2, how='right', on='Student')
m2 = pd.merge(m1,df3, how='right', on='Student')
m3 = pd.merge(m2,df4, how= 'right', on='Student')