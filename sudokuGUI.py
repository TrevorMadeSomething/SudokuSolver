import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash(__name__)

params = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

app.layout = html.Div([
    dash_table.DataTable(id='table-editable',
                         columns=([{
                             'id': p,
                             'name': p
                         } for p in params]),
                         data=[
                             dict(Model=i, **{param: 0
                                              for param in params})
                             for i in range(0, 9)
                         ],
                         editable=True),
])

if __name__ == '__main__':
    app.run_server(debug=True)
