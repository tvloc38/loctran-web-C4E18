import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds121331.mlab.com:21331/c4e18-cms

host = "ds121331.mlab.com"
port = 21331
db_name = "c4e18-cms"
user_name = "admin"
password = "admin123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())