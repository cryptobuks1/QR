from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from database import *
import datetime
from database.PDF_QR import *
from database.mail import *
# import datetime
import time


# ============================================================================
#                                Admin work
# =============================================================================
@csrf_exempt
def adminlogin(request):
    if 'admin' not in request.session:
        if request.method == 'POST':
            Email = request.POST['Email']
            password = request.POST['password']
            query = "SELECT * FROM `admin` WHERE `email`='{}' and `password`='{}'".format(Email, password)
            result = Fetchall(query)
            print(result)
            if result and result != 'INVALID QUERY':
                request.session['admin'] = result[0]
                print(request.session['admin'])
                return redirect(dashBoard)
            else:
                return render(request, 'adminlogin.html', {'result': 'not'})
        return render(request, 'adminlogin.html')
    else:
        return redirect(dashBoard)


def dashBoard(request):
    if 'admin' in request.session:
        return render(request, 'adminDashboard.html')
    else:
        return redirect(adminlogin)


def logoutamin(request):
    try:
        del request.session['admin']
    except:
        pass
    return redirect(adminlogin)


@csrf_exempt
def addNews(request):
    if 'admin' not in request.session:
        return redirect(adminlogin)

    if request.method == 'POST':
        today = datetime.date.today()
        title = request.POST['title']
        title = title.replace("'", '789qwe')
        title = title.replace('"', '987ewq')
        discription = request.POST['discription']
        discription = discription.replace("'", '789qwe')
        discription = discription.replace('"', '987ewq')
        query = "INSERT INTO `news`(`title`, `description`, `dateofnews`) VALUES ('{}','{}','{}')".format(title,
                                                                                                          discription,
                                                                                                          today)
        print(query)
        result = Insert(query)
        return render(request, 'addNews.html', {'result': result})
    return render(request, 'addNews.html')


def viewnews(request):
    if 'admin' not in request.session:
        return redirect(adminlogin)

    query = "SELECT * FROM `news`"
    result = Fetchall(query)
    data = []
    for row in result:
        dist = {
            'id': row[0],
            'title': row[1],
            'dataOfNews': row[3],
        }
        data.append(dist)
    return render(request, 'viewNews.html', {'data': data})


def deleteNews(request):
    if 'admin' not in request.session:
        return redirect(adminlogin)

    id = request.GET['id']
    query = "DELETE FROM `news` WHERE `newsid`='{}'".format(id)
    result = Delete(query)
    return redirect(viewnews)


def viewdescription(request):
    if 'admin' not in request.session:
        return redirect(adminlogin)

    id = request.GET['id']
    query = "SELECT `description` FROM `news` WHERE `newsid`='{}'".format(id)
    print(query)
    result = Fetchone(query)
    discription = result[0].replace('789qwe', "'")
    discription = discription.replace('987ewq', '"')
    return JsonResponse({'data': discription}, safe=False)


def addDepartments(request):
    if 'admin' not in request.session:
        return redirect(adminlogin)

    if request.method == 'POST':
        name = request.POST['Dname']
        location = request.POST['location']
        query1 = "select * from `departments` where `Dname`='{}'".format(name)
        result1 = Fetchall(query1)
        if result1:
            return render(request, 'addDepartments.html', {'result': 'no'})
        else:
            query = "INSERT INTO `departments`(`Dname`, `location`) VALUES ('{}','{}')".format(name.upper(), location)
            result = Insert(query)
            return render(request, 'addDepartments.html', {'result': result})
    return render(request, 'addDepartments.html')


def viewDepartments(request):
    if 'admin' not in request.session:
        return redirect(adminlogin)

    query1 = "select * from `departments`"
    result1 = Fetchall(query1)
    print(result1)
    data = []
    count = 1
    if result1 and result1 != "INVALID QUERY":
        res = "found"
        for row in result1:
            dist = {
                'count': count,
                'id': row[0],
                'name': row[1],
                'location': row[2],
            }
            data.append(dist)
            count += 1
    else:
        res = "no"
    return render(request, 'viewDepartments.html', {'data': data, 'result': res})


def delDepartments(request):
    if 'admin' not in request.session:
        return redirect(adminlogin)

    id = request.GET['id']
    print(id)
    query = "DELETE FROM `departments` WHERE `Deptid`='{}'".format(id)
    result = Delete(query)
    return redirect(viewDepartments)


@csrf_exempt
def addentity(request):
    if 'admin' not in request.session:
        return redirect(adminlogin)

    timing = ['00:15', '00:30', '00:45', '01:00', '01:15', '01:30', '01:45', '02:00', '02:15', '02:30', '02:45',
              '03:00',
              '03:15',
              '03:30',
              '03:45',
              '04:00',
              '04:15',
              '04:30',
              '04:45',
              '05:00',
              '05:15',
              '05:30',
              '05:45',
              '06:00',
              '06:15',
              '06:30',
              '06:45',
              '07:00',
              '07:15',
              '07:30',
              '07:45',
              '08:00',
              '08:15',
              '08:30',
              '08:45',
              '09:00',
              '09:15',
              '09:30',
              '09:45',
              '10:00',
              '10:15',
              '10:30',
              '10:45',
              '11:00',
              '11:15',
              '11:30',
              '11:45',
              '12:00',
              '12:15',
              '12:30',
              '12:45',
              '13:00',
              '13:15',
              '13:30',
              '13:45',
              '14:00',
              '14:15',
              '14:30',
              '14:45',
              '15:00',
              '15:15',
              '15:30',
              '15:45',
              '16:00',
              '16:15',
              '16:30',
              '16:45',
              '17:00',
              '17:15',
              '17:30',
              '17:45',
              '18:00',
              '18:15',
              '18:30',
              '18:45',
              '19:00',
              '19:15',
              '19:30',
              '19:45',
              '20:00',
              '20:15',
              '20:30',
              '20:45',
              '21:00',
              '21:15',
              '21:30',
              '21:45',
              '22:00',
              '22:15',
              '22:30',
              '22:45',
              '23:00',
              '23:15',
              '23:30',
              '23:45',
              '24:00']
    query = "SELECT * FROM `departments`"
    result = Fetchall(query)
    data = []
    for row in result:
        dist = {
            'id': row[0],
            'name': row[1],
        }
        data.append(dist)

    if request.method == 'POST':
        name = request.POST['name']
        fathername = request.POST['fathername']
        designation = request.POST['designation']
        type = request.POST['type']
        departments = request.POST['departments']
        status = request.POST['status']
        startTime = request.POST['startTime']
        endTime = request.POST['endTime']
        photo = request.FILES['photo']
        password = request.POST['password']
        email = request.POST['email']

        fs = FileSystemStorage()
        filename = fs.save("entity/" + photo.name, photo)
        query = "INSERT INTO `entity`(`name`, `fathername`, `Designation`, `Starttime`, `Endtime`, `coverphoto`, `typeofentry`, `Deptid`, `Status`,`email` ,`password`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
            name, fathername, designation, startTime, endTime, filename, type, departments, status, email, password)
        print(query)
        result = Insert(query)

        query2 = "select `Entityid` from `entity` ORDER BY `Entityid` DESC"
        result2 = Fetchone(query2)
        if result != 'INVALID QUERY':
            pdffilename = QR_and_PDF(result2[0], name, fathername, designation)
            query3 = "UPDATE `entity` SET `pdf`='{}' WHERE `Entityid`='{}'".format(pdffilename, result2[0])
            resul3 = Update(query3)
        print(result)
        return render(request, 'addentity.html', {'timing': timing, 'data': data, 'result': result})
    return render(request, 'addentity.html', {'timing': timing, 'data': data})


def viewEntity(request):
    if 'admin' not in request.session:
        return redirect(adminlogin)
    query = "SELECT * FROM `entity` INNER JOIN `departments` on `entity`.`Deptid`=`departments`.`Deptid`"
    result = Fetchall(query)
    # print(result)
    data = []
    for row in result:
        dist = {
            'id': row[0],
            'name': row[1],
            'fatherName': row[2],
            'dsignation': row[3],
            'startTime': row[4],
            'endTime': row[5],
            'photo': row[6],
            'type': row[7],
            'status': row[9],
            'email': row[10],
            'password': row[11],
            'pdf': row[12],
            'depId': row[8],
        }
        data.append(dist)
    return render(request, 'viewEntity.html', {'data': data})


def grantandRevokeEntity(request):
    id = request.GET['id']
    status = request.GET['status']
    query = "UPDATE `entity` SET `Status`='{}' WHERE `Entityid`='{}'".format(status, id)
    result = Update(query)
    return redirect(viewEntity)


def deleteEntity(request):
    id = request.GET['id']
    query = "DELETE FROM `entity` WHERE `Entityid`='{}'".format(id)
    result = Delete(query)
    return redirect(viewEntity)


def sendmailpdf(request):
    id = request.GET['id']
    query = "select email,pdf from `entity` where `Entityid`='{}'".format(id)
    result = Fetchone(query)
    print("--------->", result[0], id, result[1])
    try:
        mailwithAttachemnt(result[0], id, result[1])
    except:
        return HttpResponse('Network Prob')
    return redirect(viewEntity)


def viewEditEntity(request):
    if 'admin' not in request.session:
        return redirect(adminlogin)
    id = request.GET['id']
    timing = ['00:15', '00:30', '00:45', '01:00', '01:15', '01:30', '01:45', '02:00', '02:15', '02:30', '02:45',
              '03:00',
              '03:15',
              '03:30',
              '03:45',
              '04:00',
              '04:15',
              '04:30',
              '04:45',
              '05:00',
              '05:15',
              '05:30',
              '05:45',
              '06:00',
              '06:15',
              '06:30',
              '06:45',
              '07:00',
              '07:15',
              '07:30',
              '07:45',
              '08:00',
              '08:15',
              '08:30',
              '08:45',
              '09:00',
              '09:15',
              '09:30',
              '09:45',
              '10:00',
              '10:15',
              '10:30',
              '10:45',
              '11:00',
              '11:15',
              '11:30',
              '11:45',
              '12:00',
              '12:15',
              '12:30',
              '12:45',
              '13:00',
              '13:15',
              '13:30',
              '13:45',
              '14:00',
              '14:15',
              '14:30',
              '14:45',
              '15:00',
              '15:15',
              '15:30',
              '15:45',
              '16:00',
              '16:15',
              '16:30',
              '16:45',
              '17:00',
              '17:15',
              '17:30',
              '17:45',
              '18:00',
              '18:15',
              '18:30',
              '18:45',
              '19:00',
              '19:15',
              '19:30',
              '19:45',
              '20:00',
              '20:15',
              '20:30',
              '20:45',
              '21:00',
              '21:15',
              '21:30',
              '21:45',
              '22:00',
              '22:15',
              '22:30',
              '22:45',
              '23:00',
              '23:15',
              '23:30',
              '23:45',
              '24:00']
    query = "SELECT * FROM `departments`"
    result = Fetchall(query)
    data = []
    for row in result:
        dist = {
            'id': row[0],
            'name': row[1],
        }
        data.append(dist)
    query1 = "SELECT * FROM `entity` WHERE `Entityid`='{}'".format(id)
    result1 = Fetchone(query1)
    data1 = {
        'id': result1[0],
        'name': result1[1],
        'fathername': result1[2],
        'deg': result1[3],
        'startTime': result1[4],
        'endTime': result1[5],
        'photo': result1[6],
        'type': result1[7],
        'dip': result1[8],
        'status': result1[9],
        'email': result1[10],
        'password': result1[11],
        'pdf': result1[12],
    }
    return render(request, 'viewEditEntity.html', {'timing': timing, 'data': data, 'data1': data1})


@csrf_exempt
def viewEditEntityAction(request):
    if 'admin' not in request.session:
        return redirect(adminlogin)
    id = request.POST['id']
    name = request.POST['name']
    fathername = request.POST['fathername']
    designation = request.POST['designation']
    type = request.POST['type']
    departments = request.POST['departments']
    status = request.POST['status']
    startTime = request.POST['startTime']
    endTime = request.POST['endTime']
    password = request.POST['password']
    email = request.POST['email']

    try:
        photo = request.FILES['photo']
        if photo != "":
            fs = FileSystemStorage()
            filename = fs.save("entity/" + photo.name, photo)
            photoname = ",`coverphoto`='{}'".format(filename)
        else:
            photoname = ""
    except:
        photoname = ""
    pdffilename = QR_and_PDF(id, name, fathername, designation)
    query = "UPDATE `entity` SET `name`='{}',`fathername`='{}',`Designation`='{}',`Starttime`='{}',`Endtime`='{}'{},`typeofentry`='{}',`Deptid`='{}',`Status`='{}',`email`='{}',`password`='{}',`pdf`='{}' WHERE `Entityid`='{}'".format(
        name, fathername, designation, startTime, endTime, photoname, type, departments, status, email, password,
        pdffilename, id)
    print(query)
    result = Update(query)
    return redirect(viewEntity)


@csrf_exempt
def addVehicle(request):
    if 'admin' not in request.session:
        return redirect(adminlogin)
    id = request.GET['id']
    timing = ['00:15', '00:30', '00:45', '01:00', '01:15', '01:30', '01:45', '02:00', '02:15', '02:30', '02:45',
              '03:00',
              '03:15',
              '03:30',
              '03:45',
              '04:00',
              '04:15',
              '04:30',
              '04:45',
              '05:00',
              '05:15',
              '05:30',
              '05:45',
              '06:00',
              '06:15',
              '06:30',
              '06:45',
              '07:00',
              '07:15',
              '07:30',
              '07:45',
              '08:00',
              '08:15',
              '08:30',
              '08:45',
              '09:00',
              '09:15',
              '09:30',
              '09:45',
              '10:00',
              '10:15',
              '10:30',
              '10:45',
              '11:00',
              '11:15',
              '11:30',
              '11:45',
              '12:00',
              '12:15',
              '12:30',
              '12:45',
              '13:00',
              '13:15',
              '13:30',
              '13:45',
              '14:00',
              '14:15',
              '14:30',
              '14:45',
              '15:00',
              '15:15',
              '15:30',
              '15:45',
              '16:00',
              '16:15',
              '16:30',
              '16:45',
              '17:00',
              '17:15',
              '17:30',
              '17:45',
              '18:00',
              '18:15',
              '18:30',
              '18:45',
              '19:00',
              '19:15',
              '19:30',
              '19:45',
              '20:00',
              '20:15',
              '20:30',
              '20:45',
              '21:00',
              '21:15',
              '21:30',
              '21:45',
              '22:00',
              '22:15',
              '22:30',
              '22:45',
              '23:00',
              '23:15',
              '23:30',
              '23:45',
              '24:00']
    query = "select * from `Vehicles` where `Entityid`='{}'".format(id)
    result1 = Fetchall(query)
    listdata = []
    if result1:
        for row in result1:
            dist = {
                'id': row[0],
                'Stickered': row[1],
                'vnumber': row[2],
                'startTime': row[3],
                'endTime': row[4],
                'eid': row[5],
                'status': row[6],
            }
            listdata.append(dist)

    if request.method == 'POST':
        id = request.POST['id']
        vnumber = request.POST['vehiclenumber']
        Starttime = request.POST['Starttime']
        Endtime = request.POST['Endtime']
        Status = request.POST['Status']
        sticket = QR(id, vnumber)
        query = "INSERT INTO `Vehicles`(`Stickered`, `vehiclenumber`, `Starttime`, `Endtime`, `Entityid`, `Status`) VALUES ('{}','{}','{}','{}','{}','{}')".format(
            sticket, vnumber, Starttime, Endtime, id, Status)
        result = Insert(query)
        return render(request, 'addVehicle.html', {'id': id, 'timing': timing, 'result': result, 'listdata': listdata})
    return render(request, 'addVehicle.html', {'id': id, 'timing': timing, 'listdata': listdata})


def vehicleGrant(request):
    if 'admin' not in request.session:
        return redirect(adminlogin)
    eid = request.GET['eid']
    vid = request.GET['vid']
    status = request.GET['status']
    query = "UPDATE `Vehicles` SET `Status`='{}' WHERE `Vehicleid`='{}'".format(status, vid)
    result = Update(query)
    # print(result)
    return HttpResponseRedirect('addVehicle?id=' + eid)


def deleteVehiclePass(request):
    vid = request.GET['vid']
    eid = request.GET['eid']
    vpage = request.GET['page']
    query = "DELETE FROM `Vehicles` WHERE `Vehicleid`='{}'".format(vid)
    result = Delete(query)
    print(result)
    if vpage == 'vpage':
        return HttpResponseRedirect('allVehicle')
    return HttpResponseRedirect('addVehicle?id=' + eid)


def allVehicle(request):
    if 'admin' not in request.session:
        return redirect(adminlogin)
    query = "SELECT * FROM `QR`.`Vehicles` INNER JOIN `entity` on `Vehicles`.`Entityid`=`entity`.`Entityid`"
    result = Fetchall(query)
    dist = []
    for row in result:
        d = {
            'vid': row[0],
            'stickered': row[1],
            'vNumber': row[2],
            'startTime': row[3],
            'endtTime': row[4],
            'eid': row[5],
            'status': row[6],
            'name': row[8],
        }
        dist.append(d)
    return render(request, 'allVehicles.html', {'data': dist})


def printQR(request):
    vid = request.GET['vid']
    query = "SELECT * FROM `Vehicles` WHERE `Vehicleid`='{}'".format(vid)
    result = Fetchone(query)
    return render(request, 'printQR.html', {'result': result})


def allEnteryEntered(request):
    if 'admin' not in request.session:
        return redirect(adminlogin)
    query = "SELECT * FROM `Entity_entry` INNER JOIN `entity` on `Entity_entry`.`Entityid`=`entity`.`Entityid`"
    result = Fetchall(query)
    data = []
    for row in result:
        dist = {
            'Eid': row[0],
            'Entityid': row[1],
            'DateofEntery': str(row[2]),
            'TimeofEntery': (row[3]),
            'DateofExit': (row[5]),
            'TimeofExit': (row[4]),
            'name': row[8],
        }
        data.append(dist)
    print(data)
    return render(request, 'allEnteryEntered.html', {'data': data})


def allEnteryVehicle(request):
    if 'admin' not in request.session:
        return redirect(adminlogin)
    query = "SELECT * FROM `Vehicle_Entry` INNER JOIN `Vehicles` on `Vehicles`.`Vehicleid`=`Vehicle_Entry`.`Vehicleid`"
    result = Fetchall(query)
    data = []
    for row in result:
        dist = {
            'E_id': row[0],
            'V_id': row[1],
            'EnterTime': row[2],
            'Enterdate': row[4],
            'exitTime': row[3],
            'exitdate': row[5],
            'vnumber': row[8],
        }
        data.append(dist)
    return render(request, 'allEnteryVehicle.html', {'data': data})


# ========================================================================
#                       end of admin work
# ==========================================================================


def entityEntery(request):
    return render(request, 'entityEntery.html')


@csrf_exempt
def addentityEntery(request):
    qrdata = request.POST['qrdata']
    print(qrdata)
    qdata = qrdata.split(",")
    query = "SELECT `Entityid`,`name` FROM `entity` WHERE `Entityid`='{}' AND `name`='{}' and `Status`='Grant'".format(
        qdata[0], qdata[1])
    result = Fetchone(query)
    qrdate = datetime.date.today()
    qu = time.asctime(time.localtime())
    qrtime = qu.split()[3]
    print("------->", result)
    if result and result != 'INVALID QUERY':
        query2 = "SELECT `Eeid`, `Entityid`, `Dateofentry`, `Timeofentry`, `Exittime`, `exitdate`, `remarks` FROM `Entity_entry` WHERE `Entityid`='{}' and `Dateofentry` is not NULL and `Exittime` is NULL".format(
            qdata[0])
        print(query2)
        result2 = Fetchone(query2)
        if result2:
            return HttpResponse('allready')
        else:
            query1 = "INSERT INTO `Entity_entry`(`Entityid`, `Dateofentry`, `Timeofentry`) VALUES ('{}','{}','{}')".format(
                qdata[0], qrdate, qrtime)
            result1 = Insert(query1)
            print(result1)
            print(query1)
            if result1 != "INVALID QUERY":
                final = qdata[1]
            else:
                final = "fail"
            return HttpResponse(final)
    else:
        return HttpResponse("not")


def exitEntery(request):
    return render(request, 'exitEntery.html')


@csrf_exempt
def exitenteryAction(request):
    qrdata = request.POST['qrdata']
    print(qrdata)
    qdata = qrdata.split(",")
    query = "SELECT `Entityid`,`name` FROM `entity` WHERE `Entityid`='{}' AND `name`='{}' and `Status`='Grant'".format(
        qdata[0], qdata[1])
    result = Fetchall(query)
    qrdate = datetime.date.today()
    qu = time.asctime(time.localtime())
    qrtime = qu.split()[3]
    print("------->", result)
    if result and result != 'INVALID QUERY':
        query2 = "SELECT `Eeid`, `Entityid`, `Dateofentry`, `Timeofentry`, `Exittime`, `exitdate`, `remarks` FROM `Entity_entry` WHERE `Entityid`='{}' and `Dateofentry` is not NULL and `Exittime` is NULL".format(
            qdata[0])
        print("------->", query2)
        result2 = Fetchall(query2)
        print("######-->", result2)
        if result2:
            query1 = "UPDATE `Entity_entry` SET `Exittime`='{2}',`exitdate`='{1}' WHERE `Entityid`='{0}'".format(
                qdata[0], qrdate, qrtime)
            result1 = Insert(query1)
            print(result1)
            print(query1)
            if result1 != "INVALID QUERY":
                final = qdata[1]
            else:
                final = "fail"
            return HttpResponse(final)
        else:
            return HttpResponse('allready')
    else:
        return HttpResponse("not")


def enteryVehicle(request):
    return render(request, 'enterVehicle.html')


@csrf_exempt
def enteryVehicleAction(request):
    qrdata = request.POST['qrdata']
    qrdata = qrdata.split(",")
    print(qrdata)
    qrdate = datetime.date.today()
    qu = time.asctime(time.localtime())
    qrtime = qu.split()[3]
    query = "SELECT * FROM `Vehicles` WHERE `Entityid`='{}' and `Status`='Grant' and `vehiclenumber`='{}'".format(
        qrdata[0], qrdata[1])
    # print(query)
    result = Fetchall(query)
    if result and result != 'INVALID QUERY':
        query = "SELECT * FROM `Vehicles` INNER JOIN `Vehicle_Entry` ON `Vehicles`.`Vehicleid`=`Vehicle_Entry`.`Vehicleid` WHERE  `Vehicles`.`Entityid`='{}' and `Vehicles`.`Status`='Grant' and `Vehicles`.`vehiclenumber`='{}' and `Vehicle_Entry`.`Entrytime` is not  NULL and `Vehicle_Entry`.`dateofexit` is NULL".format(
            qrdata[0], qrdata[1])
        print(query)
        result2 = Fetchall(query)
        print(result2)
        if result2:
            result = 'allready'
        else:
            query = "INSERT INTO `Vehicle_Entry`(`Vehicleid`, `Entrytime`,  `Dateofentry`) VALUES ('{}','{}','{}')".format(
                result[0][0], qrtime, qrdate)
            print(query)
            result = Insert(query)
            result = qrdata[1]


    else:
        result = "notGrant"
    return HttpResponse(result)


def ExitVehicle(request):
    return render(request, 'exitVehicle.html')


@csrf_exempt
def exitVehicleAction(request):
    qrdata = request.POST['qrdata']
    qrdata = qrdata.split(",")
    print(qrdata)
    qrdate = datetime.date.today()
    qu = time.asctime(time.localtime())
    qrtime = qu.split()[3]
    query = "SELECT * FROM `Vehicles` WHERE `Entityid`='{}' and `Status`='Grant' and `vehiclenumber`='{}'".format(
        qrdata[0], qrdata[1])
    print(query)
    result = Fetchall(query)
    if result and result != 'INVALID QUERY':
        query = "SELECT * FROM `Vehicles` INNER JOIN `Vehicle_Entry` ON `Vehicles`.`Vehicleid`=`Vehicle_Entry`.`Vehicleid` WHERE  `Vehicles`.`Entityid`='{}' and `Vehicles`.`Status`='Grant' and `Vehicles`.`vehiclenumber`='{}' and `Vehicle_Entry`.`Entrytime` is not  NULL and `Vehicle_Entry`.`dateofexit` is  NULL".format(
            qrdata[0], qrdata[1])
        print(query)
        result2 = Fetchone(query)
        print(result2)
        if result2:
            query = "UPDATE `Vehicle_Entry` SET `Exittime`='{}', `dateofexit`='{}' WHERE `Vehicleid`='{}'".format(
                qrtime, qrdate, result[0][0])
            print(query)
            result = Insert(query)
            result = qrdata[1]
        else:
            result = 'allready'

    else:
        result = "notGrant"
    return HttpResponse(result)


# def index1(request):
#     return render(request, 'index2.html')

def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


@csrf_exempt
def loginentery(request):
    id = request.POST['id']
    password = request.POST['password']
    query = "SELECT * FROM `entity` WHERE `Entityid`='{}' and `password`='{}'".format(id, password)
    print(query)
    result = Fetchall(query)
    print(result)

    if result and result != 'INVALID QUERY':
        query2 = "SELECT `Vehicleid` FROM `Vehicles` WHERE `Entityid`='{}'".format(id)
        result2 = Fetchone(query2)
        if result2:
            vno = result2[0]
        else:
            vno = 'NotFound'
        request.session['user'] = result
        return render(request, 'index.html', {'vno': vno})
    else:
        return render(request, 'index.html', {'invalid': 'invalid'})


def logoutuser(request):
    try:
        del request.session['user']
    except:
        pass
    return redirect(index)


def vdata(request):
    if 'user' not in request.session:
        return HttpResponseRedirect("/#login")
    else:
        id = request.GET['id']
        query = "SELECT * FROM `Vehicles` WHERE `Vehicleid`='{}'".format(id)
        print(query)
        result = Fetchall(query)
        print(result)
        dist = []
        if result:
            for row in result:
                d = {
                    'vid': row[0],
                    # 'stickered': row[1],
                    'vNumber': row[2],
                    'startTime': row[3],
                    'endtTime': row[4],
                    'eid': row[5],
                    'status': row[6],
                    # 'name': row[8],
                }
                dist.append(d)
            final = "Found"
        else:
            final = "notFound"
        return render(request, 'V_data.html', {'data': dist, 'final': final})


def edata(request):
    if 'user' not in request.session:
        return HttpResponseRedirect("/#login")
    else:
        id = request.GET['id']
        query = "SELECT * FROM `Entity_entry` WHERE `Entityid`='{}'".format(id)
        result = Fetchall(query)
        print(result)
        data = []
        if result:
            for row in result:
                dist = {
                    'Eid': row[0],
                    'Entityid': row[1],
                    'DateofEntery': str(row[2]),
                    'TimeofEntery': (row[3]),
                    'DateofExit': (row[5]),
                    'TimeofExit': (row[4]),
                }
                data.append(dist)
            final = "Found"
        else:
            final = "notFound"
        return render(request, 'e_data.html', {'data': data, 'final': final})
