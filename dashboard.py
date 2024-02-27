#Created by Beatriz Albuquerque.
# Run this app with `python app.py`

# database: https://www.nature.com/articles/nature18003


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
    html.H1(children='Dashboard: Breast Cancer Data analysis'),
     
    dcc.Dropdown(options, value='All Subtypes', id='dcc_rppa_clusters'),
    
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
    else:
        fig = px.bar(df[df["RPPA Clusters"]==value], x="Vital Status", y="OS Time", color="RPPA Clusters", barmode="group")
    return fig

if __name__ == '__main__':
    app.run(debug=True)

    



