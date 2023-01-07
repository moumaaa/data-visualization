from dash import Dash, html, dcc,  Input, Output
import plotly.express as px
import pandas as pd
from advance import fetch_data

app = Dash(__name__)

df = fetch_data()

app.layout = html.Div(children=[
    html.H1(children='Dynamic Visualization with Filtering Per Country Manufacturer'),
    html.P(children='''
        Data on the largest U.S. Car Manufacturers including Foreign Manufacturers with U.S Operations. URL: https://www.thomasnet.com/articles/top-suppliers/car-manufacturers-in-usa/
    '''),
    dcc.Dropdown(df["Country"].unique(), id='country-dropdown'),
    dcc.Graph(id='graph-with-dropdown')
    
])


@app.callback(
    Output('graph-with-dropdown', 'figure'),
    Input('country-dropdown', 'value'))
def update_figure(selected_country):

    if not selected_country:
        fig = px.bar(df, x="Country", y="Number of Manufacturers")
        
    else:    

        fig = px.bar(df[df.Country == selected_country], x="Country", y="Number of Manufacturers")

    fig.update_layout(transition_duration=500)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)