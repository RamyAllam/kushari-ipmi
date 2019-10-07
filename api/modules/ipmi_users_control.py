import json
from pyghmi.ipmi import command
from api.config.config_global import json_output_success_string, json_output_failed_string, json_output_error_string,\
    json_ipmi_failed_connecting_string, json_ipmi_users_failed_string


def start_ipmi_users_control(bmc_ip, bmc_username, bmc_password, uid, mode, password=None):
    ipmi_users_control_data = dict()
    ipmi_users_control_data['action'] = 'IPMI - Users Control'

    try:
        connection_object = command.Command(bmc=bmc_ip, userid=bmc_username, password=bmc_password)
        if connection_object:
            # Password field is optional, let's check if it's in the request
            if password:
                # cmd_results returns true or false
                cmd_results = connection_object.set_user_password(uid, mode, password)
            else:
                cmd_results = connection_object.set_user_password(uid, mode, password)

            # Check the if true, return the command results
            if cmd_results:
                ipmi_users_control_data['status'] = json_output_success_string
                ipmi_users_control_data['data'] = cmd_results

            # If false, return the failed string
            else:
                ipmi_users_control_data['status'] = json_output_failed_string
                ipmi_users_control_data['data'] = json_ipmi_users_failed_string

        # If connection error, return the connection error string
        else:
            ipmi_users_control_data['status'] = json_output_failed_string
            ipmi_users_control_data['data'] = json_ipmi_failed_connecting_string

        return json.dumps(ipmi_users_control_data)

    # Return the exception message
    except Exception as e:
        ipmi_users_control_data['status'] = json_output_error_string
        ipmi_users_control_data['data'] = "{}".format(e)
        return json.dumps(ipmi_users_control_data)
