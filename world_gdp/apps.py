from django.apps import AppConfig
import pickle
import pandas as pd

class WorldGdpConfig(AppConfig):
    name = 'world_gdp'
    randomForest = pickle.load(open('/home/worldgdp/world_gdp/world_gdp/model/finalized_model.sav', 'rb'))
