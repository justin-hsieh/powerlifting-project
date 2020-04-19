import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

from joblib import load
import pandas as pd


model = load('assets/model.joblib')


@app.callback(
    Output('prediction-content', 'children'),
    [Input('Sex', 'value'), 
     Input('Age', 'value'), 
     Input('Bodyweight', 'value'), 
     Input('Equipment', 'value')]
)


def predict(Sex, Age, Bodyweight, Equipment):
    df = pd.DataFrame(
        data=[[Sex,Equipment,Age,Bodyweight]],
        
            columns=['Sex','Equipment','Age','Bodyweight']
                    )
    
    pred = model.predict(df)[0]
    
    result = [html.Div(f'Total of Squat, Bench Press, and Deadlift (in kg): \n\n',
                       style={'margin-left':'365px','margin-bottom':'30px', 'fontSize': '20px'})
             ]
    
    result += [html.Div(f'{pred:,.0f}\n\n',
                       style={'margin-left':'545px','margin-bottom':'50px', 'fontSize': '30px'})
              ]
    
    result += [html.Div(f'Total of Squat, Bench Press, and Deadlift (in lbs): \n\n',
                       style={'margin-left':'365px','margin-bottom':'30px', 'fontSize': '20px'})
             ]
    
    result += [html.Div(f'{pred*2.2:,.0f}\n\n',
                       style={'margin-left':'545px','margin-bottom':'50px', 'fontSize': '30px'})
              ]
    return result


column1 = dbc.Col(
    [
        dcc.Markdown('# Predict', className='mb-1', style={'margin-left':'500px'}),
        #dcc.Markdown('###### See how much you would lift in competition.',
        #             className='mb-5', style={'margin-left':'400px'}
        #            ),
        dcc.Markdown('#### Sex', style={'margin-left':'550px', 'margin-top': '40px'}),
        dcc.RadioItems(
            id='Sex',
            options=[
                {'label': 'Female', 'value': '1'},
                {'label': 'Male', 'value': '0'}
                    ],
            value='1',
            labelStyle={'display': 'inline-block'},
            className='mb-4',
            inputStyle={'margin-left':'10px'},
            style={'margin-left':'500px'}
            
        ),
        
        dcc.Markdown('#### Age',style={'margin-left':'550px'}),
        dcc.Input(
            id='Age',
            placeholder='Enter your age...',
            type='number',
            value='',
            className='mb-4',
            style={'margin-left':'480px'}
        ),
        
        dcc.Markdown('#### Bodyweight (kg)',style={'margin-left':'480px', 'margin-top': '20px'}),
        dcc.Slider(
                id='Bodyweight',
                min=20,
                max=240,
                step=1,
                marks={i: '{}'.format(i) for i in range(20,241,20)},
                value=100,
                className='mb-4',
              
        ),
        dcc.Markdown('###### *1 kg = 2.20 lb,  1 lb = 0.45 kg*',
                     className='mb-4',
        ),
        
        dcc.Markdown('#### Equipment',style={'margin-left':'515px'}),
        dcc.Dropdown(
            id='Equipment',
            options=[
                {'label': 'Wraps', 'value': '2'},
                {'label': 'Raw', 'value': '0'},
                {'label': 'Single-ply', 'value': '1'}
                    ],
            value='',
            className='mb-1',
            style={'width':'200px', 'margin-left': '238px', 'margin-bottom': '50px'},
            placeholder='Select One'
        ),  
     
        
       #html.H2('You are predicted to place: ', className='mb-5'),
       html.Div(id='prediction-content',className='mt-4', style={'marginTop': '10px'})
       
    ],
    md=12,
)


layout = dbc.Row([column1])