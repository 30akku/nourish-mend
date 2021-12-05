import requests
import json

def get_dish(diet):
    url = 'https://api.edamam.com/api/recipes/v2?type=public&q=recipes&app_id=f521ef6d&app_key=8119142429b59a19afb28f098f448a52&mealType=Breakfast&mealType=Dinner&mealType=Lunch' 
    params = {'diet': diet}
    r = requests.get(url, params=params)
    dishes = r.json()
    json_data = json.loads(r.text)
    #dish_list = {'dishes':dishes['hits']}
    #dish_list = dishes['hits.recipe']
    #for element in json_data['hits']:
        #print(element['recipe'])
    
    for i in json_data['hits']:
        print(i['recipe']['label'])
    return "aka"