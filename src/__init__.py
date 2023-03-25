import os
from src.modules.mongoDB import find
# from src.docxOCR import handleDocxExtraction
from src.pdfOCR import handlePdfExtraction
from src.invalid import handleInvalideFile


doc_pages = []
root = os.getcwd()


def mainProcess():
    # fetch all unprocessed documents
    documents = find(False)

    # if document new upload documets found
    if not documents:

        print("********* no new document found *********")

    else:

        for document in documents:
            # get doctype field
            doctype = document["document"]["doc_type"]

            # check document type for extraction
            # run extraction on pdf document
            if doctype == "pdf":
                # pdf document extration function
                handlePdfExtraction(document)

            elif doctype == "docx":
                # docx document extration function
                handleInvalideFile(document)
                # handleDocxExtraction(document)
            else:

                handleInvalideFile(document)
