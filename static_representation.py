catalogo = {} #Usando un diccionario para una librería

def add_book(titulo, autor, genero, isbn):
    catalogo[isbn] = {"titulo": titulo, "autor": autor, "genero": genero}
    return catalogo

def search_book(query):
  results = []
  for isbn, book_data in catalogo.items():
    if query in book_data['titulo'] or query in book_data['autor'] or query == isbn:
      results.append(book_data)
  return results

def display_catalog():
     for isbn, book_data in catalogo.items():
      print(f"ISBN: {isbn}, Titulo: {book_data['titulo']}, Autor: {book_data['autor']}, Genero: {book_data['genero']}")

#ejemplo

add_book("El señor de los Anillos", "J.R.R. Tolkien", "Fantasia", "9780547928227")
add_book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science Fiction", "9780345391803")

print("Ingrese Autor, Titulo o ISBN a buscar: ")
a = input()
search_results = search_book(a)
print(f"El libro es:  {search_results}")
display_catalog()