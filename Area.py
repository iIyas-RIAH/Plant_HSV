# import required libraries
import cv2

# load the input image
img = cv2.imread('Images/savedImage.jpg')

# convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply thresholding to convert grayscale to binary image
ret, thresh = cv2.threshold(gray, 40, 255, 0)

# find the contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("Number of objects detected:", len(contours))

w0 = img.shape[0]
h0 = img.shape[1]

somme = 0


# define function to compute the extent
def extent(cnt):
    area = cv2.contourArea(cnt)
    rect_area = w * h
    extent = float(area) / rect_area
    return extent


# loop over all the contours
for i, cnt in enumerate(contours):
    area = cv2.contourArea(cnt)
    rect_area = w0 * h0
    ext = float(area) / rect_area
    x, y, w, h = cv2.boundingRect(cnt)
    img = cv2.drawContours(img, [cnt], 0, (255, 255, 255), 2)
    somme += ext

somme = round(somme, 2)
print(somme)
cv2.imshow("Extents", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
