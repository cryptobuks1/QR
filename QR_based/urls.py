"""QR_based URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from view import *
urlpatterns = [
    path('admin', adminlogin),
    path('dashBoard', dashBoard),
    path('logoutamin', logoutamin),

    path('addNews', addNews),
    path('viewnews', viewnews),
    path('deleteNews', deleteNews),
    path('viewdescription', viewdescription),

    path('addDepartments', addDepartments),
    path('viewDepartments', viewDepartments),
    path('delDepartments', delDepartments),

    path('addentity', addentity),
    path('viewEntity', viewEntity),
    path('grantandRevokeEntity', grantandRevokeEntity),
    path('deleteEntity', deleteEntity),
    path('sendmailpdf', sendmailpdf),
    path('viewEditEntity', viewEditEntity),
    path('viewEditEntityAction', viewEditEntityAction),
    path('addVehicle', addVehicle),
    path('vehicleGrant', vehicleGrant),
    path('deleteVehiclePass', deleteVehiclePass),
    path('allVehicle', allVehicle),
    path('printQR', printQR),
    path('allEnteryEntered', allEnteryEntered),
    path('allEnteryVehicle', allEnteryVehicle),


    # path('', index1),
    path('', index),
    path('entityEntery', entityEntery),
    path('addentityEntery', addentityEntery),
    path('exitEntery', exitEntery),
    path('exitenteryAction', exitenteryAction),
    path('enteryVehicle', enteryVehicle),
    path('enteryVehicleAction', enteryVehicleAction),
    path('ExitVehicle', ExitVehicle),
    path('exitVehicleAction', exitVehicleAction),
    path('contact', contact),
    path('loginentery', loginentery),
    path('logoutuser', logoutuser),
    path('vdata', vdata),
    path('edata', edata),
]
