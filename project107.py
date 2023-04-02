import csv
import plotly.express as px
import pandas as pd

data = pd.read_csv('data.csv')
mean_of_data = data.groupby(['student_id','level'],as_index=False)['attempt'].mean()

scatter = px.scatter(mean_of_data,x = 'student_id',y='level',color='attempt',size='attempt')
scatter.show()