import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


df = pd.read_csv('../Data/2018WinterOlympics.csv')

trace1 = go.Bar(x=df['NOC'], y=df['Gold'], name='Gold', marker=dict(color='#ffd700'))
trace2 = go.Bar(x=df['NOC'], y=df['Silver'], name='Silver', marker=dict(color='#9ea0a1'))
trace3 = go.Bar(x=df['NOC'], y=df['Bronze'], name='Bronze', marker=dict(color='#cd7f32'))


data = [trace1, trace2, trace3]

layout = go.Layout(
    title='Medals',
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='Stack-bar.html')
# pyo.plot(fig, filename='Nested-bar.html')