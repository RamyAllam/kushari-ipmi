from inventory.modules import query_inventory
from api.modules.ipmi_chassis_power_status import start_ipmi_chassis_power_status
from api.config.config_global import json_output_success_string, json_output_failed_string, json_output_error_string
import json
import ast


def start_inventory_ipmi_chassis_power_status(server_name):
    ipmi_chassis_power_status_data = dict()
    ipmi_chassis_power_status_data['action'] = 'IPMI Inventory - Chassis Status'

    try:
        inventory_data = query_inventory.start_query_inventory(server_name)

        # Check if data returned from inventory
        if inventory_data['status'] == json_output_success_string:
            bmc_ip = inventory_data['data']['bmc_ip']
            bmc_username = inventory_data['data']['bmc_username']
            bmc_password = inventory_data['data']['bmc_password']
            cmd_results = start_ipmi_chassis_power_status(
                bmc_ip=bmc_ip, bmc_username=bmc_username, bmc_password=bmc_password
            )

            # The object returns str value, make sure it's a dict
            cmd_results = ast.literal_eval(cmd_results)

            # Check the command results
            if cmd_results['status'] == json_output_success_string:
                ipmi_chassis_power_status_data['status'] = json_output_success_string
                ipmi_chassis_power_status_data['data'] = cmd_results
            else:
                ipmi_chassis_power_status_data['status'] = json_output_failed_string
                ipmi_chassis_power_status_data['data'] = cmd_results

        # If failed or no data in inventory
        else:
            ipmi_chassis_power_status_data['status'] = json_output_failed_string
            ipmi_chassis_power_status_data['data'] = inventory_data

        # Return the data
        return json.dumps(ipmi_chassis_power_status_data)

    except Exception as e:
        ipmi_chassis_power_status_data['status'] = json_output_error_string
        ipmi_chassis_power_status_data['data'] = "{}".format(repr(e))
        return json.dumps(ipmi_chassis_power_status_data)
