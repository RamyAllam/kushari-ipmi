import json
from api.config.config_global import json_output_success_string, json_output_failed_string, json_output_error_string
import ipmi_boot_setnextboot
import ipmi_chassis_power_control
import ast


# Boot and reboot
def start_ipmi_boot_immediate(bmc_ip, bmc_username, bmc_password, boot_option='network', power_status='boot'):
    ipmi_boot_immediate_data = dict()
    ipmi_boot_immediate_data['action'] = 'IPMI - Set boot option and reboot'

    try:
        # Set next boot to PXE
        ipmi_boot_setnextboot_object = ipmi_boot_setnextboot.start_ipmi_boot_setnextboot(
            bmc_ip, bmc_username, bmc_password, boot_option
        )

        # The object returns str value, make sure it's a dict
        ipmi_boot_setnextboot_object = ast.literal_eval(ipmi_boot_setnextboot_object)

        # Check if next boot successfully configured
        if ipmi_boot_setnextboot_object['status'] == json_output_success_string:

            # If next boot is configured, reboot the server
            ipmi_chassis_power_control_object = ipmi_chassis_power_control.start_ipmi_chassis_power_control(
                bmc_ip, bmc_username, bmc_password, power_status)

            # The object returns str value, make sure it's a dict
            ipmi_chassis_power_control_object = ast.literal_eval(ipmi_chassis_power_control_object)

            # Check the reboot request status
            if ipmi_chassis_power_control_object['status'] == json_output_success_string:
                ipmi_boot_immediate_data['status'] = json_output_success_string
                ipmi_boot_immediate_data['data'] = ipmi_chassis_power_control_object['data']
            else:
                # If reboot failed, return the chassis function data
                ipmi_boot_immediate_data['status'] = json_output_failed_string
                ipmi_boot_immediate_data['data'] = ipmi_chassis_power_control_object['data']

        # If next boot configuration failed, return setnextboot function data
        else:
            ipmi_boot_immediate_data['status'] = json_output_failed_string
            ipmi_boot_immediate_data['data'] = ipmi_boot_setnextboot_object['data']

        return json.dumps(ipmi_boot_immediate_data)

    except Exception as e:
        ipmi_boot_immediate_data['status'] = json_output_error_string
        ipmi_boot_immediate_data['data'] = "{}".format(e)
        return json.dumps(ipmi_boot_immediate_data)
