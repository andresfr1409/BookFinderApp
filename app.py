import flask
import requests
import json

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        # Obtener la consulta de búsqueda ingresada por el usuario
        query = flask.request.form['query']
        
        # Realizar una solicitud a la API de Google Libros
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={query}')
        
        # Procesar la respuesta de la API y extraer los datos necesarios
        data = json.loads(response.text)
        books = []
        
        for item in data['items']:
            book = {
                'title': item['volumeInfo']['title'],
                'author': item['volumeInfo'].get('authors', ['N/A'])[0],
                'published_date': item['volumeInfo'].get('publishedDate', 'N/A'),
                'image_link': item['volumeInfo'].get('imageLinks', {}).get('thumbnail', ''),
                'external_link': item['volumeInfo'].get('infoLink', '#'),
                'description': item['volumeInfo'].get('description', 'N/A'),
                'page_count': item['volumeInfo'].get('pageCount', 'N/A')
            }
            books.append(book)
        
        # Renderizar la plantilla HTML y pasar los libros encontrados
        return flask.render_template('search.html', books=books)
    
    # Si el método de solicitud es GET, mostrar el formulario de búsqueda
    return flask.render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)