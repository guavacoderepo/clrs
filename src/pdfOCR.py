from src.modules.mongoDB import update
from PyPDF2 import PdfReader
import os
import requests
import cv2
import easyocr
import fitz
import numpy as np


doc_pages = []
root = os.getcwd()
reader = easyocr.Reader(['en'])

# function to for text extraction


def handlePdfExtraction(document):

    doc_pages = []
    docurl = document["document"]["data_url"]
    isCertified = False

    print(
        "***************** started *******************\n")

    try:
        print(
            "***************** before request *******************\n")
        # send request to *cloudinary*
        request = requests.get(docurl)
        print(
            "***************** request done *******************\n")

        # tmp dir for temporary file storage
        path = os.path.join(root, "tmp", os.path.basename(docurl))
        imgPath = os.path.join(root, "tmp/pdfConvertedImage.png")

        # save file in a tmp folder
        with open(path, 'wb') as f:
            f.write(request.content)
            print(
                "***************** done writing to pdf *******************\n")

# ******************************************************************************************
        # print(path)

         # read the pdf from tmp folder
        reader = PdfReader(path)

        # extract text from docx
        for page in reader.pages:
            # print(page.extract_text())
            text = page.extract_text()
            # clean extracted file
            text.replace("\n", "")

            # check if empty text
            if text == "":
                pass
            else:
                doc_pages.append(text)

# ******************************************************************************************

        if doc_pages[0] == "" and doc_pages[len(doc_pages)] == "":
            print("************ Not ocr doc ***********************")
            # get the pdf from tmp folder
            doc = fitz.open(path)

            # ite through the pages of the document
            for page_idx in range(doc.page_count):

                text = ""

                page = doc[page_idx]
                pix = page.get_pixmap()

                # Save the image
                # image_file = f"tmp/converetedImage.png"

                # Save pages as images in the pdf
                pix.save(imgPath)

                # get image for ocr operation
                img = cv2.imread(imgPath)

                # convert image to grey scale
                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # Create the sharpening kernel
                kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

                # Apply the sharpening kernel to the image using filter2D

                img = cv2.filter2D(img_rgb, -1, kernel)

                # save document in greyscale
                # cv2.imwrite(imgPath, img)
                cv2.imwrite(imgPath, img_rgb)

                # read en model for running ocr

                # extract text from image
                # extracted = reader.readtext(img_rgb, detail=0)
                extracted = reader.readtext(imgPath, detail=0)

                # iterate through extracted text and join
                for t in extracted:
                    text = text + " " + t

                    # check isCertified in text
                    if "certif" in text:
                        print("************** certified found **************\n")
                        isCertified = True

                print("************** extraction done **************\n")

                # check if empty text
                if text == "":
                    pass
                else:
                    doc_pages.append(text)

# ******************************************************************************************

        # update db
        update(document["_id"], doc_pages, True, False, "", isCertified)

        # empty for new data
        doc_pages = []

        # delete file from tmp
        os.remove(path)

    except Exception as e:
        doc_pages = []
        update(document["_id"], doc_pages, True, True, e, isCertified)

        print(e)
    pass
