"""
Global Education Statistics Dashboard
Data Visualization Final Project - Plotly Dash Application
"""

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load the cleaned dataset
df = pd.read_csv(os.path.join(script_dir, 'cleaned_education_data.csv'))

# Create continent grouping
def get_continent(region):
    region_lower = str(region).lower()
    if any(x in region_lower for x in ['north america', 'latin america', 'south america']):
        return 'Americas'
    elif any(x in region_lower for x in ['western europe', 'eastern europe']):
        return 'Europe'
    elif any(x in region_lower for x in ['asia', 'east asia', 'southern asia', 'south-eastern asia']):
        return 'Asia'
    elif any(x in region_lower for x in ['africa', 'sub-saharan']):
        return 'Africa'
    elif any(x in region_lower for x in ['middle east', 'arab']):
        return 'Middle East'
    elif any(x in region_lower for x in ['oceania', 'pacific']):
        return 'Oceania'
    else:
        return 'Other'

df['Continent'] = df['Region'].apply(get_continent)

# Initialize the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

# Define available options
countries = sorted(df['Country'].unique())
regions = sorted(df['Region'].unique())
years = sorted(df['Year'].unique())

# App Layout
app.layout = html.Div([
    html.Header([
        html.H1("Global Education Statistics Dashboard", 
                style={'textAlign': 'center', 'color': '#2c3e50'}),
        html.P("Data Visualization Final Project",
               style={'textAlign': 'center', 'color': '#7f8c8d'})
    ], style={'backgroundColor': '#ecf0f1', 'padding': '20px', 'marginBottom': '20px'}),
    
    html.Div([
        html.H3("Interactive Filters"),
        html.Div([
            html.Div([
                html.Label("Select Region:"),
                dcc.Dropdown(id='region-dropdown',
                    options=[{'label': r, 'value': r} for r in ['All'] + regions],
                    value='All')
            ], style={'width': '30%', 'display': 'inline-block'}),
            html.Div([
                html.Label("Select Year:"),
                dcc.Dropdown(id='year-dropdown',
                    options=[{'label': str(y), 'value': y} for y in ['All'] + years],
                    value='All')
            ], style={'width': '30%', 'display': 'inline-block'}),
            html.Div([
                html.Label("Select Countries:"),
                dcc.Dropdown(id='country-dropdown',
                    options=[{'label': c, 'value': c} for c in countries],
                    value=None, multi=True)
            ], style={'width': '30%', 'display': 'inline-block'})
        ]),
        html.Div([
            html.Div([
                html.Label("Literacy Rate Threshold:"),
                dcc.Slider(id='literacy-slider', min=0, max=100, step=5, value=50,
                    marks={i: str(i) for i in range(0, 101, 10)})
            ], style={'width': '48%', 'display': 'inline-block'}),
            html.Div([
                html.Label("Chart Type:"),
                dcc.RadioItems(id='chart-type-radio',
                    options=[{'label': ' Bar', 'value': 'bar'},
                             {'label': ' Column', 'value': 'column'}],
                    value='column', inline=True)
            ], style={'width': '48%', 'display': 'inline-block'})
        ])
    ], style={'backgroundColor': '#f9f9f9', 'padding': '20px', 'marginBottom': '20px'}),
    
    html.Div([
        html.Div([html.H4("Literacy Rate (Column Chart)"), dcc.Graph(id='literacy-bar-chart')],
                 style={'width': '48%', 'display': 'inline-block'}),
        html.Div([html.H4("GDP by Region (Bar Chart)"), dcc.Graph(id='gdp-bar-chart')],
                 style={'width': '48%', 'display': 'inline-block'})
    ]),
    html.Div([
        html.Div([html.H4("Enrollment Rates (Stacked Column)"), dcc.Graph(id='enrollment-stacked-column-chart')],
                 style={'width': '48%', 'display': 'inline-block'}),
        html.Div([html.H4("Enrollment Rates (Stacked Bar)"), dcc.Graph(id='enrollment-stacked-bar-chart')],
                 style={'width': '48%', 'display': 'inline-block'})
    ]),
    html.Div([
        html.Div([html.H4("Gender Literacy (Clustered Column)"), dcc.Graph(id='literacy-clustered-column-chart')],
                 style={'width': '48%', 'display': 'inline-block'}),
        html.Div([html.H4("Gender Literacy (Clustered Bar)"), dcc.Graph(id='literacy-clustered-bar-chart')],
                 style={'width': '48%', 'display': 'inline-block'})
    ]),
    html.Div([
        html.Div([html.H4("GDP vs Literacy (Scatter)"), dcc.Graph(id='scatter-gdp-literacy')],
                 style={'width': '48%', 'display': 'inline-block'}),
        html.Div([html.H4("Spending vs Enrollment (Bubble)"), dcc.Graph(id='bubble-chart')],
                 style={'width': '48%', 'display': 'inline-block'})
    ]),
    html.Div([
        html.Div([html.H4("Literacy Distribution (Histogram)"), dcc.Graph(id='histogram-literacy')],
                 style={'width': '48%', 'display': 'inline-block'}),
        html.Div([html.H4("GDP by Continent (Box)"), dcc.Graph(id='box-gdp-chart')],
                 style={'width': '48%', 'display': 'inline-block'})
    ]),
    html.Div([html.H4("Student-Teacher Ratio (Violin)"), dcc.Graph(id='violin-chart')]),
    html.Div([
        html.Div([html.H4("Literacy Trend (Line)"), dcc.Graph(id='line-literacy-trend')],
                 style={'width': '48%', 'display': 'inline-block'}),
        html.Div([html.H4("Spending Over Time (Area)"), dcc.Graph(id='area-spending-chart')],
                 style={'width': '48%', 'display': 'inline-block'})
    ]),
    html.Footer(html.P("2024 Data Visualization Project", style={'textAlign': 'center'}))
], style={'fontFamily': 'Arial', 'padding': '20px'})

@app.callback(
    [Output('literacy-bar-chart', 'figure'), Output('gdp-bar-chart', 'figure'),
     Output('enrollment-stacked-column-chart', 'figure'), Output('enrollment-stacked-bar-chart', 'figure'),
     Output('literacy-clustered-column-chart', 'figure'), Output('literacy-clustered-bar-chart', 'figure'),
     Output('scatter-gdp-literacy', 'figure'), Output('bubble-chart', 'figure'),
     Output('histogram-literacy', 'figure'), Output('box-gdp-chart', 'figure'),
     Output('violin-chart', 'figure'), Output('line-literacy-trend', 'figure'),
     Output('area-spending-chart', 'figure')],
    [Input('region-dropdown', 'value'), Input('year-dropdown', 'value'),
     Input('country-dropdown', 'value'), Input('literacy-slider', 'value'),
     Input('chart-type-radio', 'value')]
)
def update_charts(region, year, countries, threshold, chart_type):
    fdf = df.copy()
    if region != 'All': fdf = fdf[fdf['Region'] == region]
    if year != 'All': fdf = fdf[fdf['Year'] == year]
    if countries: fdf = fdf[fdf['Country'].isin(countries)]
    fdf = fdf[fdf['Literacy rate'] >= threshold]
    
    cdf = fdf[fdf['Year'] == fdf['Year'].max()] if year == 'All' else fdf
    if len(cdf) > 15: cdf = cdf.nlargest(15, 'Literacy rate')
    
    # Week 1: Column Chart (Vertical Bar)
    if chart_type == 'column':
        fig1 = px.bar(cdf, x='Country', y='Literacy rate', color='Literacy rate',
                      title=f"Literacy Rate - {year}", height=400,
                      labels={'Country': 'Country', 'Literacy rate': 'Literacy Rate (%)'})
    else:
        fig1 = px.bar(cdf, y='Country', x='Literacy rate', color='Literacy rate',
                      orientation='h', title=f"Literacy Rate - {year}", height=400,
                      labels={'Country': 'Country', 'Literacy rate': 'Literacy Rate (%)'})
    
    # Week 1: Bar Chart by Region (Horizontal)
    gdp_reg = fdf.groupby('Region')['GDP per capita'].mean().reset_index().sort_values('GDP per capita')
    fig2 = px.bar(gdp_reg, x='GDP per capita', y='Region', orientation='h',
                  color='GDP per capita', title="Avg GDP by Region", height=400,
                  labels={'GDP per capita': 'GDP per Capita (USD)', 'Region': 'Region'})
    
    # Week 2: Stacked Column Chart (Vertical)
    enf = cdf[['Country','Enrollment rate primary','Enrollment rate secondary','Enrollment rate tertiary']].head(10)
    fig3 = go.Figure()
    for col, name, clr in [('Enrollment rate primary','Primary','#3498db'),
                           ('Enrollment rate secondary','Secondary','#2ecc71'),
                           ('Enrollment rate tertiary','Tertiary','#e74c3c')]:
        fig3.add_trace(go.Bar(x=enf['Country'], y=enf[col], name=name, marker_color=clr))
    fig3.update_layout(title="Enrollment Rates (Stacked Column)", barmode='stack', height=400,
                       xaxis_title='Country', yaxis_title='Enrollment Rate (%)')
    
    # Week 2: Stacked Bar Chart (Horizontal)
    fig4 = go.Figure()
    for col, name, clr in [('Enrollment rate primary','Primary','#3498db'),
                           ('Enrollment rate secondary','Secondary','#2ecc71'),
                           ('Enrollment rate tertiary','Tertiary','#e74c3c')]:
        fig4.add_trace(go.Bar(y=enf['Country'], x=enf[col], name=name, marker_color=clr, orientation='h'))
    fig4.update_layout(title="Enrollment Rates (Stacked Bar)", barmode='stack', height=400,
                       yaxis_title='Country', xaxis_title='Enrollment Rate (%)')
    
    # Week 2: Clustered Column Chart (Vertical)
    lgf = cdf[['Country','Male literacy rate','Female literacy rate']].head(10)
    fig5 = go.Figure()
    fig5.add_trace(go.Bar(x=lgf['Country'], y=lgf['Male literacy rate'], name='Male'))
    fig5.add_trace(go.Bar(x=lgf['Country'], y=lgf['Female literacy rate'], name='Female'))
    fig5.update_layout(title="Gender Literacy (Clustered Column)", barmode='group', height=400,
                       xaxis_title='Country', yaxis_title='Literacy Rate (%)')
    
    # Week 2: Clustered Bar Chart (Horizontal)
    fig6 = go.Figure()
    fig6.add_trace(go.Bar(y=lgf['Country'], x=lgf['Male literacy rate'], name='Male', orientation='h'))
    fig6.add_trace(go.Bar(y=lgf['Country'], x=lgf['Female literacy rate'], name='Female', orientation='h'))
    fig6.update_layout(title="Gender Literacy (Clustered Bar)", barmode='group', height=400,
                       yaxis_title='Country', xaxis_title='Literacy Rate (%)')
    
    # Week 3: Scatter Chart (no size parameter - pure scatter)
    fig7 = px.scatter(fdf, x='GDP per capita', y='Literacy rate', color='Continent',
                      hover_data=['Country'], title="GDP vs Literacy", height=400,
                      labels={'GDP per capita': 'GDP per Capita (USD)', 'Literacy rate': 'Literacy Rate (%)'})
    
    # Week 4: Bubble Chart (with size parameter for bubble effect)
    fig8 = px.scatter(fdf, x='Government spending on education (% of GDP)', y='Enrollment rate primary',
                      size='Enrollment rate secondary', color='Region', 
                      title="Spending vs Enrollment (Bubble)", height=400,
                      labels={'Government spending on education (% of GDP)': 'Govt Spending (% of GDP)', 
                              'Enrollment rate primary': 'Primary Enrollment Rate (%)'})
    
    # Week 5: Histogram
    fig9 = px.histogram(fdf, x='Literacy rate', color='Continent', nbins=20,
                        title="Literacy Distribution", height=400,
                        labels={'Literacy rate': 'Literacy Rate (%)', 'count': 'Number of Countries'})
    
    # Week 6: Box Chart
    fig10 = px.box(fdf, x='Continent', y='GDP per capita', color='Continent',
                   title="GDP Distribution by Continent", height=400,
                   labels={'Continent': 'Continent', 'GDP per capita': 'GDP per Capita (USD)'})
    
    # Week 7: Violin Chart
    fig11 = px.violin(fdf, x='Continent', y='Student-teacher ratio', color='Continent',
                      box=True, points='all', title="Student-Teacher Ratio Distribution", height=400,
                      labels={'Continent': 'Continent', 'Student-teacher ratio': 'Student-Teacher Ratio'})
    
    # Week 8: Line Chart
    ldf = df.groupby(['Year','Continent'])['Literacy rate'].mean().reset_index()
    fig12 = px.line(ldf, x='Year', y='Literacy rate', color='Continent', markers=True,
                    title="Literacy Trend Over Time", height=400,
                    labels={'Year': 'Year', 'Literacy rate': 'Literacy Rate (%)'})
    
    # Week 9: Area Chart
    adf = df.groupby(['Year','Continent'])['Government spending on education (% of GDP)'].mean().reset_index()
    fig13 = px.area(adf, x='Year', y='Government spending on education (% of GDP)', color='Continent',
                    title="Education Spending Over Time", height=400,
                    labels={'Year': 'Year', 'Government spending on education (% of GDP)': 'Spending (% of GDP)'})
    
    return fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10, fig11, fig12, fig13

if __name__ == '__main__':
    print("Starting dashboard at http://127.0.0.1:8050/")
    app.run(debug=True, host='0.0.0.0', port=8050)
