$(document).ready(function(){
    // Validate username
    $("#username").change(function() {
        $.ajax({
            type: 'POST',
            url: $("#form-register").data("url"),
            data: {
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(), // Bắt buộc phải có CSRF TOKEN
                username: $(this).val()
            },
            success: function (data) {
                $("#username").removeClass("is-invalid");
                $("#username").addClass("is-valid");
                $("#username").parent().append(`<div class="valid-feedback">${data.message}</div>`);
            },
            error: function ($xhr, textStatus, erroThrown) {
                $("#username").removeClass("is-valid");
                $("#username").addClass("is-invalid");
                $("#username").parent().append(`<div class="invalid-feedback">${$xhr.responseJSON.message}</div>`);
            }
        })
    });
    
    // Password và confirm_password phải giống nhau (client validation)
    $("#password").change(function () {
        var password = $(this).val();
        if (password.length < 6) {
            $(this).removeClass("is-valid");
            $(this).addClass("is-invalid");
            $(this).parent().append(`<div class="invalid-feedback">Mật khẩu quá ngắn</div>`);
        }
        else {
            $(this).removeClass("is-invalid");
            $(this).addClass("is-valid");
            $(this).parent().append(`<div class="valid-feedback">OK</div>`);
        }
    });
    $("#confirm_password").change(function () {
        var password = $("#password").val();
        var confirm_password = $(this).val();
        if (password != confirm_password) {
            $(this).removeClass("is-valid");
            $(this).addClass("is-invalid");
            $(this).parent().append(`<div class="invalid-feedback">Nhập lại mật khẩu không khớp</div>`);
        }
        else {
            $(this).removeClass("is-invalid");
            $(this).addClass("is-valid");
            $(this).parent().append(`<div class="valid-feedback">OK</div>`);
        }
    });
    $("#first_name").change(function () {
        var first_name = $(this).val();
        if (first_name.length < 2) {
            $(this).removeClass("is-valid");
            $(this).addClass("is-invalid");
            $(this).parent().append(`<div class="invalid-feedback">Tên quá ngắn</div>`);
        }
        else {
            $(this).removeClass("is-invalid");
            $(this).addClass("is-valid");
            $(this).parent().append(`<div class="valid-feedback">OK</div>`);
        }
    });
    $("#last_name").change(function () {
        var last_name = $(this).val();
        if (last_name.length < 2) {
            $(this).removeClass("is-valid");
            $(this).addClass("is-invalid");
            $(this).parent().append(`<div class="invalid-feedback">Họ quá ngắn</div>`);
        }
        else {
            $(this).removeClass("is-invalid");
            $(this).addClass("is-valid");
            $(this).parent().append(`<div class="valid-feedback">OK</div>`);
        }
    });
});