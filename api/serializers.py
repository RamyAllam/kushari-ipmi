from rest_framework import serializers
from api.config.config_global import ipmi_boot_options, ipmi_persist_options, ipmi_uefiboot_options, ipmi_users_control_mode,\
    ipmi_network_bmc_config_options


class ipmi_chassis_power_control_serializer(serializers.Serializer):
    bmc_ip = serializers.IPAddressField()
    bmc_username = serializers.CharField(max_length=1000)
    bmc_password = serializers.CharField(max_length=1000)


class ipmi_chassis_power_status_serializer(serializers.Serializer):
    bmc_ip = serializers.IPAddressField()
    bmc_username = serializers.CharField(max_length=1000)
    bmc_password = serializers.CharField(max_length=1000)


class ipmi_chassis_uid_control_serializer(serializers.Serializer):
    bmc_ip = serializers.IPAddressField()
    bmc_username = serializers.CharField(max_length=1000)
    bmc_password = serializers.CharField(max_length=1000)
    uid_status = serializers.BooleanField()
    uid_duration = serializers.IntegerField(required=False)


class ipmi_network_bmcinfo_serializer(serializers.Serializer):
    bmc_ip = serializers.IPAddressField()
    bmc_username = serializers.CharField(max_length=1000)
    bmc_password = serializers.CharField(max_length=1000)


class ipmi_network_bmc_config_serializer(serializers.Serializer):
    bmc_ip = serializers.IPAddressField()
    bmc_username = serializers.CharField(max_length=1000)
    bmc_password = serializers.CharField(max_length=1000)
    new_bmc_ip = serializers.IPAddressField()
    new_bmc_gw = serializers.IPAddressField()
    new_bmc_prefix = serializers.IntegerField(max_value=32, default=24)
    new_bmc_network_type = serializers.ChoiceField(choices=ipmi_network_bmc_config_options, allow_blank=False,
                                                   allow_null=False, default=ipmi_network_bmc_config_options[0])


class ipmi_network_eth0info_serializer(serializers.Serializer):
    bmc_ip = serializers.IPAddressField()
    bmc_username = serializers.CharField(max_length=1000)
    bmc_password = serializers.CharField(max_length=1000)


class ipmi_boot_setnextboot_serializer(serializers.Serializer):
    bmc_ip = serializers.IPAddressField()
    bmc_username = serializers.CharField(max_length=1000)
    bmc_password = serializers.CharField(max_length=1000)
    boot_option = serializers.ChoiceField(choices=ipmi_boot_options, allow_blank=False, allow_null=False)
    persist = serializers.ChoiceField(choices=ipmi_persist_options, allow_blank=False, allow_null=False,
                                      default=ipmi_uefiboot_options[1])
    uefiboot = serializers.ChoiceField(choices=ipmi_uefiboot_options, allow_blank=False, allow_null=True,
                                       default=ipmi_uefiboot_options[1])


class ipmi_boot_immediate_serializer(serializers.Serializer):
    bmc_ip = serializers.IPAddressField()
    bmc_username = serializers.CharField(max_length=1000)
    bmc_password = serializers.CharField(max_length=1000)
    boot_option = serializers.ChoiceField(choices=ipmi_boot_options, allow_blank=False, allow_null=False)


class ipmi_users_control_serializer(serializers.Serializer):
    bmc_ip = serializers.IPAddressField()
    bmc_username = serializers.CharField(max_length=1000)
    bmc_password = serializers.CharField(max_length=1000)
    uid = serializers.IntegerField(max_value=255)
    mode = serializers.ChoiceField(choices=ipmi_users_control_mode, allow_blank=False, allow_null=False)
    password = serializers.CharField(max_length=19, required=False)
