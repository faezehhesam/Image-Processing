import cv2

img=cv2.imread('DATA/111.jpg')

while True:
    cv2.imshow('111',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()        
        
    
    
    