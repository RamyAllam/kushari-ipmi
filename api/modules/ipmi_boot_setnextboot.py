import json
from pyghmi.ipmi import command
from api.config.config_global import json_output_success_string, json_output_failed_string, json_output_error_string,\
    json_ipmi_boot_setnextboot_failed_string, json_ipmi_failed_connecting_string


def start_ipmi_boot_setnextboot(bmc_ip, bmc_username, bmc_password, boot_option, persist=False, uefiboot=False):
    ipmi_boot_setnextboot_data = dict()
    ipmi_boot_setnextboot_data['action'] = 'IPMI - Configure boot'

    try:
        connection_object = command.Command(bmc=bmc_ip, userid=bmc_username, password=bmc_password)

        if connection_object:
            cmd_results = connection_object.set_bootdev(bootdev=boot_option, persist=persist, uefiboot=uefiboot)

            if cmd_results and "error" not in cmd_results:
                ipmi_boot_setnextboot_data['status'] = json_output_success_string
                ipmi_boot_setnextboot_data['data'] = cmd_results

            # Return the error string if found in the results
            elif "error" in cmd_results:
                ipmi_boot_setnextboot_data['status'] = json_output_failed_string
                ipmi_boot_setnextboot_data['data'] = cmd_results
            else:
                ipmi_boot_setnextboot_data['status'] = json_output_failed_string
                ipmi_boot_setnextboot_data['data'] = json_ipmi_boot_setnextboot_failed_string
        else:
            ipmi_boot_setnextboot_data['status'] = json_output_failed_string
            ipmi_boot_setnextboot_data['data'] = json_ipmi_failed_connecting_string

        return json.dumps(ipmi_boot_setnextboot_data)

    except Exception as e:
        ipmi_boot_setnextboot_data['status'] = json_output_error_string
        ipmi_boot_setnextboot_data['data'] = "{}".format(e)
        return json.dumps(ipmi_boot_setnextboot_data)
