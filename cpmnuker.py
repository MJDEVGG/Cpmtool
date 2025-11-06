import requests
from time import sleep

BASE_URL: str = "https://mjcpm.squareweb.app/api"

class CPMNuker:

    def __init__(self, access_key) -> None:
        self.auth_token = None
        self.access_key = access_key
    
    def get_key_data(self) -> any:
        params = { "key": self.access_key }
        response = requests.get(f"{BASE_URL}/get_key_data", params=params)
        response.encoding = 'utf-8'
        response_decoded = response.json()
        return response_decoded

    def login(self, email, password) -> int:
        payload = { "account_email": email.encode('utf-8'), "account_password": password.encode('utf-8') }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/account_login", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return -1
        
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")
    
    def set_player_rank(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/set_rank", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return False
        return response_decoded.get("ok")
    
