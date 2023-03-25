# import os
# import docx
# import requests
# from src.modules.mongoDB import update


# doc_pages = []
# root = os.getcwd()

# # function to upload document


# def handleDocxExtraction(document):
#     doc_pages = []
#     docurl = document["document"]["data_url"]
#     isCertified = False

#     try:
#         # send request to *cloudinary*
#         request = requests.get(docurl)

#         # tmp dir for temporary file storage
#         path = os.path.join(root, "tmp", os.path.basename(docurl))

#         # save file in a tmp folder
#         with open(path, 'wb') as f:
#             f.write(request.content)
#             print(
#                 "***************** done writing to doc *******************")

#         # read the pdf from tmp folder
#         doc = docx.Document(path)

#         # extract text from docx
#         for page in doc.paragraphs:
#             text = page.text
#             # clean extracted file
#             text.replace("\n", "")

#             # check if empty text
#             if text == "":
#                 pass
#             else:
#                 doc_pages.append(text)

#         # upload to mongo db
#         update(document["_id"], doc_pages, True, False, "", isCertified)

#         doc_pages = []

#         # delete file from tmp
#         os.remove(path)

#     except Exception as e:
#         doc_pages = []
#         # upload and update mongo db
#         update(document["_id"], doc_pages, True, True, e, isCertified)

#     pass
