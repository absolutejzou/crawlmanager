$(function () {
    $("form").validate({
        rules: {
            name: {
                required: true,
                minlength: 4,
                maxlength: 16
            },
            password: {
                required: true,
                minlength: 8,
                maxlength: 32
            }
        },
        messages: {
            name: {
                required: '用户名不能为空',
                minlength: '用户名长度必须为4-16位',
                maxlength: '用户名长度必须为4-16位'
            },
            password: {
                required: '密码不能为空',
                minlength: '密码长度必须为8-32位',
                maxlength: '密码长度必须为8-32位'
            }
        },
        errorElement: 'div',
        errorPlacement: function(error, element) {
            var placement = $(element).data('error');
            if (placement) {
                $(placement).append(error)
            } else {
                error.insertAfter(element);
            }
        }
    });
});
