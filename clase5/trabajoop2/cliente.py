import requests

url = 'https://verbose-system-97jqjjvxgwfpxvg-8000.app.github.dev/'

# ejemplo request en GET
r = requests.get(url)
print(r.text)

# ejemplo request en POST
r = requests.post(url + 'encolar', json={'nombre': 'Juan', 'productos': ['manzana', 'pera']})
print(r.text)