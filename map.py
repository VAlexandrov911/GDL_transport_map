import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

gdl_metro_stations = pd.read_csv("gdl_metro.csv")

# 1 line
fig = go.Figure()
fig.add_trace(go.Scattermapbox(
    name='Mi Tren L1',
    lat=gdl_metro_stations["lat"][1:22],
    lon=gdl_metro_stations["lon"][1:22],
    mode="markers+text+lines",
    marker=go.scattermapbox.Marker(
        size=14,
        symbol=gdl_metro_stations["Type"][1:22]
    ),
    line=go.scattermapbox.Line(
        color='brown',
        width=3
    ),
    text=gdl_metro_stations["Station"][1:22],
    textfont=dict(size=15, color='brown'),
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
        color='darkgreen',
        width=3
    ),
    text=gdl_metro_stations["Station"][22:33],
    textfont=dict(size=15, color='darkgreen'),
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
        color='red',
        width=3
    ),
    text=gdl_metro_stations["Station"][33:52],
    textfont=dict(size=15, color='red'),
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
        color='darkcyan',
        width=2
    ),
    text=gdl_metro_stations["Station"][52:80],
    textfont=dict(size=15, color='darkcyan'),
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
        symbol=gdl_metro_stations["Type"][80:123],
        color='purple'
    ),
    line=go.scattermapbox.Line(
        color='purple',
        width=2
    ),
    text=gdl_metro_stations["Station"][80:123],
    textfont=dict(size=15, color='purple'),
    textposition="bottom right",
    showlegend=True
))

fig.update_layout(margin={"r": 5,
                          "t": 5,
                          "l": 5,
                          "b": 5}
                  )
fig.update_layout(mapbox_bounds={"west": -103.6,
                                 "east": -103.1,
                                 "south": 20.5,
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
# fig.show()

app = dash.Dash(external_stylesheets=[dbc.themes.UNITED])

title = dcc.Markdown(
    """
## Guadalajara Transport Map
    My attempt to show main public lines and stations together @VAlex
------------
"""
)

app.layout = html.Div([
    title,
    dcc.Graph(figure=fig, style={"height": 615})
])

app.run_server(debug=True, use_reloader=False)
