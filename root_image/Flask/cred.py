import base64


cred = ''
cred_byte = cred.encode(encoding='UTF-8',errors='strict')
encoded = base64.b64encode(cred)
vcenter = ''

auth_header = []

auth_header.append( "Authorization = "Basic")
