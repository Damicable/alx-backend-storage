"""Nginx log stats module """


from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db_count = client.logs.nginx.count({})
    methods_dict = {
                'GET': client.logs.nginx.count({'method': 'GET'}),
                'POST': client.logs.nginx.count({'method': 'POSTT'}),
                'PUT': client.logs.nginx.count({'method': 'PUT'}),
                'PATCH': client.logs.nginx.count({'method': 'PATCH'}),
                'DELETE': client.logs.nginx.count({'method': 'DELETE'}),
            }
    get_status = client.logs.nginx.count({'method': 'GET', 'path': '/status'})

    print("{} logs".format(db_count))
    print("Methods: ")
    for key, val in methods_dict.items():
        print("\tmethod {}: {}".format(key, val))
    print("{} status check".format(get_status))
