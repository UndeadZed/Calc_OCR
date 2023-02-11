import easyocr



def use_ocr(img):

    res = ""

    reader = easyocr.Reader(['en'])  # English language

    result = reader.readtext(img)

    for r in result:
        res = res+" "+str(r[1])

    return res



