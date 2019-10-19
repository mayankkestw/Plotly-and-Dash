import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

x = np.random.randint(1,101,100)
y = np.random.randint(1,101,100)

data = [go.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker=dict(
        size=12,
        color='rgb(51,204,153)',
        symbol='pentagon',
        line=dict(width=2)
    )
)]

layout  = go.Layout(
    title='Hello',
    xaxis=dict(title='X-axis'),
    yaxis=dict(title='Y-axis'),
    hovermode='closest'
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter.html')