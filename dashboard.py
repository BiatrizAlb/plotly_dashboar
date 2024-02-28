#Created by Beatriz Albuquerque.
# Run this app with `python app.py`

from dash import Dash, dcc, html, Input, Output,callback
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("clinical_data_breast_cancer.csv")

df = df.loc[df["RPPA Clusters"]!="X", :]

fig = px.bar(df, x="Vital Status", y="OS Time", color="RPPA Clusters", barmode="group")

options = list(df['RPPA Clusters'].unique())
options.append('All Subtypes')

# HTML Structure
app.layout = html.Div(children=[
    html.H1(children='Breast Cancer Data Analysis'),
    
    html.H4(children='Select the subtype:'),
    dcc.Dropdown(options, value='All Subtypes', id='dcc_rppa_clusters'),
    html.H4(children=''),
    dcc.Graph(
        id='graph_rppa_clusters',
        figure=fig
    )
])

@callback(
    # Output: Graph
    Output('graph_rppa_clusters', 'figure'),
    # Input: Selected Subtype
    Input('dcc_rppa_clusters', 'value')
)
def update_output(value):
    
    #Shows the current chart to the selected item
    if value == "All Subtypes":
        fig = px.bar(df, x="Vital Status", y="OS Time", color="RPPA Clusters", barmode="group")
        fig.update_layout(
            title="Vital Status x OS Time of each pacient by subtype",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
                )
            )
    else:
        fig = px.bar(df[df["RPPA Clusters"]==value], x="Vital Status", y="OS Time", color="RPPA Clusters", barmode="group")
        fig.update_layout(
            title="Vital Status x OS Time of each pacient by subtype",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
                )
            )
    return fig

if __name__ == '__main__':
    app.run(debug=True)

    



