import requests
import configuration
import data


def post_new_client_kit(kit_body, auth_token):
    # Se realiza una copia del cuerpo de la solicitud para evitar cambios en el diccionario original
    body = kit_body.copy()

    # Se agrega el encabezado de autorización al cuerpo de la solicitud
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }

    # Se envía la solicitud POST para crear un nuevo kit de producto
    response = requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=body,
        headers=headers
    )

    # Se retorna la respuesta de la solicitud
    return response

# Crear un nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_new_client_kit(kit_body, auth_token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)


def get_new_user_token():
    user_response = post_new_user(data.user_body)
    return user_response.json()["authToken"]
