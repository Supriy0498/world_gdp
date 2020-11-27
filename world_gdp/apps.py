from django.apps import AppConfig
import pickle
import pandas as pd

class WorldGdpConfig(AppConfig):
    name = 'world_gdp'
    randomForest = pickle.load(open('D:\\django venv\\countries_world\\world_gdp\\model\\finalized_model.sav', 'rb'))
