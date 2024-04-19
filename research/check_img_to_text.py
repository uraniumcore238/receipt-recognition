# import pytesseract
# from PIL import Image
# # TODO
# # Path to the Tesseract executable (Change it according to your installation)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#
# # # Open the image file
# # image_path = r'C:\Users\urani\Documents\Programming\Python_projects\receipt-recognition\images\receipt_one.jpg'  # Replace 'image.jpg' with the path to your image
# # img = Image.open(image_path)
# #
# # # Use pytesseract to do OCR on the image
# # text = pytesseract.image_to_string(img)
# #
# # # Print the extracted text
# # print(text)
#
#
# import cv2
# from PIL import Image
# import pytesseract
#
# img_cv = cv2.imread(r'C:\Users\urani\Documents\Programming\Python_projects\receipt-recognition\images\receipt_one.jpg')
#
#
# img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img_rgb))
# # OR
# img_rgb = Image.frombytes('RGB', img_cv.shape[:2], img_cv, 'raw', 'BGR', 0, 0)
# print(pytesseract.image_to_string(img_rgb))
