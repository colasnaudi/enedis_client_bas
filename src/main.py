from EnedisAPI import EnedisAPI

def main():
    # Initialize EnedisAPI
    enedis_api = EnedisAPI()

    # Get access token
    access_token = enedis_api.get_access_token()

    if access_token:
        # Example: Get daily consumption
        start_date = '2023-01-01'
        end_date = '2023-01-31'
        usage_point_id = '2'

        daily_consumption_data = enedis_api.get_daily_consumption(access_token, start_date, end_date, usage_point_id)
        print("Daily Consumption Data:")
        print(daily_consumption_data)

        # Additional examples for other API endpoints can be added here

    else:
        print("Failed to obtain access token. Check error messages above.")

if __name__ == "__main__":
    main()
