import urllib
import urllib2
import json,xmltodict
from pymongo import MongoClient
dishName = 'biryani';
cuisineName = 'Indian';
recipeId = '00000000'
response = urllib2.urlopen('http://api.bigoven.com/recipes?title_kw='+urllib.quote(dishName)+
                           '&api_key=&pg=1&rpp=50').read()
response = xmltodict.parse(response)
response = json.dumps(response)
response = json.loads(response)
if response[u'RecipeSearchResult'][u'Results'] is not None:
    for recipeInfo in response[u'RecipeSearchResult'][u'Results'][u'RecipeInfo']:
        if recipeInfo.has_key(u'Cuisine'):
                if recipeInfo[u'Cuisine'] is not None:
                    if recipeInfo[u'Cuisine'].lower() == cuisineName.lower():
                        if recipeInfo.has_key(u'Title'):
                            if recipeInfo[u'Title'] is not None:
                                if recipeInfo[u'Title'].lower() == dishName.lower():
                                    recipeId = recipeInfo[u'RecipeID']
                                    break
    print "RECIPEID="+recipeId
    recipeResponse = urllib2.urlopen('http://api.bigoven.com/recipe/'+recipeId+
                                     '?api_key=').read()
    recipeResponse = xmltodict.parse(recipeResponse)
    recipeResponse = json.dumps(recipeResponse)
    recipeResponse = json.loads(recipeResponse)
    if recipeResponse.has_key(u'Recipe') and recipeResponse[u'Recipe'] is not None and \
                    recipeResponse[u'Recipe'][u'Ingredients'] is not None :
        if recipeResponse[u'Recipe'][u'Ingredients'][u'Ingredient'] is not None:
           JSONObj = { "cuisineName ": cuisineName, "dishName":dishName ,
                       "ingredients":recipeResponse[u'Recipe'][u'Ingredients'][u'Ingredient'] }
           client = MongoClient('localhost', 27017)
           db = client['twitter_db']
           collection = db['twitter_collection']
           collection.insert(JSONObj)
           print 'Ingredients for '+dishName+' are below:'
           for ingredient in recipeResponse[u'Recipe'][u'Ingredients'][u'Ingredient']:
                print ingredient[u'Name']

