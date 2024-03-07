import matplotlib.pyplot as plt
import easyocr
from IPython.display import Image

# Display the image
Image("plates/scaned_img_0.jpg")

# Initialize EasyOCR reader
reader = easyocr.Reader(['id'])

# Perform OCR on the image
output = reader.readtext('plates/scaned_img_0.jpg')
for item in output:
    print(item[1])
