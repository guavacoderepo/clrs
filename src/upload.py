import os
from src.modules.mongoDB import insert

# function to upload document


def handleDocxUpload():

    # upload demo data
    data = {
        "document": {
            "doc_type": "pdf",
            "data_url": "https://clrs-bucket.nyc3.cdn.digitaloceanspaces.com/doc-3.pdf"
        },
        "pages": [],
        "isCertified": False,
        "isProcessed": False,
        "isProcessedFailed": False,
        "processing_log": ""
    }
    doc = insert(data)
    print(doc.inserted_id)
