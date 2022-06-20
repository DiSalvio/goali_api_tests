import requests
from dotenv import load_dotenv
from faker import Faker
import os

load_dotenv()


def decode_message(response):
    print(response._content)
    return eval(response._content.decode('utf-8'))['Message']


def test_sign_up_without_params():
    payload = {
    }
    response = requests.post(os.getenv('BASE_URL') + 'signup/', data=payload)
    assert response.status_code == 400


def test_sign_up_with_valid_params():
    fake = Faker()
    fake_password = fake.password()
    payload = {
        "email": fake.email(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "username": fake.user_name(),
        "password": fake_password,
        "confirm_password": fake_password
    }
    response = requests.post(os.getenv('BASE_URL') + 'signup/', data=payload)
    assert response.status_code == 200
    assert decode_message(response) == "Successfully Signed up"
