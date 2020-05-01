from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from database import *
import datetime


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
            if result != 'INVALID QUERY':
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
    id = request.GET['id']
    query = "DELETE FROM `news` WHERE `newsid`='{}'".format(id)
    result = Delete(query)
    return redirect(viewnews)


def viewdescription(request):
    id = request.GET['id']
    query = "SELECT `description` FROM `news` WHERE `newsid`='{}'".format(id)
    print(query)
    result = Fetchone(query)
    discription = result[0].replace('789qwe', "'")
    discription = discription.replace('987ewq', '"')
    return JsonResponse({'data': discription}, safe=False)


def addDepartments(request):
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
    query1 = "select * from `departments`"
    result1 = Fetchall(query1)
    print(result1)
    data = []
    count = 1
    if result1 != "INVALID QUERY":
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
    id = request.GET['id']
    print(id)
    query = "DELETE FROM `departments` WHERE `Deptid`='{}'".format(id)
    result = Delete(query)
    return redirect(viewDepartments)


@csrf_exempt
def addentity(request):
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

        fs = FileSystemStorage()
        filename = fs.save("entity/"+photo.name, photo)
        query = "INSERT INTO `entity`(`name`, `fathername`, `Designation`, `Starttime`, `Endtime`, `coverphoto`, `typeofentry`, `Deptid`, `Status`, `password`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
            name, fathername, designation, startTime, endTime, filename, type, departments, status, password)
        print(query)
        result = Insert(query)
        print(result)
        return render(request, 'addentity.html', {'timing': timing, 'data': data, 'result': result})
    return render(request, 'addentity.html', {'timing': timing, 'data': data})

def viewEntity(request):
    query="SELECT * FROM `entity` INNER JOIN `departments` on `entity`.`Deptid`=`departments`.`Deptid`"
    result=Fetchall(query)
    data=[]
    for row in result:
        dist={
            'id':row[0],
            'name':row[1],
            'fatherName':row[2],
            'dsignation':row[3],
            'startTime':row[4],
            'endTime':row[5],
            'type':row[6],
            'dpid':row[7],
            'status':row[8],
            'password':row[9],
            'dName':row[11],
        }
        data.append(dist)
    return render(request,'viewEntity.html',{'data':data})
# ========================================================================
#                       end of admin work
# ==========================================================================
