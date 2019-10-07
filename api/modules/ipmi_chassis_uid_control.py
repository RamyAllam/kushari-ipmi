import json
from pyghmi.ipmi import command
from api.config.config_global import json_output_success_string, json_output_failed_string, json_output_error_string,\
    json_ipmi_failed_connecting_string


def start_ipmi_chassis_uid_control(bmc_ip, bmc_username, bmc_password, uid_status, uid_duration=None):
    ipmi_chassis_uid_control_data = dict()
    ipmi_chassis_uid_control_data['action'] = 'IPMI - UID Control'

    try:
        connection_object = command.Command(bmc=bmc_ip, userid=bmc_username, password=bmc_password)
        if connection_object:
            cmd_results = connection_object.set_identify(on=uid_status, duration=uid_duration)

            # The results are always None, so let's expect its none for success too
            if cmd_results is None:
                ipmi_chassis_uid_control_data['status'] = json_output_success_string
                ipmi_chassis_uid_control_data['data'] = cmd_results

        else:
            ipmi_chassis_uid_control_data['status'] = json_output_failed_string
            ipmi_chassis_uid_control_data['data'] = json_ipmi_failed_connecting_string

        return json.dumps(ipmi_chassis_uid_control_data)

    except Exception as e:
        ipmi_chassis_uid_control_data['status'] = json_output_error_string
        ipmi_chassis_uid_control_data['data'] = "{}".format(e)
        return json.dumps(ipmi_chassis_uid_control_data)
