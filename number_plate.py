import cv2
import easyocr
from IPython.display import Image

# Load the Haar cascade for plate detection
harcascade = "model/haarcascade_russian_plate_number.xml"

# Initialize the video capture
cap = cv2.VideoCapture(0)
cap.set(3, 640) # width
cap.set(4, 480) # height

# Minimum area for plate detection
min_area = 500
count = 0

# Infinite loop to capture video frames
while True:
    success, img = cap.read()

    # Load the plate cascade
    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect plates
    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    # Iterate through detected plates
    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            # Extract plate region of interest (ROI)
            img_roi = img[y: y + h, x:x + w]
            cv2.imshow("ROI", img_roi)

    # Display the result
    cv2.imshow("Result", img)

    # Save the plate image when 's' is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_roi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        cv2.imshow("Results", img)
        cv2.waitKey(500)
        count += 1
        # Display the saved image
        Image("plates/scaned_img_" + str(count - 1) + ".jpg")

        # Initialize EasyOCR reader
        reader = easyocr.Reader(['id'])

        # Perform OCR on the image
        output = reader.readtext('plates/scaned_img_' + str(count - 1) + '.jpg')
        for item in output:
            print(item[1])

# Release the capture
cap.release()
cv2.destroyAllWindows()
