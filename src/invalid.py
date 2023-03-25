from src.modules.mongoDB import update


def handleInvalideFile(document):
    doc_pages = []

    try:
        # upload to mongo db
        update(document["_id"], doc_pages, True,
               True, "Invalid file format/type", False)
        print("Invalid file format/type")

    except Exception as e:
        print(e)
        pass
