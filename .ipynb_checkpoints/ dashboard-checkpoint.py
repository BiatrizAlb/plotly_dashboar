#Created by Beatriz Albuquerque.
# Run this app with `python app.py`

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("clinical_data_breast_cancer.csv")

fig = px.bar(df, x="Gender", y="Age at Initial Pathologic Diagnosis")

app.layout = html.Div(children=[
    html.H1(children='Dashboard: Breast cancer data analysis'),

    html.Div(children='''
        Dash: A web application framework for my data. '''),

    dcc.Graph(
        id='example',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
