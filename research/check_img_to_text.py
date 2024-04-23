import pytesseract
from PIL import Image
import cv2


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


image_path = (r'C:\Users\urani\Documents\Programming\Python_projects\receipt-recognition\images'
              r'\receipt_one.jpg')
img = Image.open(image_path)
text = pytesseract.image_to_string(img)


img_cv = cv2.imread(r'C:\Users\urani\Documents\Programming\Python_projects\receipt-recognition\
images\receipt_one.jpg')


img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
pytesseract.image_to_string(img_rgb)

img_rgb = Image.frombytes('RGB', img_cv.shape[:2], img_cv, 'raw',
                          'BGR', 0, 0)
pytesseract.image_to_string(img_rgb)
