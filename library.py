import datetime
import jwt


def create_token(payload_dictionary: dict, token_password: str):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
        'iat': datetime.datetime.utcnow(),
    }
    payload.update(payload_dictionary)
    encode_jdw = jwt.encode(
        payload=payload,
        key=token_password,
        algorithm='HS256', )
    return encode_jdw


def decode_token(token_jwt: str, token_password: str):
    decoded = jwt.decode(
        token_jwt,
        token_password,
        algorithms='HS256', )
    return decoded


dictionary_with_information = {
    'name': 'Yaroslav',
    'surname': 'Shymanovskyi',
    'age': 14,
}
token_password = 'Password1234'
token_jwt = create_token(dictionary_with_information, token_password)
decode_token(token_jwt, token_password)
