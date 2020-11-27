from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import sklearn
from .apps import WorldGdpConfig

def home(req):
    #return HttpResponse(gdp)#.format(pred[0]))#req,'world_gdp/index.html')
    return render(req,'world_gdp/index.html')

def predict(req):
   return render(req,'world_gdp/predict.html')

def dashboard(req):
   return render(req,'world_gdp/dashboard.html')

def dataset(req):
   return render(req,'world_gdp/dataset.html')

def getGDP(req):
    country = req.POST.get('country')
    population = float(req.POST.get('population'))
    area = float(req.POST.get('area'))
    population_density = float(req.POST.get('population_density'))
    coast = float(req.POST.get('coast'))
    migration = float(req.POST.get('migration'))
    mortality = float(req.POST.get('mortality'))
    phones = float(req.POST.get('phones'))
    arable = float(req.POST.get('arable'))
    crop = float(req.POST.get('crop'))
    other = float(req.POST.get('other'))
    literacy = float(req.POST.get('literacy'))
    birthrate = float(req.POST.get('birthrate'))
    deathrate = float(req.POST.get('deathrate'))
    region_label = float(req.POST.get('region_label'))
    climate_label = float(req.POST.get('climate_label'))

    training_features = ['Population', 'Area (sq. mi.)',
       'Pop. Density (per sq. mi.)', 'Coastline (coast/area ratio)',
       'Net migration', 'Infant mortality (per 1000 births)',
       'Literacy (%)', 'Phones (per 1000)',
       'Arable (%)', 'Crops (%)', 'Other (%)', 'Birthrate',
       'Deathrate', 'Region_label',
       'Climate_label']
    df = pd.DataFrame(columns = training_features)
    df = df.append({'Population':population, 'Area (sq. mi.)':area,
       'Pop. Density (per sq. mi.)':population_density, 'Coastline (coast/area ratio)':coast,
       'Net migration':migration, 'Infant mortality (per 1000 births)':mortality,
       'Literacy (%)':literacy, 'Phones (per 1000)':phones,
       'Arable (%)':arable, 'Crops (%)':crop, 'Other (%)':other, 'Birthrate':birthrate,
       'Deathrate':deathrate, 'Region_label':region_label,
       'Climate_label':climate_label},ignore_index = True)
    model = WorldGdpConfig.randomForest
    pred = model.predict(df)
    gdp = 'gdp of '+ country + ' is '+str(round(pred[0],2))
    return HttpResponse(gdp)
