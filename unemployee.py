#Import the Libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#File path  
df = pd.read_csv("C:/Users/91705/Desktop/Internship/unemployment_in_India.csv")
df.head()

df.describe()

df.isna().sum()
df.info()
df = df.rename(columns={df.columns[0]:'State',df.columns[3]:'EUR',df.columns[4]:'EE', df.columns[5]:'ELPR', df.columns[6]:'Region'})
df.head()
df.State.unique()
group_region = df.groupby(['Region'])[['EUR', 'EE', 'ELPR']].mean().reset_index()
group_region = round(group_region,2)
group_region

fig = px.bar(group_region, x="Region", y="EUR", color="Region", title="Average Unemployment Rate by Region")
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.show()

group_state = df.groupby(['State'])[['EUR', 'EE', 'ELPR']].mean().reset_index()
group_state = round(group_state,2)
group_state.head()

fig = px.bar(group_state, x="State", y="EUR", color="State", title="Unemployment Rate Analysis")
fig.show()

unemployment = df[["State", "Region", "EUR"]]

fig = px.sunburst(unemployment, path=['Region','State'], values='EUR',
                  title= 'Unemployment rate in every State and Region', height=650)
fig.show()

df1 = pd.read_csv('/kaggle/input/unemployment-in-india/Unemployment in India.csv')
df1.head()

df1['Area'].value_counts()

sns.countplot(x=df1['Area'], palette="Set2")
plt.show()
