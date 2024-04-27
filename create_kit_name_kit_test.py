import sender_stand_request
import data


def positive_assert_code_201(kit_body, response):
    # Verificar que la solicitud se realizó con éxito (código 201)
    assert response.status_code == 201
    # Verificar que el campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body, response):
    # Verificar que la solicitud no se realizó con éxito (código 400)
    assert response.status_code == 400
    # Verificar que el campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
    assert response.json()["name"] == kit_body["name"]




# Prueba 1: Crear un kit con el 1 carácter en el nombre
def test_create_kit_with_one_character_name():
    # Obtener el cuerpo de la solicitud con un nombre de kit de un solo carácter
    kit_body = data.get_kit_body(data.one_letter)
    # Obtener el token de autenticación
    auth_token = sender_stand_request.get_new_user_token()
    # Enviar la solicitud para crear un nuevo kit
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Verificar que la solicitud se realizó con éxito
    positive_assert_code_201(kit_body, response)

# Prueba 2: Crear una solicitud con un nombre de kit largo (511 caracteres)
def test_create_kit_with_long_character_name():
    kit_body = data.get_kit_body(data.with_long_character_name)
    # Obtener el token de autenticación
    auth_token = sender_stand_request.get_new_user_token()
    # Enviar la solicitud para crear un nuevo kit
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Verificar que la solicitud se realizó con éxito
    positive_assert_code_201(kit_body, response)

# Prueba 3: Crear una solicitud con el nombre vacío da error
def test_create_kit_with_empty_name_get_error_response():
    kit_body = data.get_kit_body(data.empty_name)
    # Obtener el token de autenticación
    auth_token = sender_stand_request.get_new_user_token()
    # Enviar una solicitud para crear un nuevo kit
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Verificar que la solicitud no se realizó con éxito (código 400)
    negative_assert_code_400(kit_body, response)

# Prueba 4: Crear un kit con un nombre con un número de caracteres mayor a la cantidad permitida (512) da error
def test_create_kit_with_more_characters_than_allowed():
    kit_body = data.get_kit_body(data.more_characters_than_allowed)
    # Obtener el token de autenticación
    auth_token = sender_stand_request.get_new_user_token()
    # Enviar una solicitud para crear un nuevo kit
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Verificar que la solicitud no se realizó con éxito (código 400)
    negative_assert_code_400(kit_body, response)

# Prueba 5: Crear un kit con caracteres especiales en el nombre
def test_create_kit_with_special_characters():
    kit_body = data.get_kit_body(data.special_characters)
    # Obtener el token de autenticación
    auth_token = sender_stand_request.get_new_user_token()
    # Enviar la solicitud para crear un nuevo kit
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Verificar que la solicitud se realizó con éxito
    positive_assert_code_201(kit_body, response)

# Prueba 6: Crear un kit con espacios en el nombre
def test_create_kit_with_spaces():
    kit_body = data.get_kit_body(data.with_spaces)
    # Obtener el token de autenticación
    auth_token = sender_stand_request.get_new_user_token()
    # Enviar la solicitud para crear un nuevo kit
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Verificar que la solicitud se realizó con éxito
    positive_assert_code_201(kit_body, response)

# Prueba 7: Crear kit con números en el nombre
def test_create_kit_with_numbers():
    kit_body = data.get_kit_body(data.with_numbers)
    # Obtener el token de autenticación
    auth_token = sender_stand_request.get_new_user_token()
    # Enviar la solicitud para crear un nuevo kit
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Verificar que la solicitud se realizó con éxito
    positive_assert_code_201(kit_body, response)

# Prueba 8: Crear un kit sin parámetros da error
def test_create_kit_no_parameters():
    kit_body = data.get_kit_body(data.no_parameters)
    # Obtener el token de autenticación
    auth_token = sender_stand_request.get_new_user_token()
    # Enviar una solicitud para crear un nuevo kit
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Verificar que la solicitud no se realizó con éxito (código 400)
    negative_assert_code_400(kit_body, response)

# Prueba 9: Crear un kit con un valor numérico como nombre da error
def test_create_kit_with_number_parameter():
    kit_body = data.get_kit_body(data.number_parameter)
    # Obtener el token de autenticación
    auth_token = sender_stand_request.get_new_user_token()
    # Enviar una solicitud para crear un nuevo kit
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Verificar que la solicitud no se realizó con éxito (código 400)
    negative_assert_code_400(kit_body, response)
