import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dbc.Row(
            [
                dcc.Markdown(
                    """
                        ## Predict How Much You Can Lift
                    """,
                    style = dict(marginTop= '30px', marginBottom='10px')
                    ),
                dcc.Markdown(
                """
            The sport of powerlifting consists of performing three different types of lifts: squat, bench press, and deadlift. Competitions are held worldwide to see who can maximize three attempts at maximal weight on each lift. Scoring is based on the sum of their best attempts for each lift. 

            This app was created to help predict the total weight of the three lifts one could achieve based on certain measures (sex, weight, age, equipment used). The prediction can be the basis to formulating a fitness plan for those who are interested in competing in powerlifting contests.

                """
                    )
            ]),
        
        dbc.Row(
            [
                dcc.Link(dbc.Button('Get Started', color='dark',style=dict(width='220px', marginBottom='40px', marginTop='10px')), href='/predictions', style=dict(margin='auto', width='220px'))
            ])
         
    ],
 
    md=6,
    align="center"
)


column2 = dbc.Col(
    [
        html.Img(src='assets/images243.png',className='rounded mx-auto d-block')
    ],
    md=6,
    align="center"
)
"""
gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)
"""
layout = dbc.Row([column1, column2])