import pandas as pd
import plotly.graph_objects as go

gdl_metro_stations = pd.read_csv("gdl_metro.csv")

# 1 line
fig = go.Figure()
fig.add_trace(go.Scattermapbox(
    name='Mi Tren L1',
    lat=gdl_metro_stations["lat"][3:22],
    lon=gdl_metro_stations["lon"][3:22],
    mode="markers+text+lines",
    marker=go.scattermapbox.Marker(
        size=14,
        symbol=gdl_metro_stations["Type"][3:22]
    ),
    line=go.scattermapbox.Line(
        color='brown'
    ),
    text=gdl_metro_stations["Station"][3:22],
    textfont=dict(size=13, color='brown'),
    textposition="bottom right",
    showlegend=True
))

# 2 line
fig.add_trace(go.Scattermapbox(
    name='Mi Tren L2',
    lat=gdl_metro_stations["lat"][22:33],
    lon=gdl_metro_stations["lon"][22:33],
    mode="markers+text+lines",
    marker=go.scattermapbox.Marker(
        size=14,
        symbol=gdl_metro_stations["Type"][22:33]
    ),
    line=go.scattermapbox.Line(
        color='darkgreen'
    ),
    text=gdl_metro_stations["Station"][22:33],
    textfont=dict(size=13, color='darkgreen'),
    textposition="bottom right",
    showlegend=True
))

# 3 line
fig.add_trace(go.Scattermapbox(
    name='Mi Tren L3',
    lat=gdl_metro_stations["lat"][33:52],
    lon=gdl_metro_stations["lon"][33:52],
    mode="markers+text+lines",
    marker=go.scattermapbox.Marker(
        size=14,
        symbol=gdl_metro_stations["Type"][33:52]
    ),
    line=go.scattermapbox.Line(
        color='red'
    ),
    text=gdl_metro_stations["Station"][33:52],
    textfont=dict(size=13, color='red'),
    textposition="bottom right",
    showlegend=True
))

# 4 line
fig.add_trace(go.Scattermapbox(
    name='Mi Macro Calzada',
    lat=gdl_metro_stations["lat"][52:80],
    lon=gdl_metro_stations["lon"][52:80],
    mode="markers+text+lines",
    marker=go.scattermapbox.Marker(
        size=14,
        symbol=gdl_metro_stations["Type"][52:80]
    ),
    line=go.scattermapbox.Line(
        color='turquoise'
    ),
    text=gdl_metro_stations["Station"][52:80],
    textfont=dict(size=13, color='turquoise'),
    textposition="bottom right",
    showlegend=True
))

# 5 line
fig.add_trace(go.Scattermapbox(
    name='Mi Macro Periférico',
    lat=gdl_metro_stations["lat"][80:123],
    lon=gdl_metro_stations["lon"][80:123],
    mode="markers+text+lines",
    marker=go.scattermapbox.Marker(
        size=14,
        symbol=gdl_metro_stations["Type"][80:123]
    ),
    line=go.scattermapbox.Line(
        color='purple'
    ),
    text=gdl_metro_stations["Station"][80:123],
    textfont=dict(size=13, color='purple'),
    textposition="bottom right",
    showlegend=True
))

fig.update_layout(margin={"r": 0,
                          "t": 0,
                          "l": 0,
                          "b": 0}
                  )
fig.update_layout(mapbox_bounds={"west": -103.8,
                                 "east": -103,
                                 "south": 20,
                                 "north": 21}
                  )
fig.update_layout(
    hovermode='x unified',
    mapbox=dict(
        accesstoken='pk.eyJ1IjoiZGFuaWNhbiIsImEiOiJjam4xZjBxZm0zd2FyM3ZwbnFqanJnZG9jIn0.AM7q7GapFhEt_b_JAJVqNA',
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=20.661035901320137,
            lon=-103.35748477714348
        ),
        pitch=0,
        zoom=11.2,
        style="outdoors"
    )
)
fig.show()
