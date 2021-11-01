import numpy as np
import plotly.graph_objects as go

data = np.genfromtxt('activity-export-DailyStep_Calle_Studietur.csv', delimiter = ',', names=["Dato", "Skridt"])

fig = go.Figure(go.Scatter(x = data['Dato'], y = data['Skridt'],
                  name='Skridt'))

fig.update_layout(title='Apple Share Prices over time (2014)',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)

fig.show()