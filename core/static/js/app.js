// App btns
function OpenMenu() {
  var navbar = $(".menu");
  if (navbar.attr('class') === "menu") {
    navbar.addClass(" responsive");
  } else {
    navbar.attr('class', 'menu');
  }
}


function getTable() {
    let input = $("#selectTable").val();
    let url = "";
    if (input == 0) {
        url = "http://127.0.0.1:8000/customers/table/"
        $("#btnsCustomer").css("display", "inline-flex");
        $("#btnsRequest").hide();
    } else {
        url = "http://127.0.0.1:8000/requests/table/"
        $("#btnsRequest").css("display", "inline-flex");
        $("#btnsCustomer").hide();
    }
    $.get(url, function(data) {
        $("#divTable").html(data);
    })
}


function filterStatus() {
    let input = $("#SelectorStatus").val()
    let tr = $("tr");
    let option = setOptionValue(input);
        for (i = 0; i < tr.length; i++) {
        let td = tr[i].getElementsByTagName("td")[1];
        if (td) {
         let txtValue = td.textContent || td.innerText;
          if (txtValue.indexOf(option) > -1) {
            tr[i].style.display = "";
          } else {
            tr[i].style.display = "none";
          }
        }
      }
}

function setOptionValue(input) {
    switch(input) {
      case '0':
        option = ''
        break;
      case '1':
        option = 'Concluido'
        break;
      case '2':
        option = 'Em aguardo'
        break;
      case '3':
        option = 'Em aberto'
        break;
      default:
        option = ''
    }
    return option
}
// Filter
function filterCpf(filter) {
    let input = filter.value
    let tr = $("tr");
    for (i = 0; i < tr.length; i++) {
        let td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            let txtValue = td.textContent || td.innerText;
            if (txtValue.indexOf(input) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
      }
}


function clearFilter() {
    let filter = $(".input-filter")
    filter.val('')
}


// Modal
function showModal() {
    $("#Modal").toggle();
}


$(document).click(function(event) {
    if ($(event.target).attr('id') == "Modal") {
        showModal();
    }
});


// Form
function getCustomerForm() {
    $.get("http://127.0.0.1:8000/customers/form/", function(data) {
        $("#Edit").html(data)
        showModal();
    })
}


function getRequestForm() {
    $.get("http://127.0.0.1:8000/requests/form/", function(data) {
        $("#Edit").html(data)
        showModal();
    })
}


// Edit
function getEditRequests(id) {
    $.get("http://127.0.0.1:8000/requests/edit=" + id + "/", function(data) {
         $("#Edit").html(data)
         showModal();
    })
}


function setEditRequest(id) {
    $.post("http://127.0.0.1:8000/requests/edit=" + id + "/", data=requestData(), function(data, status) {
        alert(data)
        if (status == 'success') {
            getTable();
            showModal();
        }
    })
}


function getEditCustomers(id) {
    $.get("http://127.0.0.1:8000/customers/edit=" + id + "/", function(data) {
        $("#Edit").html(data)
        showModal();
    })
}


function setEditCustomer(id) {
    $.post("http://127.0.0.1:8000/customers/edit=" + id + "/", data=customerData(), function(data, status) {
    alert(data)
    if (status == 'success') {
        getTable();
        showModal();
        }
    })
}


function saveCustomer() {
    $.post("http://127.0.0.1:8000/customers/new/", data=customerData(),function (data, status) {
        alert(data)
        if (status == 'success') {
            showModal()
            getTable()
        }
    })
}


function saveRequests() {
    $.post("http://127.0.0.1:8000/requests/new/", data=requestData(), function (data, status) {
        alert(data)
        if (status == 'success') {
            showModal()
            getTable()
        }
    })
}


function deleteCustomer(id) {
    $.post("http://127.0.0.1:8000/customers/delete/id="  + id + "/", function (data, status) {
        alert(data)
        if (status == 'success') {
            showModal();
            getTable()
        }
    })
}


function deleteRequest(id) {
    $.post("http://127.0.0.1:8000/requests/delete/id="  + id + "/", function (data, status) {
        alert(data)
        if (status == 'success') {
            showModal();
            getTable()
        }
    })
}


// Data to customer post
function customerData() {
    cpf = $("#Cpf").val()
    name = $("#Name").val()
    lastname = $("#Lastname").val()
    city = $("#City").val()
    address = $("#Address").val()
    telephone = $("#Telephone").val()
    email = $("#Email").val()

    data ={
    cpf: cpf,
    name: name,
    lastname: lastname,
    city: city,
    address: address,
    telephone: telephone,
    email: email,
    }
    return data
}


function requestData() {
    choice = $("#Choice").val()
    title = $("#Title").val()
    order = $("#Order").val()
    status = $("#Status").val()
    data = {
        choice: choice,
        title: title,
        order: order,
        status: status,
    }
    return data
}
