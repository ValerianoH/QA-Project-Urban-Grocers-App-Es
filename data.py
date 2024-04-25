# Encabezados para las solicitudes
headers = {
    "Content-Type": "application/json"
}

# Cuerpo de solicitud para crear un nuevo usuario
user_body = {
    "firstName": "Max",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop",
    "email": "usuario@example.com",
    "comment": "Comentario"
}

# Cuerpo de solicitud para crear un nuevo kit
kit_body = {
    "name": "Mi conjunto",
    "card": {
        "id": 1,
        "name": "para la situación"
    },
    "productsList": None,
    "id": 7,
    "productsCount": 0

}

# Función que cambia el contenido del cuerpo de solicitud al parámetro "name"
def get_kit_body(name):
    kit_body = {
        "name": name,
        "card": {
            "id": 1,
            "name": "Para la situación"
        },
        "productsList": None,
        "id": 7,
        "productsCount": 0
    }
    return kit_body
