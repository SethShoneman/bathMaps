import plotly.graph_objects as go
import repository as rep

token = "pk.eyJ1IjoidWdoaXRzc2lkIiwiYSI6ImNrNm54Z3I5cTE1aDIzbW55MjcwdWp4MnEifQ.xylSSPUA0Yt9ly6jOBMg4w"

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
        pitch=0,
        zoom=14
    ),
)

fig.show()