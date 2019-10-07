import json
from pyghmi.ipmi import command
from api.config.config_global import json_output_success_string, json_output_failed_string, json_output_error_string,\
    json_ipmi_failed_connecting_string


def start_ipmi_network_bmc_config(bmc_ip, bmc_username, bmc_password, new_bmc_ip, new_bmc_gw, new_bmc_prefix,
                                  new_bmc_network_type):
    ipmi_bmc_network_config_data = dict()
    ipmi_bmc_network_config_data['action'] = 'IPMI - Configure BMC Network'

    try:
        new_bmc_ip = "{}/{}".format(new_bmc_ip, new_bmc_prefix)
        connection_object = command.Command(bmc=bmc_ip, userid=bmc_username, password=bmc_password)
        if connection_object:
            cmd_results = connection_object.set_net_configuration(
                ipv4_address=new_bmc_ip, ipv4_configuration=new_bmc_network_type, ipv4_gateway=new_bmc_gw
            )

            # The results are always None, so let's expect its none for success too
            if cmd_results is None:
                ipmi_bmc_network_config_data['status'] = json_output_success_string
                ipmi_bmc_network_config_data['data'] = cmd_results

        # If connection error, return the connection error string
        else:
            ipmi_bmc_network_config_data['status'] = json_output_failed_string
            ipmi_bmc_network_config_data['data'] = json_ipmi_failed_connecting_string

        return json.dumps(ipmi_bmc_network_config_data)

    # Return the exception message
    except Exception as e:
        ipmi_bmc_network_config_data['status'] = json_output_error_string
        ipmi_bmc_network_config_data['data'] = "{}".format(e)
        return json.dumps(ipmi_bmc_network_config_data)
