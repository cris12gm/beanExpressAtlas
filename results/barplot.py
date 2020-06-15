import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import plot

def barplotGene(expressionMatrix,samples):

    samples = ["VM","IM","FB5"]
    xValues = []
    yValues = []
    for sample in samples:
        xValues.append(sample)
        yValues.append(getattr(expressionMatrix,sample))

    fig = go.Figure(data=[
        go.Bar(x=xValues, y=yValues, marker_color='rgb(25, 74, 144)')])


    div_obj = plot(fig, show_link=False, auto_open=False, include_plotlyjs=True, output_type = 'div')
    return div_obj