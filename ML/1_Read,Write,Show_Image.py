from cv2 import cv2
#imread will read the image
#integer value 1 means load a color image, 0 means load image in grayscale mode,
# -1 means cv2.imread_unchanged (loads image as such imcluding a channel) 
img=cv2.imread('lena.jpg',-1)

print(img)
cv2.imshow("image",img)
#cv2.waitKey(5000)  # wait for 5000 
#If you want the user to close,then
k= cv2.waitKey(0)

if k==27:   #pressed esc key
    cv2.destroyAllWindows()
elif k== ord('s'):   #if pressed s key
    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()