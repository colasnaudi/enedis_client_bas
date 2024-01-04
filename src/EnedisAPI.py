import requests
import os
from dotenv import load_dotenv

class EnedisAPI:
    def __init__(self):
        load_dotenv()

        self.base_url = 'https://ext.hml.api.enedis.fr'
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')
        print("# --------------- Enedis API Credentials --------------- #\n")
        print(f"Client ID: {self.client_id}")
        print(f"Client Secret: {self.client_secret}")

    def get_access_token(self):
        endpoint = '/oauth2/v3/token'

        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.post(self.base_url + endpoint, data=data, headers=headers)

        print("\n# --------------- Enedis API Response --------------- #\n")

        if response.status_code == 200:
            return response.json().get('access_token')
        else:
            print(f"Error getting access token: {response.status_code}")
            print(response.text)  # Print the response text for additional details
            return None
        
    def get_daily_consumption(self, access_token, start, end, usage_point_id):
        endpoint = '/metering_data_dc/v5/daily_consumption'

        params = {
            'start': start,
            'end': end,
            'usage_point_id': usage_point_id
        }

        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.get(self.base_url + endpoint, params=params, headers=headers)

        print("\n# --------------- Enedis API Response --------------- #\n")

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error getting daily consumption: {response.status_code}")
            print(response.text)

    def get_daily_consumption_max_power(self, access_token, start, end, usage_point_id):
        endpoint = '/metering_data_dcmp/v5/daily_consumption_max_power'

        params = {
            'start': start,
            'end': end,
            'usage_point_id': usage_point_id
        }

        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.get(self.base_url + endpoint, params=params, headers=headers)

        print("\n# --------------- Enedis API Response --------------- #\n")

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error getting daily consumption max power: {response.status_code}")
            print(response.text)
    
    def get_consumption_load_curve(self, access_token, start, end, usage_point_id):
        endpoint = '/metering_data_clc/v5/consumption_load_curve'

        params = {
            'start': start,
            'end': end,
            'usage_point_id': usage_point_id
        }

        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.get(self.base_url + endpoint, params=params, headers=headers)

        print("\n# --------------- Enedis API Response --------------- #\n")

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error getting consumption load curve: {response.status_code}")
            print(response.text)

    def get_daily_production(self, access_token, start, end, usage_point_id):
        endpoint = '/metering_data_dp/v5/daily_production'

        params = {
            'start': start,
            'end': end,
            'usage_point_id': usage_point_id
        }

        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.get(self.base_url + endpoint, params=params, headers=headers)

        print("\n# --------------- Enedis API Response --------------- #\n")

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error getting daily production: {response.status_code}")
            print(response.text)

    def get_production_load_curve(self, access_token, start, end, usage_point_id):
        endpoint = '/metering_data_plc/v5/production_load_curve'

        params = {
            'start': start,
            'end': end,
            'usage_point_id': usage_point_id
        }

        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.get(self.base_url + endpoint, params=params, headers=headers)

        print("\n# --------------- Enedis API Response --------------- #\n")

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error getting production load curve: {response.status_code}")
            print(response.text)

    def get_identity(self, access_token, usage_point_id):
        endpoint = '/customers_i/v5/identity'

        params = {
            'usage_point_id': usage_point_id
        }

        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.get(self.base_url + endpoint, params=params, headers=headers)

        print("\n# --------------- Enedis API Response --------------- #\n")

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error getting identity: {response.status_code}")
            print(response.text)

    def get_contact_data(self, access_token, usage_point_id):
        endpoint = '/customers_cd/v5/contact_data'

        params = {
            'usage_point_id': usage_point_id
        }

        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.get(self.base_url + endpoint, params=params, headers=headers)

        print("\n# --------------- Enedis API Response --------------- #\n")

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error getting contact data: {response.status_code}")
            print(response.text)

    def get_usage_points_contracts(self, access_token, usage_point_id):
        endpoint = '/customers_upc/v5/usage_points/contracts'

        params = {
            'usage_point_id': usage_point_id
        }

        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.get(self.base_url + endpoint, params=params, headers=headers)

        print("\n# --------------- Enedis API Response --------------- #\n")

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error getting usage points contracts: {response.status_code}")
            print(response.text)

    def get_usage_points_addresses(self, access_token, usage_point_id):
        endpoint = '/customers_upa/v5/usage_points/addresses'

        params = {
            'usage_point_id': usage_point_id
        }

        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.get(self.base_url + endpoint, params=params, headers=headers)

        print("\n# --------------- Enedis API Response --------------- #\n")
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error getting usage points addresses: {response.status_code}")
            print(response.text)