import pandas as pd
import plotly.graph_objects as go


gdl_metro_stations = pd.read_csv("gdl_metro.csv")
fig = go.Figure(go.Scattermapbox(
    lat=gdl_metro_stations["lat"],
    lon=gdl_metro_stations["lon"],
    mode="markers+text+lines",
    marker=go.scattermapbox.Marker(
        size=14,
        color=gdl_metro_stations["Line"],
    ),
    text=gdl_metro_stations["Station"],
))
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0,
                          "t": 0,
                          "l": 0,
                          "b": 0})
fig.update_layout(
    hovermode='closest',
    mapbox=dict(
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=20.677911291920235,
            lon=-103.3471823866469
        ),
        pitch=0,
        zoom=11,

    )
)
fig.show()
