from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame({
    "Automaker": ["GM", "Ford", "Toyota", "Honda", "Subaru"],
    "Estimated Annual Revenue (Billion)": [122, 127, 279, 142, 29],
    "Headquarters": ["Detroit", "Dearborn", "Toyota City", "Tokyo", "Tokyo"]
})

fig = px.bar(df, x="Automaker", y="Estimated Annual Revenue (Billion)", color="Headquarters")

app.layout = html.Div(children=[
    html.H1(children='Simple Dynamic Visualization Page'),

    html.P(children='''
        Data on the largest U.S. Car Manufacturers including Foreign Manufacturers with U.S Operations. URL: https://www.thomasnet.com/articles/top-suppliers/car-manufacturers-in-usa/
    '''),

    dcc.Graph(
        id='sample-graph',
        figure=fig
    )
])

if __name__ == '_main_':
    app.run_server(debug=True)