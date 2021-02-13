# visit https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html for plotly documentation
import plotly.graph_objects as go
import repository as rep

# this is the token used to generate the plotly map, may have to be regenerated
token = "pk.eyJ1IjoidWdoaXRzc2lkIiwiYSI6ImNrNm54Z3I5cTE1aDIzbW55MjcwdWp4MnEifQ.xylSSPUA0Yt9ly6jOBMg4w"

# the latitutes, longitudes, and names of the respective points. First lat corresponds to first lon and text, second to second, and so on
lats = [rep.codeDay.lat, rep.sb1.lat, rep.chpt1.lat, rep.pnbrd1.lat]
lons = [rep.codeDay.lon, rep.sb1.lon, rep.chpt1.lon, rep.pnbrd1.lon]
texts = [rep.codeDay.text, rep.sb1.text, rep.chpt1.text, rep.pnbrd1.text]

# create a new figure using plotly
# initialize the longitudes, latitudes, and texs as points
fig = go.Figure(go.Scattermapbox(
        lat=lats,
        lon=lons,
        mode='markers',
        marker=go.scattermapbox.Marker(size=14),
        text=texts,
    ))

# create the map with needed visual attributes
fig.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=token,
        bearing=0,
        center=go.layout.mapbox.Center(
            # center the map at a calculated average of the points' positions
            lat=rep.avgLat,
            lon=rep.avgLon
        ),
        pitch=0,
        zoom=14
    ),
)

fig.show()
