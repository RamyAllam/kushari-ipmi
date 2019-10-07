# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from inventory.modules import inventory_ipmi_chassis_power_status, inventory_ipmi_chassis_power_control,\
    inventory_ipmi_network_bmcinfo, inventory_ipmi_network_bmcinfo_macaddress, inventory_ipmi_network_eth0info_macaddress,\
    inventory_ipmi_boot_setnextboot, inventory_ipmi_boot_immediate, inventory_ipmi_users_control

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ipmi_chassis_power_control_serializer, ipmi_chassis_power_status_serializer, \
    ipmi_network_bmcinfo_serializer, ipmi_boot_setnextboot_serializer, ipmi_boot_immediate_serializer,\
    ipmi_network_eth0info_serializer, ipmi_users_control_serializer
from rest_framework.renderers import JSONRenderer
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser


# # Create your views here.
@api_view(['POST'])
def ipmi_chassis_power_on_view(request):

    if request.method == 'POST':
        serializer = ipmi_chassis_power_control_serializer(data=request.data)
        if serializer.is_valid():
            # Extract the data from json
            json = JSONRenderer().render(serializer.data)
            stream = BytesIO(json)
            data = JSONParser().parse(stream)
            server_name_from_request = data['server_name']

            # IPMI Chassis power on
            results = inventory_ipmi_chassis_power_control.start_inventory_ipmi_chassis_power_control(
                server_name=server_name_from_request,
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
            server_name_from_request = data['server_name']

            # IPMI Chassis power off
            results = inventory_ipmi_chassis_power_control.start_inventory_ipmi_chassis_power_control(
                server_name=server_name_from_request,
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
            server_name_from_request = data['server_name']

            # IPMI Chassis power reset
            results = inventory_ipmi_chassis_power_control.start_inventory_ipmi_chassis_power_control(
                server_name=server_name_from_request,
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
            server_name_from_request = data['server_name']

            # IPMI Chassis power cycle
            results = inventory_ipmi_chassis_power_control.start_inventory_ipmi_chassis_power_control(
                server_name=server_name_from_request,
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
            server_name_from_request = data['server_name']

            # IPMI Chassis OS shutdown
            results = inventory_ipmi_chassis_power_control.start_inventory_ipmi_chassis_power_control(
                server_name=server_name_from_request,
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
            server_name_from_request = data['server_name']

            # IPMI Chassis get power status
            results = inventory_ipmi_chassis_power_status.start_inventory_ipmi_chassis_power_status(
                server_name=server_name_from_request
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
            server_name_from_request = data['server_name']

            # IPMI get network info
            results = inventory_ipmi_network_bmcinfo.start_inventory_ipmi_network_bmcinfo(
                server_name=server_name_from_request
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
            server_name_from_request = data['server_name']

            # IPMI get network bmc mac address
            results = inventory_ipmi_network_bmcinfo_macaddress.start_inventory_ipmi_network_bmcinfo_macaddress(
                server_name=server_name_from_request
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
            server_name_from_request = data['server_name']

            # IPMI get network eth0 mac address
            results = inventory_ipmi_network_eth0info_macaddress.start_inventory_ipmi_network_eth0info_macaddress(
                server_name=server_name_from_request
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
            server_name_from_request = data['server_name']
            boot_option_from_request = data['boot_option']
            persist_option_from_request = data['persist']
            uefiboot_option_from_request = data['uefiboot']

            # IPMI Set boot
            results = inventory_ipmi_boot_setnextboot.start_inventory_ipmi_boot_setnextboot(
                server_name=server_name_from_request,
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
            server_name_from_request = data['server_name']
            boot_option_from_request = data['boot_option']

            # IPMI boot immediate
            results = inventory_ipmi_boot_immediate.start_inventory_ipmi_boot_immediate(
                server_name=server_name_from_request,
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
            server_name_from_request = data['server_name']
            uid_from_request = data['uid']
            mode_from_request = data['mode']

            # Password field is optional, let's check if it's in the request
            password_from_request = None
            try:
                password_from_request = data['password']
            except:
                pass

            # IPMI users control
            results = inventory_ipmi_users_control.start_inventory_ipmi_users_control(
                server_name=server_name_from_request,
                uid=uid_from_request,
                mode=mode_from_request,
                password=password_from_request
            )

            # If Ok, return the results
            return HttpResponse(results, content_type="application/json")

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")
