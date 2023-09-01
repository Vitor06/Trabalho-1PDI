import numpy as np
import cv2 as cv


def main():
    m = 120       
    x = 30

    if(m+x>360):   
        intervalo_superior = ((m + x)%360) //2
        intervalo_inferior = (m - x )//2 

    # if(m-x<0):
    #     intervalo_superior = (m + x) //2
    #     intervalo_inferior = ((m - x ) + 360 )//2 
    else:
        intervalo_inferior = (m - x )//2 
        intervalo_superior = (m + x) //2

    img = cv.imread("flor.jpg")
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_channel = hsv_img[:, :, 0]  # Canal H (Matiz)

    mask = np.logical_and(h_channel >= intervalo_inferior, h_channel <= intervalo_superior)

    h_channel[mask] = (h_channel[mask] + 90)

    hsv_img[:, :, 0] = h_channel

    rgb_img = cv.cvtColor(hsv_img, cv.COLOR_HSV2BGR)    

    cv.imwrite  ("rgb_img_fatia.jpg",rgb_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

main()
