import numpy as np
import cv2 as cv


def main():
    m = 100
    x = 10

    if(m+x>360  ):
        intervalo_superior = (m+x)% 360
        intervalo_inferior = abs(m-x)
        #falta o inferior
    else:
        intervalo_superior = m+x
        intervalo_inferior =  m-x

    img = cv.imread("flor.jpg")
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_channel = hsv_img[:, :, 0]  # Canal H (Matiz)

    mask = np.logical_and(h_channel >= intervalo_inferior, h_channel <= intervalo_superior)
    h_channel[mask] = h_channel[mask] +180

    print(h_channel[mask])

    hsv_img[:, :, 0] = h_channel

    rgb_img = cv.cvtColor(hsv_img, cv.COLOR_HSV2BGR)

    cv.imwrite  ("rgb_img_fatia.jpg",rgb_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

main()
