from dash import Dash, dcc, html, dash_table, Input, Output, callback
import plotly.express as px
from f1_data import get_f1_laps_df, get_f1_telemetry_df, get_f1_session_data


app = Dash(__name__)
0
colors = {
    'background': '#FFFFFF',
    'text': '#7FDBFF'
}

year, grand_prix, session = 2023, 'Spain', 'R'
drivers = ['VER', 'LEC']

laps_df = get_f1_laps_df(drivers, year, grand_prix, session)
telemetry_df = get_f1_telemetry_df(drivers, year, grand_prix, session)
session_df = get_f1_session_data(year, grand_prix, session)

fig_1 = px.line(laps_df, x="LapNumber", y="LapTime", color="Driver")
fig_2 = px.scatter(telemetry_df, x="X", y="Y",  color="Speed")
fig_3 = px.box(laps_df, x="Driver", y="LapTime", points="all")
fig_4 = px.line(session_df, x="LapNumber", y="Position", color='Driver')
#fig_5 = px.imshow(session_df, x="LapNumber", y="Driver")


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='F1 race result',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div([dash_table.DataTable(data=laps_df.to_dict('records'), page_size=20)]),
    html.Div([dash_table.DataTable(data=telemetry_df.to_dict('records'), page_size=20)]),
    html.Div([dash_table.DataTable(data=session_df.to_dict('records'), page_size=20)]),

    dcc.Graph(id='example-graph-1', figure=fig_1),
    dcc.Graph(id='example-graph-2', figure=fig_2),
    dcc.Graph(id='example-graph-3', figure=fig_3),
    dcc.Graph(id='example-graph-4', figure=fig_4),
    #dcc.Graph(id='example-graph-5', figure=fig_5),
])

@callback(
    Output('dd-output-container', 'children'),
    Input('pilot-dropdown', 'value')
)

def update_output(value):
    return f'You have selected: {value}'



if __name__ == '__main__':
    app.run(debug=True)