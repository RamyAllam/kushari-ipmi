import json
from pyghmi.ipmi import command
from api.config.config_global import json_output_success_string, json_output_failed_string, json_output_error_string,\
    json_ipmi_failed_connecting_string, json_ipmi_chassis_power_failed_string


def start_ipmi_chassis_power_control(bmc_ip, bmc_username, bmc_password, power_status):
    ipmi_chassis_power_on_data = dict()
    ipmi_chassis_power_on_data['action'] = 'IPMI - Chassis Control'

    try:
        connection_object = command.Command(bmc=bmc_ip, userid=bmc_username, password=bmc_password)
        if connection_object:
            cmd_results = connection_object.set_power(power_status)

            if cmd_results and "error" not in cmd_results:
                ipmi_chassis_power_on_data['status'] = json_output_success_string
                ipmi_chassis_power_on_data['data'] = cmd_results

            # Return the error string if found in the results
            elif "error" in cmd_results:
                ipmi_chassis_power_on_data['status'] = json_output_failed_string
                ipmi_chassis_power_on_data['data'] = cmd_results

            else:
                ipmi_chassis_power_on_data['status'] = json_output_failed_string
                ipmi_chassis_power_on_data['data'] = json_ipmi_chassis_power_failed_string

        else:
            ipmi_chassis_power_on_data['status'] = json_output_failed_string
            ipmi_chassis_power_on_data['data'] = json_ipmi_failed_connecting_string

        return json.dumps(ipmi_chassis_power_on_data)

    except Exception as e:
        ipmi_chassis_power_on_data['status'] = json_output_error_string
        ipmi_chassis_power_on_data['data'] = "{}".format(e)
        return json.dumps(ipmi_chassis_power_on_data)
