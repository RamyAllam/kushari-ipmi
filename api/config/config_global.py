# ========================================================================================= #
# Variables strings
json_output_success_string = "success"
json_output_failed_string = "failed"
json_output_error_string = "error"
json_ipmi_failed_connecting_string = "Failed connecting to IPMI"
json_ipmi_boot_setnextboot_failed_string = "Failed to configure the next boot"
json_ipmi_chassis_power_failed_string = "Failed to manage the chassis status"
json_ipmi_network_failed_string = "Failed to query IPMI network information"
json_ipmi_users_failed_string = "Failed to manage IPMI users"
# ========================================================================================= #
# Variables - Serializers - strings
ipmi_boot_options = ['hd', 'network', 'optical', 'setup', 'default']

# Take care of ordering, as this will affect serializers choose field default
ipmi_persist_options = [True, False]

# Take care of ordering, as this will affect serializers choose field default
ipmi_uefiboot_options = [True, False]

ipmi_users_control_mode = ['enable', 'disable', 'set_password', 'test_password']

ipmi_network_bmc_config_options = ['static', 'dhcp']
# ========================================================================================= #
# API EndPoints
inventory_api_host = "http://kushari-inventory.domain.tld:8000"
inventory_api_severinfo = "api/inventory/info"
inventory_api_severinfo_url = "{}/{}".format(inventory_api_host, inventory_api_severinfo)
inventory_api_token = ""
# ========================================================================================= #
