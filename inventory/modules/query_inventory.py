from api.config.config_global import json_output_success_string, json_output_failed_string, json_output_error_string,\
    inventory_api_severinfo_url
import requests


def start_query_inventory(server_name, inventory_api_severinfo_url=inventory_api_severinfo_url):
    query_inventory_data = dict()
    query_inventory_data['action'] = 'IPMI Inventory - Query'

    try:
        # Reserved for token
        # headers = {'Authorization': 'Token {}'.format(token)}
        inventory_api_severinfo_url = "{}/{}".format(inventory_api_severinfo_url, server_name)
        response = requests.get(inventory_api_severinfo_url)  # , headers=headers)
        response_json = response.json()
        response_status_code = response.status_code

        # Check if the request is valid
        if response_status_code == 200:
            bmc_ip = response_json['bmc_ip']
            bmc_password = response_json['bmc_password']
            bmc_username = response_json['bmc_username']

            query_inventory_data['status'] = json_output_success_string
            query_inventory_data['data'] = {
                'bmc_ip': bmc_ip,
                'bmc_username': bmc_username,
                'bmc_password': bmc_password
            }
        else:
            query_inventory_data['status'] = json_output_failed_string
            query_inventory_data['data'] = response_json

        return query_inventory_data

    except Exception as e:
        query_inventory_data['status'] = json_output_error_string
        query_inventory_data['data'] = "{}".format(e)
        return query_inventory_data
