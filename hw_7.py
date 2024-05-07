import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com/booking"
AUTH_URL = "https://restful-booker.herokuapp.com/auth"
PING_URL = "https://restful-booker.herokuapp.com/ping"
STATUS_OK = 200


@pytest.fixture(scope='function')
def get_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(AUTH_URL, json=payload)
    token = response.json()['token']
    yield token


@pytest.fixture(scope='function')
def get_new_booking_id():
    payload = {
        "firstname": "Olya",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "Breakfast"}

    response = requests.post(BASE_URL, json=payload)
    booking_id = response.json()['bookingid']
    yield booking_id


def test_get_all_bookings():
    response = requests.get(BASE_URL)
    assert response.status_code == STATUS_OK
    print(f'\n{len(response.json())}')
    print(response.headers)
    assert 'Connection' in response.headers, 'There is no expected key'


def test_get_bookins_with_id():
    response = requests.get(f'{BASE_URL}/2')
    response_data = response.json()
    expected_keys = ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates']
    print(response_data)
    assert response.status_code == STATUS_OK
    for key in expected_keys:
        assert key in response_data.keys()


def test_post_booking():
    payload = {
        "firstname": "Ira",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(BASE_URL, json=payload)
    print(response.json())
    assert response.status_code == STATUS_OK
    booking_id = response.json()['bookingid']
    get_response = requests.get(f'{BASE_URL}/{booking_id}')
    assert get_response.json()['firstname'] == 'Ira'


def test_create_booking_with_fixture(get_new_booking_id):
    response = requests.get(f'{BASE_URL}/{get_new_booking_id}')
    assert response.json()['firstname'] == 'Olya'


def test_delete_new_booking(get_new_booking_id, get_token):
    headers = {'Cookie': f'token = {get_token}'}
    response = requests.delete(f'{BASE_URL}/{get_new_booking_id}', headers=headers)
    assert response.status_code == 201
    get_response = requests.get(f'{BASE_URL}/{get_new_booking_id}')
    assert get_response.status_code == 404


response = requests.get("https://yandex.ru/search/?clid=2801392&text=%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%D1%8B+%D0%BE%D0%BE%D0%BF&lr=15")
assert  response.status_code == 200, "Запрос на получение ответа от сайта сломан"
print(response.text)