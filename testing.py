import cv2
img = cv2.imread("test1.png")
img2 = img.copy()
mask = cv2.imread("test_ad.jpg")
print(mask.shape)

pos = (116,134)

img2[pos[0]:(pos[0]+mask.shape[0]), pos[1]:(pos[1]+mask.shape[1])] = mask
cv2.imshow("img",img2)

cv2.waitKey(0)