import numpy as np
import cv2 as cv


def main():
    m = 100
    x = 200

    if(m+x>360  ):
        intervalo_superior = (m+x)% 360
        #falta o inferior
    else:
        intervalo_superior = m+x
        intervalo_inferior =  m-x

    img = cv.imread("praia.jpg")
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imwrite  ("hsv_img.jpg",hsv_img)

    h_channel = hsv_img[:, :, 0]  # Canal H (Matiz)

    mask = np.logical_and(h_channel >= intervalo_inferior, h_channel <= intervalo_superior)

    h_channel[mask] = h_channel[mask] + 180
    hsv_img[:, :, 0] = h_channel

    cv.imwrite  ("hsv_img_fatia.png",hsv_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

main()