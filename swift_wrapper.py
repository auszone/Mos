import swiftclient
import os

container_name = 'data'
conn = swiftclient.Connection(
    user=os.environ['OS_USERNAME'],
    key=os.environ['OS_PASSWORD'],
    authurl=os.environ['OS_AUTH_URL'],
    tenant_name="hackthon6",
    auth_version="2.0"
)
def send(file):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = file.name
    conn.put_object(container_name, filename, contents=file.read())

def upload_from_file(filename):
    with open(filename, 'r') as my_file:
        conn.put_object(container_name, filename, contents= my_file.read())

def download(filename):
    obj_tuple = conn.get_object(container_name, filename)
    with open(filename, 'w') as my_file:
        my_file.write(obj_tuple[1])

def updateMetaData(object, dict):
    conn.post_object(container_name, object, headers=dict)

