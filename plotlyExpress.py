import plotly.graph_objects as go
import repository as rep

token = "pk.eyJ1IjoidWdoaXRzc2lkIiwiYSI6ImNrNm54Z3I5cTE1aDIzbW55MjcwdWp4MnEifQ.xylSSPUA0Yt9ly6jOBMg4w"

spaces='                                                                                                           '

lats = [rep.codeDay.lat, rep.sb1.lat, rep.chpt1.lat, rep.pnbrd1.lat]
lons = [rep.codeDay.lon, rep.sb1.lon, rep.chpt1.lon, rep.pnbrd1.lon]
texts = [rep.codeDay.text, rep.sb1.text, rep.chpt1.text, rep.pnbrd1.text]

fig = go.Figure(go.Scattermapbox(
        lat=lats,
        lon=lons,
        mode='markers',
        marker=go.scattermapbox.Marker(size=14),
        text=texts,
    ))

fig.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=token,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=rep.avgLat,
            lon=rep.avgLon
        ),
        style='outdoors',
        pitch=0,
        zoom=14
    ),
)

import json
from textwrap import dedent as d

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(
        id='basic-interactions',
        figure=fig
    ),

    # dcc.Link(
    #     'Navigate to "Leave a Review"',
    #     href='https://docs.google.com/forms/d/e/1FAIpQLSdA-ITHtdfyulyhr2ZOlWZ624AErDcd1gvJDaro22RtleY-zw/viewform'
    # ),

    html.Div(className='row', children=[
         html.Div([
             dcc.Markdown(d("")),
             html.Pre(id='hover-data')
        ], className='three columns'),

        html.Div([
            dcc.Markdown(d("")),
            html.Pre(id='click-data'),
        ], className='three columns',)
    ])
])


@app.callback(
    Output('hover-data', 'children'),
    [Input('basic-interactions', 'hoverData')])
def display_hover_data(hoverData):
    if hoverData == None:
        print('None')
    else:
        x = hoverData['points']
        x = x[0]
        out = (spaces+str(x['lon']) + ', ' + str(x['lat']) + ' - ' + x['text'])
        return json.dumps(out)

@app.callback(
    Output('click-data', 'children'),
    [Input('basic-interactions', 'clickData')])

def click_to_page(clickData):
    if clickData == None:
        print('None')
    else:
        x = clickData['points']
        x = x[0]
        print(x['text'])
        return dcc.Link(
        "Leave a Review",
        href='https://docs.google.com/forms/d/e/1FAIpQLSdA-ITHtdfyulyhr2ZOlWZ624AErDcd1gvJDaro22RtleY-zw/viewform')

app.run_server(debug=True)
