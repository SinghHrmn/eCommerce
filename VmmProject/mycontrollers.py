from django.shortcuts import *
from django.http import *
from connectionfile import *
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import *
from datetime import *
import http.client
import smtplib

CARTLIST = []
list1 = []

def updatedata(request):
    r1 = request.GET["d1"]
    r2 = request.GET["d2"]
    r3 = request.GET["d3"]

    global list1
    list1 = []
    list1.append(r1)
    list1.append(r2)
    list1.append(r3)


    return HttpResponse("<h1>Data recieved</h1>")
def updated(request):
    global list1
    s = ""
    for x in list1:
        s += x
    return HttpResponse(s)

def addAdmin(request):
    return render(request, "adminAdd.html")


def addAdminAction(request):
    conn = connection.connection('')
    query = "insert into admin VALUE('" + request.GET["fullName"] + "','" + request.GET["email"] + \
            "','" + request.GET["password"] + "','" + request.GET["userType"] + "')"
    cr = conn.cursor()
    result = cr.execute(query)
    conn.commit()
    d = {}
    if result:
        d["msg"] = "User Added Successfully"
    else:
        d["msg"] = "Error Adding User"
    return JsonResponse(d)


def viewAdmin(request):
    return render(request, "adminView.html")


def viewAdminAction(request):
    conn = connection.connection('')
    query = "select * from admin"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    x = []
    for p in result:
        d = {}
        d["fullName"] = p[0]
        d["email"] = p[1]
        d["password"] = p[2]
        d["userType"] = p[3]
        d["deletelink"] = "delete-admin-action?email=" + p[1]
        d["editlink"] = "edit-admin?email=" + p[1]
        x.append(d)

    return JsonResponse(x, safe=False)


def editAdmin(request):
    conn = connection.connection('')
    query = "select * from admin where email='" + request.GET["email"] + "'"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchone()
    d = {}
    d["fullName"] = result[0]
    d["email"] = result[1]
    d["password"] = result[2]

    return render(request, "adminEdit.html", d)


def editAdminAction(request):
    conn = connection.connection('')
    query = "select * from admin"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    x = []
    for p in result:
        d = {}
        d["fullName"] = p[0]
        d["email"] = p[1]
        d["password"] = p[2]
        d["userType"] = p[3]
        d["deletelink"] = "delete-admin-action?email=" + p[1]
        d["editlink"] = "edit-admin-action?email=" + p[1]
        x.append(d)

    return JsonResponse(x, safe=False)


def saveAdmin(request):
    conn = connection.connection('')
    query = "update admin set fullName='" + request.GET["fullName"] + "',password='" + request.GET["password"] \
            + "',userType='" + request.GET["userType"] + "' where email='" + request.GET["email"] + "'"
    cr = conn.cursor()
    cr.execute(query)
    conn.commit()
    return HttpResponseRedirect("view-admin")


def deleteAdminAction(request):
    conn = connection.connection('')
    query = "delete from admin where email='" + request.GET["email"] + "'"
    cr = conn.cursor()
    cr.execute(query)
    conn.commit()

    return HttpResponseRedirect("view-admin")


def addCategory(request):
    return render(request, "categoryAdd.html")


def addCategoryAction(request):
    conn = connection.connection('')
    query = "insert into categorytable VALUE ('" + request.GET["categoryName"] + "','" + request.GET[
        "description"] + "')"
    cr = conn.cursor()
    result = cr.execute(query)
    conn.commit()
    d = {}
    if result:
        d["msg"] = "Category Added Successfully"
    else:
        d["msg"] = "Error Adding Category"
    return JsonResponse(d)


def viewCategory(request):
    return render(request, "categoryView.html")


def viewCategoryAction(request):
    conn = connection.connection('')
    query = "select * from categorytable"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    x = []
    for p in result:
        d = {}
        d["categoryName"] = p[0]
        d["description"] = p[1]
        d["deletelink"] = "delete-category-action?categoryName=" + p[0]
        d["editlink"] = "edit-category?categoryName=" + p[0]
        x.append(d)

    return JsonResponse(x, safe=False)


def editCategory(request):
    conn = connection.connection('')
    query = "select * from categorytable where categoryName='" + request.GET["categoryName"] + "'"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchone()
    d = {}
    d["categoryName"] = result[0]
    d["description"] = result[1]

    return render(request, "categoryEdit.html", d)


def editCategoryAction(request):
    conn = connection.connection('')
    query = "select * from categorytable"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    x = []
    for p in result:
        d = {}
        d["categoryName"] = p[0]
        d["description"] = p[1]
        d["deletelink"] = "delete-category-action?categoryName=" + p[0]
        d["editlink"] = "edit-category-action?categoryName=" + p[0]
        x.append(d)

    return JsonResponse(x, safe=False)


def saveCategory(request):
    conn = connect("127.0.0.1", "root", '', "project")
    query = "update categorytable set description='" + request.GET["description"] + "' where categoryName='" + \
            request.GET["categoryName"] + "'"
    cr = conn.cursor()
    cr.execute(query)
    conn.commit()
    return HttpResponseRedirect("view-category")


def deleteCategoryAction(request):
    conn = connection.connection('')
    query = "delete from categorytable where categoryName='" + request.GET["categoryName"] + "'"
    cr = conn.cursor()
    cr.execute(query)
    conn.commit()

    return HttpResponseRedirect("view-category")


def userSignup(request):
    return render(request, "signUp.html")


def userSignupAction(request):
    conn = connection.connection('')
    query = "insert into usersignup VALUES ('" + request.GET["fullName"] + "','" + request.GET["mobileNo"] + "','" + \
            request.GET["address"] + "','" + request.GET["city"] + "','" + request.GET["email"] + "','" + request.GET[
                "password"] + "')"
    cr = conn.cursor()
    result = cr.execute(query)
    conn.commit()
    d = {}
    if result:
        d["msg"] = "Signup Successful"
    else:
        d["msg"] = "Error during Signup"
    return JsonResponse(d)


def addProduct(request):
    conn = connection.connection('')
    query = "select * from categorytable"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    x = []
    for p in result:
        d = {}
        d["categoryName"] = p[0]
        x.append(d)

    return render(request, "productAdd.html", {"mydata": x})


@csrf_exempt
def addProductAction(request):
    conn = connection.connection('')
    cr = conn.cursor()
    categoryName = request.POST['categoryName']
    productName = request.POST['productName']
    price = request.POST['price']
    mrp = request.POST['mrp']
    description = request.POST['description']
    photo = request.FILES['photo']
    fs = FileSystemStorage()
    filename = fs.save(photo.name, photo)
    location = fs.url(filename)
    query = "insert into producttable VALUES (NULL ,'" + productName + "','" + price + "','" + mrp + "','" + description + "','" + filename + "','" + categoryName + "')"
    result = cr.execute(query)
    conn.commit()
    conn.close()
    d = {}
    if result:
        d["msg"] = "Data Saved"
    else:
        d["msg"] = "Data Not Saved: ERROR"

    return JsonResponse(d, safe=False)


def viewProduct(request):
    return render(request, "productView.html")


def viewProductAction(request):
    conn = connection.connection('')
    query = "select * from producttable"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    x = []
    for p in result:
        d = {}
        d["pid"] = p[0]
        d["pname"] = p[1]
        d["price"] = p[2]
        d["mrp"] = p[3]
        d["photo"] = p[5]
        d["description"] = p[4]
        d["categoryName"] = p[6]
        d["deletelink"] = "delete-product-action?id=" + str(p[0])
        d["editlink"] = "edit-product-action?id=" + str(p[0])
        x.append(d)
    return JsonResponse(x, safe=False)


def deleteProductAction(request):
    conn = connection.connection('')
    query = "delete from producttable where pid='" + request.GET["id"] + "'"
    cr = conn.cursor()
    cr.execute(query)
    conn.commit()

    return HttpResponseRedirect("view-product")


def viewAllProducts(request):
    return render(request, "productShowAll.html")


def viewAllProductsAction(request):
    conn = connection.connection('')
    query = "select * from producttable"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    x = []
    for p in result:
        d = {}
        d["pid"] = p[0]
        d["pname"] = p[1]
        d["price"] = p[2]
        d["mrp"] = p[3]
        d["photo"] = p[5]
        d["description"] = p[4]
        d["categoryName"] = p[6]
        x.append(d)
    return JsonResponse(x, safe=False)


def addtoCartAction(request):
    global CARTLIST
    conn = connection.connection('')
    pid = request.GET['pid']
    qty = request.GET['qty']
    query = "select * from producttable where pid='" + str(pid) + "'"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    for p in result:
        d = {}
        d["pid"] = p[0]
        d["pname"] = p[1]
        d["price"] = p[2]
        d["mrp"] = p[3]
        d["photo"] = p[5]
        d["description"] = p[4]
        d["categoryName"] = p[6]
        d['qty'] = qty
        d['total'] = float(p[2]) * float(qty)
        CARTLIST.append(d)
    request.session['MYCART'] = CARTLIST
    return JsonResponse(CARTLIST, safe=False)

def testfile(request):
    return render(request, 'file_test.html')

def myCart(request):
    return render(request, 'myCart.html')


def myCartAction(request):
    if request.session.has_key('MYCART'):
        return JsonResponse(request.session['MYCART'], safe=False)
    else:
        return JsonResponse([],safe=False)


def userLogin(request):
    return render(request, "userLogin.html")


@csrf_exempt
def userLoginAction(request):
    conn = connection.connection('')
    email = request.POST['email']
    password = request.POST['password']
    query = "select * from usersignup where email='" + email + "'"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    flag = False
    for p in result:
        if email == p[4] and password == p[5]:
            request.session['USEREMAIL'] = email
            flag = True
            break
    d = {}
    if flag == True:
        d['msg'] = "Login Success"
    else:
        d['msg'] = "Invalid Login"
    return JsonResponse(d,safe=False)


def proceedtoPay(request):
    d = {}
    if request.session.has_key('USEREMAIL'):
        conn = connection.connection('')
        email = request.session['USEREMAIL']
        query = "select * from usersignup where email='" + email + "'"
        cr = conn.cursor()
        cr.execute(query)
        result = cr.fetchall()
        for p in result:
            d["fullName"] = p[0]
            d["city"] = p[3]
            d["address"] = p[2]
            d["mobileNo"] = p[1]
        netamount = 0.0
        for p in request.session['MYCART']:
            netamount += p['total']
        d['netAmount'] = netamount
        d['fromcart'] = "billing"
        k = "billinfo.html"
    else:
        d['fromcart'] = "yes"
        k = "userLogin.html"
    return render(request,k,d)

def userHomePage(request):
    return render(request,"userHomePage.html")

def billinfo(request):
    conn = connection.connection('')
    email = request.session['USEREMAIL']
    query = "select * from usersignup where email='" + email + "'"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    d={}
    for p in result:
        d["fullName"]=p[0]
        d["city"]=p[3]
        d["address"]=p[2]
        d["mobileNo"]=p[1]
    netamount = 0.0
    for p in request.session['MYCART']:
        netamount += p['total']
    d['netAmount'] = netamount
    return render(request,"billinfo.html",d)


def logout(request):
    del request.session['USEREMAIL']
    if request.session.has_key('MYCART'):
        del request.session['MYCART']
    return HttpResponseRedirect("login")

@csrf_exempt
def checkoutaction(request):
    conn = connection.connection('')
    email = request.POST['email']
    fullName = request.POST['fullName']
    mobileNo = request.POST['mobileNo']
    address = request.POST['address']
    city = request.POST['city']
    netAmount = request.POST['netAmount']
    dt = datetime.now().date()
    paymentMethod = request.POST['paymentMode']
    query = "insert into ordertable values(null,'"+ email+"','"+fullName+"','"+str(mobileNo)+"','"+address+"','"+city+"','"+str(netAmount)+"','"+str(dt)+"','pending','"+paymentMethod+"')"
    cr = conn.cursor()
    cr.execute(query)
    conn.commit()
    orderid = cr.lastrowid
    ar = request.session['MYCART']
    for i in range(0,len(request.session['MYCART'])):
        query1 = "insert into orderdetail values(null,'" + str(orderid) + "','" + str(ar[i]["pid"]) + "','"+ ar[i]["pname"]+"','" + str(ar[i]["price"]) + "','" + str(ar[i]["qty"]) + "','" + str(ar[i]["total"]) + "')"
        cr1 = conn.cursor()
        cr1.execute(query1)
        conn.commit()
    conn.close()
    msg = fullName+"! Your Order has been placed for Rs." + str(
        netAmount) + " .Your order will be delivered after order approval. Thank You"
    msg = msg.replace(" ", "%20")
    conn1 = http.client.HTTPConnection("server1.vmm.education")
    conn1.request('GET',
                  "/VMMCloudMessaging/AWS_SMS_Sender?username=ExamSystem&password=S4J5LT3C&message=" + msg + "&phone_numbers=" + str(mobileNo))
    response = conn1.getresponse()
    print(response.read())
    sender = 'tania.vmmteachers23@gmail.com'
    receiver = email
    password = 'Teachers@123'
    try:
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(sender, password)
        body = "\nYour Order has been placed for Rs." + str(
            netAmount) + " .Your order will be delivered after order approval. Thank You\n\n"
        subject = "Subject:Django Shopping "
        msg = subject + body
        # msg='Subject:Demo <h1>This is a test e-mail message.</h1>'
        smtpserver.sendmail(sender, receiver, msg)
        print('Sent')
        smtpserver.close()
    except smtplib.SMTPException:
        print("Not Sent")
    d={}
    d["msg"]="Data Saved"
    return JsonResponse(d,safe=False)


def thankspage(request):
    return render(request,"thankspage.html")

def sorrypage(request):
    return HttpResponse("<h1>Sorry Payment failed</h1>")


def pendingorders(request):
    return render(request,"pendingOrders.html")


def pendingordersaction(request):
    conn = connection.connection('')
    query = "select * from ordertable where status='pending' ORDER BY id DESC "
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    conn.close()
    x = []
    for p in result:
        d = {}
        d['id'] = p[0]
        d['email'] = p[1]
        d['fullname'] = p[2]
        d['mobileno'] = p[3]
        d['address'] = p[4]
        d['city'] = p[5]
        d['netamount'] = p[6]
        d['dateoforder'] = p[7]
        d['paymentmode'] = p[9]
        x.append(d)
    return JsonResponse(x, safe=False)


def approve_reject_action(request):
    orderid = request.GET['orderid']
    status = request.GET['status']
    mobileno = request.GET['mobile']

    conn = connection.connection('')
    s = "update ordertable set status='" + status + "' where id='" + str(orderid) + "'"
    cr = conn.cursor()
    result = cr.execute(s)
    conn.commit()
    conn.close()
    if status == "Accepted":
        msg = "Status for your order with orderid "+str(orderid)+"has been changed to Accepted. Your order will be dispatched soon"
        msg = msg.replace(" ", "%20")
    else:
        msg = "Your order with orderid " + str(orderid) + "has been Rejected. Sorry for the inconvenience."
        msg = msg.replace(" ", "%20")

    conn1 = http.client.HTTPConnection("server1.vmm.education")
    conn1.request('GET',
                  "/VMMCloudMessaging/AWS_SMS_Sender?username=ExamSystem&password=S4J5LT3C&message=" + msg + "&phone_numbers=" + str(mobileno))
    response = conn1.getresponse()
    print(response.read())
    d = {}
    d['message'] = "Order Updated"
    return JsonResponse(d, safe=False)


def myorder(request):
    return render(request,"myOrders.html")

def myordersaction(request):
    email = request.GET['email']
    conn = connection.connection('')
    s = "select * from ordertable where email='"+email+"' order by id DESC"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    conn.close()
    x = []
    for p in result:
        d = {}
        d['id'] = p[0]
        d['email'] = p[1]
        d['fullname'] = p[2]
        d['mobileno'] = p[3]
        d['address'] = p[4]
        d['city'] = p[5]
        d['netamount'] = p[6]
        d['dateoforder'] = p[7]
        d['status'] = p[8]
        d['paymentmode'] = p[9]
        x.append(d)
    return JsonResponse(x, safe=False)

def index(request):
    return render(request,"template/base.html")
