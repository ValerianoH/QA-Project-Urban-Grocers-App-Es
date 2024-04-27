import requests
import configuration
import data

# Crear nuevo kit
def post_new_client_kit(kit_body, auth_token):
    # Se realiza una copia del cuerpo de la solicitud para evitar cambios en el diccionario original
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    # Se envía la solicitud POST para crear un nuevo kit de producto
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)

# Crear un nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


# Obtener un nuevo token
def get_new_user_token():
    user_response = post_new_user(data.user_body)
    return user_response.json()["authToken"]
