import plotly.express as px
from plotly.offline import plot

def barplotGene(geneID):

    data_canada = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(data_canada, x='year', y='pop')

    div_obj = plot(fig, show_link=False, auto_open=False, include_plotlyjs=True, output_type = 'div')
    return div_obj