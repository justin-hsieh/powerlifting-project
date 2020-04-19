import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            # Process
            """
        ),
        
        dcc.Markdown(
            """
            #### About the Data
            
            The dataset I used consists of information about individual lifters, such as name, age, weight, equipment used, weight lifted for specific lifts, competition info/locations, placing in competition, and scoring metrics (McCulloch, Glossbrenner, IPFPoints). There are 1,423,354 entries with 37 features in the dataset I used, which can be found [here](https://www.kaggle.com/open-powerlifting/powerlifting-database#openpowerlifting.csv).
            """,
            style = dict(marginTop= '50px')
        ),
        dcc.Markdown(
            """
            #### Getting Started
            
            The dataset was loaded into a Jupyter notebook as a dataframe. Here's a snippet of what the first few rows/columns looked like initially:
            
            """,
            style = dict(marginTop= '50px')
        ),
        
        html.Img(src='assets/head1.jpg',className='rounded mx-auto d-block', style={'height':'3%', 'marginTop':'30px'}),
        
        dcc.Markdown(
            """
            Before doing any wrangling, I wanted to take a look at how many values were missing in each column. Doing this can help give an idea of which imputation techniques to use, or if the column(s) should be removed completely. 
            
            """,
            style = dict(marginTop= '50px'),
        ),
        html.Img(src='assets/na.jpg',className='rounded mx-auto d-block', style={'height':'4%', 'marginTop':'30px'}),
        
        dcc.Markdown(
            """
            The columns 'Squat4Kg', 'Bench4Kg', and 'Deadlift4Kg' are missing too many values to be of any use, so they were removed from the dataframe.
            
            """,
            style = dict(marginTop= '10px'),
        ),
        
        dcc.Markdown(
            """
            #### Exploratory Data Analysis (EDA)
            
            Exploring a few variables accompanied by visualizations. 
            
            """,
            style = dict(marginTop= '50px')
        ),
        dcc.Markdown(
            """
            ##### Gender
            """,
            style = dict(marginTop= '30px')
        ),
    
        html.Img(src='assets/gender.jpg',className='rounded mx-auto d-block', style={'height':'5%', 'marginTop':'30px'}),
        
        dcc.Markdown(
            """
            ##### Equipment Used
            
            """,
            style = dict(marginTop= '50px')
        ),
        html.Img(src='assets/eq1.jpg',className='rounded mx-auto d-block', style={'height':'2%', 'marginTop':'30px'}),
        html.Img(src='assets/eq2.jpg',className='rounded mx-auto d-block', style={'height':'5%', 'marginTop':'40px'}),
        
        dcc.Markdown(
            """
            ##### Age
            
            """,
            style = dict(marginTop= '50px')
        ),
        
        html.Img(src='assets/age1.jpg',className='rounded mx-auto d-block', style={'height':'5%', 'marginTop':'30px'}),
        
        dcc.Markdown(
            """
            ##### Bodyweight and Total Weight Lifted by Equipment Used
            
            """,
            style = dict(marginTop= '50px')
        ),
        html.Img(src='assets/bte.jpg',className='rounded mx-auto d-block', style={'height':'6%', 'marginTop':'30px'}),
        
        dcc.Markdown(
            """
            #### Data Wrangling and Modeling
            
            There were many directions I could have taken with this dataset. I could have used it to predict how lifters would place in competitions, or determine which competition is the most competitive. For the purposes of this app, I wanted to predict something that would apply to a broader powerlifting audience: the total number of kilograms lifted. This number represents the combined total of the best three lifts in each category. The picture below demonstrates me dropping the NAN/missing values from this column, which will now become the target column.
            """,
            style = dict(marginTop= '50px')
        ),
        
        html.Img(src='assets/df2.jpg',className='rounded mx-auto d-block', style={'height':'2%', 'marginTop':'30px'}),
        
        dcc.Markdown(
            """
            The next step was to split the dataset into two subsets: 80% train, 20% val. The train set will be used to train the prediction model. That prediction model will be used to make predictions and compare them to the val set to see how the model performs, also known as cross-validation. 
            
            """,
            style = dict(marginTop= '50px'),
        ),
        
        html.Img(src='assets/split.jpg',className='rounded mx-auto d-block', style={'height':'3%', 'marginTop':'30px'}),
        
        dcc.Markdown(
            """
            I created a transformer pipeline for the train data with Ordinal Encoder and Simple Imputer strategies to help with filling in missing data. Using a pipeline makes the fit/transform/predict process easier without having to perform those actions individually, which can be time/space consuming. 
            
            """,
            style = dict(marginTop= '50px'),
        ),
        html.Img(src='assets/pipeline.jpg',className='rounded mx-auto d-block', style={'height':'2%', 'marginTop':'30px'}),
        
        dcc.Markdown(
            """
            The next step was to instantiate a model using the random forest regressor, and then fit the model with the transformed values from the previous step. 
            """,
            style = dict(marginTop= '50px'),
        ),
        html.Img(src='assets/randregressor.jpg',className='rounded mx-auto d-block', style={'height':'2%', 'marginTop':'30px'}),
        
        dcc.Markdown(
            """
            Using the model, I made a set of predictions and compared them to the val set. The scoring metric used was mean absolute error. 
            """,
            style = dict(marginTop= '50px'),
        ),
        
        html.Img(src='assets/mae.jpg',className='rounded mx-auto d-block', style={'height':'2%', 'marginTop':'30px'}),
        
        dcc.Markdown(
            """
            To get a glance at how much weight each feature carries in the prediction, I used permutation importance from the eli5 library. This method can also help with feature selection by visualizing which features should have a closer look. 
            """,
            style = dict(marginTop= '50px'),
        ),
        html.Img(src='assets/perm.jpg',className='rounded mx-auto d-block', style={'height':'7%', 'marginTop':'30px'}),
        dcc.Markdown(
            """
            Tuning the model itself can also yield a better prediction. RandomizedSearchCV finds the optimal model hyperparameters to use by using randomized samples from specified distributions. 
            """,
            style = dict(marginTop= '50px'),
        ),
    
        html.Img(src='assets/randomcv.jpg',className='rounded mx-auto d-block', style={'height':'5%', 'marginTop':'30px'}),
        dcc.Markdown(
            """
            In addition to the Random Forest Regressor, I also tuned an XGBoost Regressor model with RandomizedSearchCV to compare with.
            """,
            style = dict(marginTop= '50px'),
        ),
        html.Img(src='assets/randomcv1.jpg',className='rounded mx-auto d-block', style={'height':'5%', 'marginTop':'30px'}),
        
        dcc.Markdown(
            """
            The model's result yielded a higher mean absolute error than the one for Random Forest. Therefore, I decided my prediction model will be the Random Forest Regressor.
            """,
            style = dict(marginTop= '50px'),
        ),
        html.Img(src='assets/xgbmae.jpg',className='rounded mx-auto d-block', style={'height':'1%', 'marginTop':'30px'}),
        
        
    ],
)

layout = dbc.Row([column1])