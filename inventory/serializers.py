from rest_framework import serializers
from api.config.config_global import ipmi_boot_options, ipmi_persist_options, ipmi_uefiboot_options,\
    ipmi_users_control_mode


class ipmi_chassis_power_control_serializer(serializers.Serializer):
    server_name = serializers.CharField(max_length=250)


class ipmi_chassis_power_status_serializer(serializers.Serializer):
    server_name = serializers.CharField(max_length=250)


class ipmi_network_bmcinfo_serializer(serializers.Serializer):
    server_name = serializers.CharField(max_length=250)


class ipmi_network_eth0info_serializer(serializers.Serializer):
    server_name = serializers.CharField(max_length=250)


class ipmi_boot_setnextboot_serializer(serializers.Serializer):
    server_name = serializers.CharField(max_length=250)
    boot_option = serializers.ChoiceField(choices=ipmi_boot_options, allow_blank=False, allow_null=False)
    persist = serializers.ChoiceField(choices=ipmi_persist_options, allow_blank=False, allow_null=False,
                                      default=ipmi_uefiboot_options[1])
    uefiboot = serializers.ChoiceField(choices=ipmi_uefiboot_options, allow_blank=False, allow_null=True,
                                       default=ipmi_uefiboot_options[1])


class ipmi_boot_immediate_serializer(serializers.Serializer):
    server_name = serializers.CharField(max_length=250)
    boot_option = serializers.ChoiceField(choices=ipmi_boot_options, allow_blank=False, allow_null=False)


class ipmi_users_control_serializer(serializers.Serializer):
    server_name = serializers.CharField(max_length=250)
    uid = serializers.IntegerField(max_value=255)
    mode = serializers.ChoiceField(choices=ipmi_users_control_mode, allow_blank=False, allow_null=False)
    password = serializers.CharField(max_length=19, required=False)
