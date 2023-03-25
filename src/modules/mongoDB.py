from pymongo import MongoClient

# remote server
# mongo = MongoClient(
#     "mongodb+srv://admin_1:4CK7pMDfiAHluWVW@caselawcluster1.nmsrbiv.mongodb.net/?retryWrites=true&w=majority")

try:
    # remote server
    mongo = MongoClient("mongodb+srv://admin_1:4CK7pMDfiAHluWVW@caselawcluster1.nmsrbiv.mongodb.net/?retryWrites=true&w=majority",
                        tls=True, tlsAllowInvalidCertificates=True)

except:
    # local server
    mongo = MongoClient("mongodb://localhost:27017")


def update(id, pages, isProcessed, isProcessedFailed, processing_log, isCertified):
    return mongo.test.documents.update_one({"_id": id}, {
        "$set": {"pages": pages,
                 "isProcessed": isProcessed,
                 "isProcessedFailed": isProcessedFailed,
                 "processing_log": processing_log,
                 "isCertified": isCertified
                 }
    }
    )


def find(isProcessed):
    return mongo.test.documents.find({"isProcessed": isProcessed})


def insert(data):
    return mongo.test.documents.insert_one(data)
