#!/usr/bin/env python3
"""Nginx stats"""


from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Count total logs
    db_count = client.logs.nginx.count_documents({})

    # Count methods
    methods_dict = {
        'GET': client.logs.nginx.count_documents({'method': 'GET'}),
        'POST': client.logs.nginx.count_documents({'method': 'POST'}),
        'PUT': client.logs.nginx.count_documents({'method': 'PUT'}),
        'PATCH': client.logs.nginx.count_documents({'method': 'PATCH'}),
        'DELETE': client.logs.nginx.count_documents({'method': 'DELETE'}),
    }

    # Count status check
    get_status = client.logs.nginx.count_documents({'method': 'GET', 'path': '/status'})

    # Count top 10 IPs
    top_ips = client.logs.nginx.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print("{} logs".format(db_count))
    
    # Print methods count
    print("Methods: ")
    for key, val in methods_dict.items():
        print("\tmethod {}: {}".format(key, val))
    
    print("{} status check".format(get_status))

    # Print top 10 IPs
    print("IPs:")
    for ip in top_ips:
        print("\t{}: {}".format(ip["_id"], ip["count"]))

    client.close()
