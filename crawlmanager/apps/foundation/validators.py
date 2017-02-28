from voluptuous import All, REMOVE_EXTRA, Required, Schema, Length

login_validator = Schema({
    Required('name'):       All(str, Length(max=64), msg='用户名格式有误'),
    Required('password'):   All(str, Length(max=128), msg='密码格式有误'),
}, extra=REMOVE_EXTRA)