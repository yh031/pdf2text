# import module
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os

thePdfFile = './docs/file.pdf'
# Store Pdf with convert_from_path function
images = convert_from_path(thePdfFile)
text = ''

numOfPdf = range(len(images)).stop
withoutArr = []


# for i in range(len(images)):
for i, image in enumerate(images):
    tmpText = ''
    imgLink = './tmp/page-' + str(i) + '.jpg'

    print(f"looking paged: {i}/{numOfPdf} | {round(i / numOfPdf * 100, 2)} %")
    
    # without case
    if i in withoutArr:
        print(f'paged {i} without')
    else:
        print(f'paged {i} running')
        # Save pages as images in the pdf
        images[i].save(imgLink, 'JPEG')

        # OCR the image
        _img = Image.open(imgLink)

        tmpText = pytesseract.image_to_string(_img, lang='chi_sim+eng') #chi_tra+chi_sim+eng
        tmpText = tmpText.replace("圖", "")
        tmpText = tmpText.replace(" ", "")

        text += tmpText

        print(tmpText)

        # remove the image file
        os.remove(imgLink)


print("DONE")
with open('./data-out.txt', 'w') as file:
    file.write(text)
    
