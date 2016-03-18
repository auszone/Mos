import swiftclient
user = 'hackthon6'
key = 'ohpiebau'
host = '172.17.18.3'
container_name = 'mos'
conn = swiftclient.Connection(
    user=user,
    key=key,
    authurl="http://"+ host +":5000/v2.0",
    tenant_name="hackthon6",
    auth_version="2.0"
)
def upload(filename):
    with open(filename, 'r') as my_file:
        conn.put_object(container_name, filename, contents= my_file.read())

def download(filename):
    obj_tuple = conn.get_object(container_name, filename)
    with open(filename, 'w') as my_file:
        my_file.write(obj_tuple[1])

