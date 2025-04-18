import requests

def get_categories():
    request_var = requests.get("https://api.escuelajs.co/api/v1/categories")
    
    if request_var.status_code == 200:
        print("Andres eres un capo ya estas comunicandote con API")
        print(request_var.status_code)
        print(f'this is string type --> {request_var.text}')
        print(type(request_var.text))
        categories = request_var.json()
        print(f'This is JSON --> {categories}')
        
        for category in categories:
            print(category["name"])
    else:
        print("You have to check the code again")