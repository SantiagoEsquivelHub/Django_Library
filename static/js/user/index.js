const listUsers = () => {
    $.ajax({
        url: "/user/list_user",
        type: "get",
        dataType: "json",
        success: (response) => {
            if ($.fn.DataTable.isDataTable("#users_table"))
                $("#users_table").DataTable().destroy()

            $("#users_table tbody").html("")
            for (let i = 0; i < response.length; i++) {
                let row = "<tr>"
                row += "<td>" + response[i]["pk"] + "</td>"
                row += "<td>" + response[i]["fields"]["username"] + "</td>"
                row += "<td>" + response[i]["fields"]["name"] + "</td>"
                row += "<td>" + response[i]["fields"]["last_name"] + "</td>"
                row += "<td>" + response[i]["fields"]["email"] + "</td>"
                row += "<td>" + "<button type='button' class='btn btn-primary tableButton'"
                row += 'onclick="abrir_modal_edicion(\'/user/edit_user/'+response[i]['pk']+'/\');">Edit</button>'
                row += '<button type="button" class="btn btn-danger tableButton" onclick="abrir_modal_eliminacion(\'/user/delete_user/'+response[i]['pk']+'/\');">Delete</button>' + "</td>"
                row += "</tr>"
                $("#users_table tbody").append(row)
            }
            $("#users_table").DataTable({
                language: {
                    decimal: "",
                    emptyTable: "No hay información",
                    info: "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                    infoEmpty: "Mostrando 0 to 0 of 0 Entradas",
                    infoFiltered: "(Filtrado de MAX total entradas)",
                    infoPostFix: "",
                    thousands: ",",
                    lengthMenu: "Mostrar MENU Entradas",
                    loadingRecords: "Cargando...",
                    processing: "Procesando...",
                    search: "Buscar:",
                    zeroRecords: "Sin resultados encontrados",
                    paginate: {
                        first: "Primero",
                        last: "Ultimo",
                        next: "Siguiente",
                        previous: "Anterior",
                    },
                },
            })
        },
        error: (error) => {
            console.log("error: ", error)
        }
    })
}

const registerUser = () => {
    activarBoton()
    $.ajax({
        data: $("#creation_form").serialize(),
        url: $("#creation_form").attr("action"),
        type: $("#creation_form").attr("method"),
        success: (response) => {
            notificacionSuccess(response.message)
            listUsers()
            cerrar_modal_creacion();
        },
        error: (error) => {
            notificacionError(error.responseJSON.message)
            mostrarErroresCreacion(error)
        }
    })
}

const editUser = () => {
    activarBoton()
    $.ajax({
        data: $("#edition_form").serialize(),
        url: $("#edition_form").attr("action"),
        type: $("#edition_form").attr("method"),
        success: (response) => {
            notificacionSuccess(response.message)
            listUsers()
            cerrar_modal_edicion();
        },
        error: (error) => {
            notificacionError(error.responseJSON.message)
            mostrarErroresEdicion(error)
        }
    })
}

const deleteUser = (pk) => {
    activarBoton()
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name= 'csrfmiddlewaretoken']").val()
        },
        url: '/user/delete_user/'+pk+'/',
        type: 'post',
        success: (response) => {
            notificacionSuccess(response.message)
            listUsers()
            cerrar_modal_eliminacion();
        },
        error: (error) => {
            notificacionError(error.responseJSON.message)
        }
    })
}


$(document).ready(() => listUsers())