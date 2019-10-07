from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ipmi_chassis_power_on_view, ipmi_chassis_power_off_view, ipmi_chassis_power_reset_view,\
    ipmi_chassis_power_osoff_view, ipmi_chassis_power_status_view, ipmi_network_bmcinfo_view,\
    ipmi_network_bmcinfo_macaddress_view, ipmi_boot_setnextboot_view, ipmi_boot_immediate_view,\
    ipmi_network_eth0info_macaddress_view, ipmi_users_control_view, ipmi_chassis_power_cycle_view,\
    ipmi_chassis_uid_control_view, ipmi_network_bmc_config_view
from rest_framework.authtoken import views

urlpatterns = {
    url(r'^chassis/poweron/$', ipmi_chassis_power_on_view, name="ipmi_chassis_power_on"),
    url(r'^chassis/poweroff/$', ipmi_chassis_power_off_view, name="ipmi_chassis_power_off"),
    url(r'^chassis/powerreset/$', ipmi_chassis_power_reset_view, name="ipmi_chassis_power_reset"),
    url(r'^chassis/powercycle/$', ipmi_chassis_power_cycle_view, name="ipmi_chassis_power_cycle"),
    url(r'^chassis/osoff/$', ipmi_chassis_power_osoff_view, name="ipmi_chassis_power_osoff"),
    url(r'^chassis/powerstatus/$', ipmi_chassis_power_status_view, name="ipmi_chassis_power_status"),
    url(r'^chassis/uidcontrol/$', ipmi_chassis_uid_control_view, name="ipmi_chassis_uid_control"),
    url(r'^network/bmcinfo/$', ipmi_network_bmcinfo_view, name="ipmi_network_bmcinfo"),
    url(r'^network/bmcinfo/macaddress/$', ipmi_network_bmcinfo_macaddress_view, name="ipmi_network_bmcinfo_macaddress"),
    url(r'^network/bmc/config/$', ipmi_network_bmc_config_view, name="ipmi_network_bmc_config"),
    url(r'^network/eth0info/macaddress/$', ipmi_network_eth0info_macaddress_view, name="ipmi_network_eth0info_macaddress"),
    url(r'^boot/setnextboot/$', ipmi_boot_setnextboot_view, name="ipmi_boot_setnextboot"),
    url(r'^boot/immediate/$', ipmi_boot_immediate_view, name="ipmi_boot_immediate"),
    url(r'^users/control/$', ipmi_users_control_view, name="ipmi_users_control"),

}

urlpatterns = format_suffix_patterns(urlpatterns)
