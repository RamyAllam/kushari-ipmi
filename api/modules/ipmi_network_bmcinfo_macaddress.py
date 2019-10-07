import json
from pyghmi.ipmi import command
from api.config.config_global import json_output_success_string, json_output_failed_string, json_output_error_string,\
    json_ipmi_network_failed_string, json_ipmi_failed_connecting_string

# BMC mac address


def start_ipmi_network_bmcinfo_macaddress(bmc_ip, bmc_username, bmc_password):
    ipmi_network_bmcinfo_macaddress_data = dict()
    ipmi_network_bmcinfo_macaddress_data['action'] = 'IPMI - BMC Network Mac Address'

    try:
        connection_object = command.Command(bmc=bmc_ip, userid=bmc_username, password=bmc_password)

        if connection_object:
            cmd_results = connection_object.get_net_configuration()

            if cmd_results and "error" not in cmd_results:
                ipmi_network_bmcinfo_macaddress_data['status'] = json_output_success_string
                ipmi_network_bmcinfo_macaddress_data['data'] = cmd_results['mac_address']

            # Return the error string if found in the results
            elif "error" in cmd_results:
                ipmi_network_bmcinfo_macaddress_data['status'] = json_output_failed_string
                ipmi_network_bmcinfo_macaddress_data['data'] = cmd_results

            else:
                ipmi_network_bmcinfo_macaddress_data['status'] = json_output_failed_string
                ipmi_network_bmcinfo_macaddress_data['data'] = json_ipmi_network_failed_string
        else:
            ipmi_network_bmcinfo_macaddress_data['status'] = json_output_failed_string
            ipmi_network_bmcinfo_macaddress_data['data'] = json_ipmi_failed_connecting_string

        return json.dumps(ipmi_network_bmcinfo_macaddress_data)

    except Exception as e:
        ipmi_network_bmcinfo_macaddress_data['status'] = json_output_error_string
        ipmi_network_bmcinfo_macaddress_data['data'] = "{}".format(e)
        return json.dumps(ipmi_network_bmcinfo_macaddress_data)
