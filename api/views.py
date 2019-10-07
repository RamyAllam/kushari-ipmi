# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from api.modules import ipmi_chassis_power_control, ipmi_chassis_power_status, ipmi_network_bmcinfo,\
    ipmi_network_bmcinfo_macaddress, ipmi_boot_setnextboot, ipmi_boot_immediate, ipmi_network_eth0info_macaddress,\
    ipmi_users_control, ipmi_chassis_uid_control, ipmi_network_bmc_config
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ipmi_chassis_power_control_serializer, ipmi_chassis_power_status_serializer, \
    ipmi_network_bmcinfo_serializer, ipmi_boot_setnextboot_serializer, ipmi_boot_immediate_serializer,\
    ipmi_network_eth0info_serializer, ipmi_users_control_serializer, ipmi_chassis_uid_control_serializer,\
    ipmi_network_bmc_config_serializer
from rest_framework.renderers import JSONRenderer
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from api.config.config_global import ipmi_network_bmc_config_options

# Create your views here.
@api_view(['POST'])
def ipmi_chassis_power_on_view(request):

    if request.method == 'POST':
        serializer = ipmi_chassis_power_control_serializer(data=request.data)
        if serializer.is_valid():
            # Extract the data from json
            json = JSONRenderer().render(serializer.data)
            stream = BytesIO(json)
            data = JSONParser().parse(stream)
            bmc_ip_from_request = data['bmc_ip']
            bmc_username_from_request = data['bmc_username']
            bmc_password_from_request = data['bmc_password']

            # IPMI Chassis power on
            results = ipmi_chassis_power_control.start_ipmi_chassis_power_control(
                bmc_ip=bmc_ip_from_request,
                bmc_username=bmc_username_from_request,
                bmc_password=bmc_password_from_request,
                power_status='on'
            )
            # If Ok, return the results
            return HttpResponse(results, content_type="application/json")
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


@api_view(['POST'])
def ipmi_chassis_power_off_view(request):

    if request.method == 'POST':
        serializer = ipmi_chassis_power_control_serializer(data=request.data)
        if serializer.is_valid():
            # Extract the data from json
            json = JSONRenderer().render(serializer.data)
            stream = BytesIO(json)
            data = JSONParser().parse(stream)
            bmc_ip_from_request = data['bmc_ip']
            bmc_username_from_request = data['bmc_username']
            bmc_password_from_request = data['bmc_password']

            # IPMI Chassis power off
            results = ipmi_chassis_power_control.start_ipmi_chassis_power_control(
                bmc_ip=bmc_ip_from_request,
                bmc_username=bmc_username_from_request,
                bmc_password=bmc_password_from_request,
                power_status='off'
            )
            # If Ok, return the results
            return HttpResponse(results, content_type="application/json")
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


@api_view(['POST'])
def ipmi_chassis_power_reset_view(request):

    if request.method == 'POST':
        serializer = ipmi_chassis_power_control_serializer(data=request.data)
        if serializer.is_valid():
            # Extract the data from json
            json = JSONRenderer().render(serializer.data)
            stream = BytesIO(json)
            data = JSONParser().parse(stream)
            bmc_ip_from_request = data['bmc_ip']
            bmc_username_from_request = data['bmc_username']
            bmc_password_from_request = data['bmc_password']

            # IPMI Chassis power reset
            results = ipmi_chassis_power_control.start_ipmi_chassis_power_control(
                bmc_ip=bmc_ip_from_request,
                bmc_username=bmc_username_from_request,
                bmc_password=bmc_password_from_request,
                power_status='reset'
            )
            # If Ok, return the results
            return HttpResponse(results, content_type="application/json")
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


@api_view(['POST'])
def ipmi_chassis_power_cycle_view(request):

    if request.method == 'POST':
        serializer = ipmi_chassis_power_control_serializer(data=request.data)
        if serializer.is_valid():
            # Extract the data from json
            json = JSONRenderer().render(serializer.data)
            stream = BytesIO(json)
            data = JSONParser().parse(stream)
            bmc_ip_from_request = data['bmc_ip']
            bmc_username_from_request = data['bmc_username']
            bmc_password_from_request = data['bmc_password']

            # IPMI Chassis Power cycle
            results = ipmi_chassis_power_control.start_ipmi_chassis_power_control(
                bmc_ip=bmc_ip_from_request,
                bmc_username=bmc_username_from_request,
                bmc_password=bmc_password_from_request,
                power_status='boot'
            )
            # If Ok, return the results
            return HttpResponse(results, content_type="application/json")
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


@api_view(['POST'])
def ipmi_chassis_power_osoff_view(request):

    if request.method == 'POST':
        serializer = ipmi_chassis_power_control_serializer(data=request.data)
        if serializer.is_valid():
            # Extract the data from json
            json = JSONRenderer().render(serializer.data)
            stream = BytesIO(json)
            data = JSONParser().parse(stream)
            bmc_ip_from_request = data['bmc_ip']
            bmc_username_from_request = data['bmc_username']
            bmc_password_from_request = data['bmc_password']

            # IPMI Chassis OS shutdown
            results = ipmi_chassis_power_control.start_ipmi_chassis_power_control(
                bmc_ip=bmc_ip_from_request,
                bmc_username=bmc_username_from_request,
                bmc_password=bmc_password_from_request,
                power_status='shutdown'
            )
            # If Ok, return the results
            return HttpResponse(results, content_type="application/json")
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


@api_view(['POST'])
def ipmi_chassis_power_status_view(request):

    if request.method == 'POST':
        serializer = ipmi_chassis_power_status_serializer(data=request.data)
        if serializer.is_valid():
            # Extract the data from json
            json = JSONRenderer().render(serializer.data)
            stream = BytesIO(json)
            data = JSONParser().parse(stream)
            bmc_ip_from_request = data['bmc_ip']
            bmc_username_from_request = data['bmc_username']
            bmc_password_from_request = data['bmc_password']

            # IPMI Chassis get power status
            results = ipmi_chassis_power_status.start_ipmi_chassis_power_status(
                bmc_ip=bmc_ip_from_request,
                bmc_username=bmc_username_from_request,
                bmc_password=bmc_password_from_request
            )
            # If Ok, return the results
            return HttpResponse(results, content_type="application/json")
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


@api_view(['POST'])
def ipmi_chassis_uid_control_view(request):

    if request.method == 'POST':
        serializer = ipmi_chassis_uid_control_serializer(data=request.data)
        if serializer.is_valid():
            # Extract the data from json
            json = JSONRenderer().render(serializer.data)
            stream = BytesIO(json)
            data = JSONParser().parse(stream)
            bmc_ip_from_request = data['bmc_ip']
            bmc_username_from_request = data['bmc_username']
            bmc_password_from_request = data['bmc_password']
            uid_status_from_request = data['uid_status']

            # Duration field is optional, let's check if it's in the request
            uid_duration_from_request = None
            try:
                uid_duration_from_request = data['uid_duration']
            except:
                pass

            # IPMI Chassis UID Control
            results = ipmi_chassis_uid_control.start_ipmi_chassis_uid_control(
                bmc_ip=bmc_ip_from_request,
                bmc_username=bmc_username_from_request,
                bmc_password=bmc_password_from_request,
                uid_status=uid_status_from_request,
                uid_duration=uid_duration_from_request
            )

            # If Ok, return the results
            return HttpResponse(results, content_type="application/json")

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


@api_view(['POST'])
def ipmi_network_bmcinfo_view(request):

    if request.method == 'POST':
        serializer = ipmi_network_bmcinfo_serializer(data=request.data)
        if serializer.is_valid():
            # Extract the data from json
            json = JSONRenderer().render(serializer.data)
            stream = BytesIO(json)
            data = JSONParser().parse(stream)
            bmc_ip_from_request = data['bmc_ip']
            bmc_username_from_request = data['bmc_username']
            bmc_password_from_request = data['bmc_password']

            # IPMI get network info
            results = ipmi_network_bmcinfo.start_ipmi_network_bmcinfo(
                bmc_ip=bmc_ip_from_request,
                bmc_username=bmc_username_from_request,
                bmc_password=bmc_password_from_request
            )
            # If Ok, return the results
            return HttpResponse(results, content_type="application/json")
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


@api_view(['POST'])
def ipmi_network_bmcinfo_macaddress_view(request):

    if request.method == 'POST':
        serializer = ipmi_network_bmcinfo_serializer(data=request.data)
        if serializer.is_valid():
            # Extract the data from json
            json = JSONRenderer().render(serializer.data)
            stream = BytesIO(json)
            data = JSONParser().parse(stream)
            bmc_ip_from_request = data['bmc_ip']
            bmc_username_from_request = data['bmc_username']
            bmc_password_from_request = data['bmc_password']

            # IPMI get network bmc mac address
            results = ipmi_network_bmcinfo_macaddress.start_ipmi_network_bmcinfo_macaddress(
                bmc_ip=bmc_ip_from_request,
                bmc_username=bmc_username_from_request,
                bmc_password=bmc_password_from_request
            )
            # If Ok, return the results
            return HttpResponse(results, content_type="application/json")
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


@api_view(['POST'])
def ipmi_network_eth0info_macaddress_view(request):

    if request.method == 'POST':
        serializer = ipmi_network_eth0info_serializer(data=request.data)
        if serializer.is_valid():
            # Extract the data from json
            json = JSONRenderer().render(serializer.data)
            stream = BytesIO(json)
            data = JSONParser().parse(stream)
            bmc_ip_from_request = data['bmc_ip']
            bmc_username_from_request = data['bmc_username']
            bmc_password_from_request = data['bmc_password']

            # IPMI get network eth0 mac address
            results = ipmi_network_eth0info_macaddress.start_ipmi_network_eth0info_macaddress(
                bmc_ip=bmc_ip_from_request,
                bmc_username=bmc_username_from_request,
                bmc_password=bmc_password_from_request
            )
            # If Ok, return the results
            return HttpResponse(results, content_type="application/json")
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


@api_view(['POST'])
def ipmi_network_bmc_config_view(request):

    if request.method == 'POST':
        serializer = ipmi_network_bmc_config_serializer(data=request.data)
        if serializer.is_valid():
            # Extract the data from json
            json = JSONRenderer().render(serializer.data)
            stream = BytesIO(json)
            data = JSONParser().parse(stream)
            bmc_ip_from_request = data['bmc_ip']
            bmc_username_from_request = data['bmc_username']
            bmc_password_from_request = data['bmc_password']
            new_bmc_ip_from_request = data['new_bmc_ip']
            new_bmc_gw_from_request = data['new_bmc_gw']
            new_bmc_prefix_from_request = data['new_bmc_prefix']

            # new_bmc_network_type_from_request field is optional, let's check if it's in the request
            new_bmc_network_type_from_request = ipmi_network_bmc_config_options[0]
            try:
                new_bmc_network_type_from_request = data['new_bmc_network_type']
            except:
                pass

            # IPMI BMC Configure Networking
            results = ipmi_network_bmc_config.start_ipmi_network_bmc_config(
                bmc_ip=bmc_ip_from_request,
                bmc_username=bmc_username_from_request,
                bmc_password=bmc_password_from_request,
                new_bmc_ip=new_bmc_ip_from_request,
                new_bmc_gw=new_bmc_gw_from_request,
                new_bmc_prefix=new_bmc_prefix_from_request,
                new_bmc_network_type=new_bmc_network_type_from_request
            )

            # If Ok, return the results
            return HttpResponse(results, content_type="application/json")

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


@api_view(['POST'])
def ipmi_boot_setnextboot_view(request):

    if request.method == 'POST':
        serializer = ipmi_boot_setnextboot_serializer(data=request.data)
        if serializer.is_valid():
            # Extract the data from json
            json = JSONRenderer().render(serializer.data)
            stream = BytesIO(json)
            data = JSONParser().parse(stream)
            bmc_ip_from_request = data['bmc_ip']
            bmc_username_from_request = data['bmc_username']
            bmc_password_from_request = data['bmc_password']
            boot_option_from_request = data['boot_option']
            persist_option_from_request = data['persist']
            uefiboot_option_from_request = data['uefiboot']

            # IPMI Set boot
            results = ipmi_boot_setnextboot.start_ipmi_boot_setnextboot(
                bmc_ip=bmc_ip_from_request,
                bmc_username=bmc_username_from_request,
                bmc_password=bmc_password_from_request,
                boot_option=boot_option_from_request,
                persist=persist_option_from_request,
                uefiboot=uefiboot_option_from_request
            )
            # If Ok, return the results
            return HttpResponse(results, content_type="application/json")
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


@api_view(['POST'])
def ipmi_boot_immediate_view(request):

    if request.method == 'POST':
        serializer = ipmi_boot_immediate_serializer(data=request.data)
        if serializer.is_valid():
            # Extract the data from json
            json = JSONRenderer().render(serializer.data)
            stream = BytesIO(json)
            data = JSONParser().parse(stream)
            bmc_ip_from_request = data['bmc_ip']
            bmc_username_from_request = data['bmc_username']
            bmc_password_from_request = data['bmc_password']
            boot_option_from_request = data['boot_option']

            # IPMI boot immediate
            results = ipmi_boot_immediate.start_ipmi_boot_immediate(
                bmc_ip=bmc_ip_from_request,
                bmc_username=bmc_username_from_request,
                bmc_password=bmc_password_from_request,
                boot_option=boot_option_from_request
            )
            # If Ok, return the results
            return HttpResponse(results, content_type="application/json")
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


@api_view(['POST'])
def ipmi_users_control_view(request):

    if request.method == 'POST':
        serializer = ipmi_users_control_serializer(data=request.data)
        if serializer.is_valid():
            # Extract the data from json
            json = JSONRenderer().render(serializer.data)
            stream = BytesIO(json)
            data = JSONParser().parse(stream)
            bmc_ip_from_request = data['bmc_ip']
            bmc_username_from_request = data['bmc_username']
            bmc_password_from_request = data['bmc_password']
            uid_from_request = data['uid']
            mode_from_request = data['mode']

            # Password field is optional, let's check if it's in the request
            password_from_request = None
            try:
                password_from_request = data['password']
            except:
                pass

            # IPMI users control
            results = ipmi_users_control.start_ipmi_users_control(
                bmc_ip=bmc_ip_from_request,
                bmc_username=bmc_username_from_request,
                bmc_password=bmc_password_from_request,
                uid=uid_from_request,
                mode=mode_from_request,
                password=password_from_request
            )

            # If Ok, return the results
            return HttpResponse(results, content_type="application/json")

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")
