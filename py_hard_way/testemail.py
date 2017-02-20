def checkEmail(email):
if len(email)>20:
    return error
if not isinstance(email,str):
    return error
if '@' not in email:
     ...:         return error
     ...:     if email[-4:] not in ['.com','.net','.cn']:
     ...:         return error
