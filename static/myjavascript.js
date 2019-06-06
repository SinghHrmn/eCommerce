function addadmin() {
    var fullName = document.getElementById('fullName').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('pass').value;
    var userType = document.getElementById('userType').value;

    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ar = JSON.parse(this.response);
            var s = "<div class='alert alert-success'><h3>" + ar["msg"] + "</h3></div>";
            document.getElementById("msg").innerHTML = s;
        }
    };
    xml.open("GET", "add-admin-action?fullName=" + fullName + "&email=" + email +
        "&password=" + password + "&userType=" + userType, true);
    xml.send();
};

function viewadmin() {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ar = JSON.parse(this.response)
            var s = "<table class='table table-hover'>";
            s += "<tr>";
            s += "<th>Full Name</th>";
            s += "<th>Email</th>";
            s += "<th>Password</th>";
            s += "<th>User Type</th>";
            s += "<th>Delete</th>";
            s += "<th>Edit</th>";
            s += "</tr>";
            for (var i = 0; i < ar.length; i++) {
                s += "<tr>";
                s += "<td>" + ar[i]["fullName"] + "</td>";
                s += "<td>" + ar[i]["email"] + "</td>";
                s += "<td>" + ar[i]["password"] + "</td>";
                s += "<td>" + ar[i]["userType"] + "</td>";
                s += "<td><a href='" + ar[i]["deletelink"] + "'><img src='../static/img/delete.png' style='width: 20px;height: 20px'></a></td>";
                s += "<td><a href='" + ar[i]["editlink"] + "'><img src='../static/img/edit.png' style='width: 20px;height: 20px'></a></td>";
                s += "</tr>";
            }
            s += "</table>";
            document.getElementById("table").innerHTML = s;
        }
    };
    xml.open("GET", "view-admin-action", true);
    xml.send();

};

function addcategory() {
    var categoryName = document.getElementById('categoryName').value;
    var description = document.getElementById('description').value;

    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ar = JSON.parse(this.response);
            var s = "<div class='alert alert-success'><h3>" + ar["msg"] + "</h3></div>";
            document.getElementById("msg").innerHTML = s;
        }
    };
    xml.open("GET", "add-category-action?categoryName=" + categoryName + "&description=" + description, true);
    xml.send();
};

function viewcategory() {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ar = JSON.parse(this.response)
            var s = "<table class='table table-hover'>";
            s += "<tr>";
            s += "<th>Category Name</th>";
            s += "<th>Description</th>";
            s += "<th>Delete</th>";
            s += "<th>Edit</th>";
            s += "</tr>";
            for (var i = 0; i < ar.length; i++) {
                s += "<tr>";
                s += "<td>" + ar[i]["categoryName"] + "</td>";
                s += "<td>" + ar[i]["description"] + "</td>";
                s += "<td><a href='" + ar[i]["deletelink"] + "'><img src='../static/img/delete.png' " +
                    "style='width: 20px;height: 20px'></a></td>";
                s += "<td><a href='" + ar[i]["editlink"] + "'><img src='../static/img/edit.png' " +
                    "style='width: 20px;height: 20px'></a></td>";
                s += "</tr>";
            }
            s += "</table>";
            document.getElementById("table").innerHTML = s;
        }
    }
    xml.open("GET", "view-category-action", true);
    xml.send();

}

function usersignup() {
    if ($("#frm_usersignup").valid()) {
        var fullName = document.getElementById('fullName').value;
        var mobileNo = document.getElementById('mobileNo').value;
        var address = document.getElementById('address').value;
        var city = document.getElementById('city').value;
        var email = document.getElementById('email').value;
        var password = document.getElementById('password').value;
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var ar = JSON.parse(this.response);
                var s = "<div class='jumbotron text-center'><h3>" + ar["msg"] + "</h3>";
                document.getElementById("msg").innerHTML = s;
            }
        };
        xml.open("GET", "user-signup-action?fullName=" + fullName + "&mobileNo=" + mobileNo + "&address=" + address +
            "&city=" + city + "&email=" + email + "&password=" + password, true);
        xml.send();
    }
}


function addproduct() {
    if ($("#frm_productAdd").valid()) {
        var formdata = new FormData();
        formdata.append('categoryName', document.getElementById('categoryName').value);
        formdata.append('productName', document.getElementById('productName').value);
        formdata.append('price', document.getElementById('price').value);
        formdata.append('mrp', document.getElementById('mrp').value);
        formdata.append('description', document.getElementById('description').value);
        formdata.append('photo', document.getElementById('photo').files[0]);
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var ar = JSON.parse(this.response);
                var s = "<div class='alert alert-success'><h3>" + ar["msg"] + "</h3></div>";
                document.getElementById("msg").innerHTML = s;
            }
        };
        xml.open("POST", "add-product-action", true);
        xml.send(formdata);
    }

}

function viewproduct() {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ar = JSON.parse(this.response)
            var s = "<table class='table table-hover'>";
            s += "<tr>";
            s += "<th>ID</th>";
            s += "<th>Product Name</th>";
            s += "<th>Product Category</th>";
            s += "<th>Price</th>";
            s += "<th>MRP</th>";
            s += "<th>Description</th>";
            s += "<th>Photo</th>";
            s += "<th>Delete</th>";
            s += "<th>Update</th>";
            s += "</tr>";
            for (var i = 0; i < ar.length; i++) {
                s += "<tr>";
                s += "<td>" + ar[i]["pid"] + "</td>";
                s += "<td>" + ar[i]["pname"] + "</td>";
                s += "<td>" + ar[i]["categoryName"] + "</td>";
                s += "<td>" + ar[i]["price"] + "</td>";
                s += "<td>" + ar[i]["mrp"] + "</td>";
                s += "<td>" + ar[i]["description"] + "</td>";
                s += "<td><img src='../static/media/" + ar[i]["photo"] + "' style='height: 100px;width: 100px' </td>";
                s += "<td class='text-center'><a href='" + ar[i]["deletelink"] + "'><img src='../static/img/delete.png' " +
                    "style='width: 20px;height: 20px'></a></td>";
                s += "<td class='text-center'><a href='" + ar[i]["editlink"] + "'><img src='../static/img/edit.png' " +
                    "style='width: 20px;height: 20px'></a></td>";
                s += "</tr>";
            }
            s += "</table>";
            document.getElementById("table").innerHTML = s;
        }

    };
    xml.open("GET", "view-product-action", true);
    xml.send();
}

function viewallproducts() {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ar = JSON.parse(this.response);
            var s = "<div class='row'>";
            for (var i = 0; i < ar.length; i++) {
                s += "<div class='col-md-3' style='padding:30px 30px 20px 30px;border: 0px solid'>";
                s += "<div class='col-md-12 mydiv1' style='background-color: white;padding: 5px 5px 5px 5px'>";
                s += "<img src='../static/media/" + ar[i]["photo"] + "' style='height:215px;width: 100%; padding:10px 10px 10px 10px'>";
                s += "<h4>" + ar[i]["pname"] + "</h4>";
                s += "<ins style='color:blue;margin:10px;'><strong>Rs." + ar[i]['price'] + "</strong></ins>";
                s += "<del style='color:red;margin:10px;'><strong>Rs." + ar[i]['mrp'] + "</strong></del>";
                s += "<p class='text-left' style='margin-top:12px'><button type='button' " +
                    "onclick='addtocart(" + ar[i]['pid'] + ")' class='btn btn-success'>Add To Cart</button></p>";
                s += "</div>";
                s += "</div>";
            }
            s += "</div>";
            document.getElementById('output').innerHTML = s;


        }
    };
    xml.open("GET", "view-allproduct-action", true);
    xml.send();
}
// $('.block2-btn-addcart').each(function(){
//     var nameProduct = $(this).parent().parent().parent().find('.block2-name').html();
//     var idProduct = $(this).parent().parent().parent().find('.block2-id').html();
//     $(this).on('click', function addtocart(pid) {
//         var qty = parseInt(document.getElementById('qty').value);
//         var formdata = new FormData();
//         formdata.append('id', pid);
//         formdata.append('qty', qty);
//         var xml = new XMLHttpRequest();
//         xml.onreadystatechange = function () {
//             if (this.readyState == 4 && this.status == 200) {
//                 var ar = JSON.parse(this.response);
//                 swal(nameProduct, "is added to cart !", "success");
//                 }
            
//         };
//         xml.open('POST', 'add-to-cart-action', true);
//         xml.send(formdata);

        
//     });
// });

function addtocart(pid) {
    var qty = parseInt(document.getElementById('qty').value);
    var formdata = new FormData();
    formdata.append('id', pid);
    formdata.append('qty', qty);
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ar = JSON.parse(this.response);
            alert("Product Added");
            swal(nameProduct, "is added to cart !", "success");
            
            }
            
        }
    xml.open('POST', 'add-to-cart-action', true);
    xml.send(formdata);

    };

function upgradeCartValue(pid){
    var formdata = new FormData();
    formdata.append('id', pid);
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ar = JSON.parse(this.response);
            window.location.href = "viewcart";
            
            }
            
        }
    xml.open('POST', 'upgrade-cart-action', true);
    xml.send(formdata);

}

function downgradeCartValue(pid){
    var formdata = new FormData();
    formdata.append('id', pid);
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ar = JSON.parse(this.response);
            window.location.href = "viewcart";
            
            }
            
        }
    xml.open('POST', 'downgrade-cart-action', true);
    xml.send(formdata);

}

function mycart() {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ar = JSON.parse(this.response);
            if (ar.length > 0) {
                var s = "<table class='table table-bordered'><tr>";
                s += "<th>Srno.</th>";
                s += "<th>Product Name</th>";
                s += "<th>Photo</th>";
                s += "<th>Price</th>";
                s += "<th>QTY</th>";
                s += "<th>Amount</th></tr>";
                var netamount = 0;
                for (var i = 0; i < ar.length; i++) {
                    netamount += parseFloat(ar[i]['total']);
                    s += "<tr>";
                    s += "<td>" + (i + 1) + "</td>";
                    s += "<td>" + ar[i]['pname'] + "</td>";
                    s += "<td><img src='../static/media/" + ar[i]['photo'] + "' style='width:70px;height:60px;'></td>";
                    s += "<td>" + ar[i]['price'] + "</td>";
                    s += "<td>" + ar[i]['qty'] + "</td>";
                    s += "<td>" + ar[i]['total'] + "</td>";
                    s += "</tr>";
                }
                s += "<tr><td colspan='5' class='text-right'><strong>Net Amount</strong></td><td>" + netamount + "</td></tr>";
                s += "<tr><p><td colspan='6' class='text-center'>" +
                    "<a href='view-allproducts' class='btn btn-warning'>Continue Shopping</a> " +
                    "<a href='proceedtopay' class='btn btn-success'>Proceed to Pay</a></p>" +
                    "</td></tr>";
                s += "</table>";

            }
            else{
                 var s ='<div class="container">' +
                     '<div class="row">' +
                     '<div class="text-center" style="padding: 0px 0px 0px 0px";>' +
                     '<img src="../static/img/empty-cart.png" alt="">' +
                     '</div>' +
                     '</div>' +
                     '<div class="row text-center" style="padding: 10px 0px 0px 0px">' +
                     '<span class="text-center"><a href="view-allproducts" class="btn btn-warning">Continue Shopping</a></span>' +
                     '</div>' +
                     '</div>';
            }
            document.getElementById('output').innerHTML = s;
        }

    };
    xml.open('GET', 'my-cart-action', true);
    xml.send();
}

function userlogin() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var fromcart = document.getElementById('fromcart').value;
    var formdata = new FormData();
    formdata.append('email', email);
    formdata.append('password', password);
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ar = JSON.parse(this.response);
            if (ar['msg'] == "Login Success") {
                if (fromcart == 'yes') {
                    window.location.href = 'my-cart';
                }
                else {
                    window.location.href = 'user-homepage'
                }
            }
            else {
                var s = "<div class='alert alert-warning'><h3>" + ar["msg"] + "</h3></div>";
                document.getElementById("msg").innerHTML = s;
            }
        }
    };
    xml.open("POST", "login-action", true);
    xml.send(formdata);

}

function loginnav() {
    s = '<div class="row" style="margin: -21px;">' +
        '<div class="col-md-6"><h5 class="text-muted text-right" style="padding: 8px"><strong>LOGIN</strong></h5></div>' +
        ' <div class="col-md-6" style="padding-left: 100px;padding-top: 10px;padding-bottom: 10px">       ' +
        '       ' +
        ' ' +
        '            <form id="frm_userlogin" class="form-inline" role="form">' +
        '            <input type="text" id="fromcart" style="display: none">   '+
        '            <div class="form-group">' +
        '                <label class="text-muted" style="padding-left: 8px;padding-right: 8px;">Email</label>' +
        '                <input placeholder="Enter your email" type="email" class="form-control" id="email" name="email"' +
        '                       data-rule-required="true" data-msg-required="">' +
        '            </div>' +
        '            <div class="form-group">' +
        '                <label class="text-muted" style="padding-left: 8px;padding-right: 8px;">Password</label>' +
        '                <input type="password" placeholder="Enter Password" class="form-control" id="password" name="password"' +
        '                       data-rule-required="true" data-msg-required="">' +
        '            </div>' +
        '            <div class="form-group">' +
        '                <input type="button" onclick="userlogin()" value="Login" class="btn-success btn">' +
        '            </div>' +
        '            </form>' +
        '            <div id="msg"></div>' +
        '     </div>   ' +
        '</div> ' +
        ' ' +
        '';
    document.getElementById('navlogin').innerHTML = s;
}

function billinginfo() {
            var formdata = new FormData();
            formdata.append('email',document.getElementById('email').value);
            formdata.append('fullName',document.getElementById('fullName').value);
            formdata.append('netAmount',document.getElementById('netAmount').value);
            formdata.append('mobileNo',document.getElementById('mobileNo').value);
            formdata.append('address',document.getElementById('address').value);
            formdata.append('city',document.getElementById('city').value);
            formdata.append('paymentMode',document.getElementById('paymentMode').value);

            if (document.getElementById('paymentMode').value == 'Online') {

                var amount = parseFloat(document.getElementById('netAmount').value) * 100;

                var options = {
                    "key": "rzp_test_dRWiKHS7zr2Gki",
                    "amount": amount,
                    "name": "Online Shopping System",
                    "description": "Payment Gateway",
                    "image": "http://ecourses.aec.edu.in/aditya/images/po4.png",
                    "handler": function (response) {
                        //alert(response.razorpay_payment_id);
                        if (response.razorpay_payment_id == "") {
                            //alert('Failed');
                            var xml = new XMLHttpRequest();
                            xml.onreadystatechange = function () {
                                if (this.readyState == 4 && this.status == 200) {
                                    window.location.href = "sorrypage";
                                }
                            };
                            xml.open('POST', 'checkoutaction', true);
                            xml.send(formdata);

                        }
                        else {
                            //alert('Success');
                            var xml = new XMLHttpRequest();
                            xml.onreadystatechange = function () {
                                if (this.readyState == 4 && this.status == 200) {
                                    window.location.href = "thankspage";
                                }
                            };
                            xml.open('POST', 'checkoutaction', true);
                            xml.send(formdata);

                        }
                    },
                    "prefill": {
                        //{#"name": document.getElementById('fullname').value,#}
                        "email": email
                    },
                    "notes": {
                        "address": ""
                    },
                    "theme": {
                        "color": "#F37254"
                    }
                };
                var rzp1 = new Razorpay(options);
                rzp1.open();
            }
            else {
                var xml = new XMLHttpRequest();
                xml.onreadystatechange = function () {
                    if (this.readyState == 4 && this.status == 200) {
                        window.location.href = "thankspage";
                    }
                };
                xml.open('POST', 'checkoutaction', true);
                xml.send(formdata);
            }
        }

function pendingorders() {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange=function () {
        if(this.readyState==4 && this.status==200){
            var ar = JSON.parse(this.response);
            var Accepted = "Accepted";
            var Rejected = "Rejected";
            var s = "";
            s += "<table class='table table-bordered'>";
            s += "<th>Order ID</th>";
            s += "<th>Date</th>";
            s += "<th>Email</th>";
            s += "<th>Name</th>";
            s += "<th>Mobielno</th>";
            s += "<th>City</th>";
            s += "<th>Amount</th>";
            s += "<th>Payment Mode</th>";
            s += "<th colspan='2'>Controls</th>";

            for (var i = 0; i < ar.length; i++) {
                s += "<tr>";
                s += "<td>" + ar[i]['id'] + "</td>";
                s += "<td>" + ar[i]['dateoforder'] + "</td>";
                s += "<td>" + ar[i]['email'] + "</td>";
                s += "<td>" + ar[i]['fullname'] + "</td>";
                s += "<td>" + ar[i]['mobileno'] + "</td>";
                s += "<td>" + ar[i]['city'] + "</td>";
                s += "<td>" + ar[i]['netamount'] + "</td>";
                s += "<td>" + ar[i]['paymentmode'] + "</td>";
               // console.log("<td class='text-center'><button class='btn btn-success' onclick='approve_reject_order(" + ar[i]['id'] + ","+Accepted+","+ ar[i]["mobileno"]+")'>Accept</button></td>")
                s += "<td class='text-center'><button class='btn btn-success' onclick=approve_reject_order(" + ar[i]['id'] + ",'Accepted',"+ar[i]["mobileno"]+")>Accept</button></td>";
                s += "<td class='text-center'><button class='btn btn-danger' onclick=approve_reject_order(" + ar[i]['id'] + ",'Rejected',"+ar[i]["mobileno"]+")>Reject</button></td>";
                s += "</tr>";
            }

            s += "</table>";
            document.getElementById('output').innerHTML = s;
        }
    };
    xml.open("GET","pending-order-action",true);
    xml.send();
}

function approve_reject_order(orderid,status,mobileNo) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ar = JSON.parse(this.response);
            window.location.href = "pending-orders";
        }
    };
    xml.open('GET', 'approve_reject_action?orderid=' + orderid + "&status=" + status + "&mobile="+mobileNo, true);
    xml.send();
}

function myorders(useremail) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var ar = JSON.parse(this.response);
            var s = "";
            s += "<table class='table table-bordered'>";
            s += "<th>Order ID</th>";
            s += "<th>Date</th>";
            s += "<th>Name</th>";
            s += "<th>Mobielno</th>";
            s += "<th>City</th>";
            s += "<th>Amount</th>";
            s += "<th>Payment Mode</th>";
            s += "<th>Status</th>";

            for (var i = 0; i < ar.length; i++) {
                s += "<tr>";
                s += "<td>" + ar[i]['id'] + "</td>";
                s += "<td>" + ar[i]['dateoforder'] + "</td>";
                s += "<td>" + ar[i]['fullname'] + "</td>";
                s += "<td>" + ar[i]['mobileno'] + "</td>";
                s += "<td>" + ar[i]['city'] + "</td>";
                s += "<td>" + ar[i]['netamount'] + "</td>";
                s += "<td>" + ar[i]['paymentmode'] + "</td>";
                s += "<td>" + ar[i]['status'] + "</td>";
                s += "</tr>";
            }
            s += "</table>";
            document.getElementById('output').innerHTML = s;
        }
    };
    xml.open('GET', 'myordersaction?email='+useremail, true);
    xml.send();
}