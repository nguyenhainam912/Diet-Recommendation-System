import requests
import json
import model
import pandas as pd

class Generator:
    def __init__(self,nutrition_input:list,ingredients:list=[],params:dict={'n_neighbors':5,'return_distance':False}):
        self.nutrition_input=nutrition_input
        self.ingredients=ingredients
        self.params=params

    def set_request(self,nutrition_input:list,ingredients:list,params:dict):
        self.nutrition_input=nutrition_input
        self.ingredients=ingredients
        self.params=params

    def generate(self,):
        dataset=pd.read_csv('../input/dataset.csv')
        request={
            'nutrition_input':self.nutrition_input,
            'ingredients':self.ingredients,
            'params':self.params
        }
    
        data=json.dumps(request)
        parsed_data = json.loads(data)
        recommendation_dataframe=model.recommend(dataset,parsed_data['nutrition_input'],parsed_data['ingredients'],parsed_data['params'])
        output=model.output_recommended_recipes(recommendation_dataframe)
        if output is None:
            return {"output":None}
        else:
            return {"output":output}