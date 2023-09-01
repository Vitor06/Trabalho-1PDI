import argparse
import numpy as np
import cv2 as cv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--m", help="Escolha o valor de M (Inteiro 0 <= m <= 360)", required=True)
    parser.add_argument("-x", "--x", help="Escolha o valor de X (Inteiro 0 <= x <= 179)", required=True)
    parser.add_argument("-im", "--imagem", help="Defina o nome do arquivo (com extensao) a ser utilizado e contido "
                                                "na pasta raiz", required=True)
    args = parser.parse_args()

    m = int(args.m)
    x = int(args.x)
    filename = args.imagem

    erro = False
    if m < 0 or m > 360:
        print("ERRO: Valor de M fora do intervalo permitido")
        erro = True
    if x < 0 or x > 179:
        print("ERRO: Valor de X fora do intervalo permitido")
        erro = True
    if not "." in filename:
        print("ERRO: Arquivo sem extensao definida")
        erro = True
    if erro:
        return 1

    img = cv.imread(filename)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_channel = hsv_img[:, :, 0]  # Canal H (Matiz)

    if m+x > 360:
        intervalo_inferior = (m - x) // 2
        intervalo_superior = ((m + x) % 360) // 2
        mask = np.logical_and(h_channel <= intervalo_inferior, h_channel >= intervalo_superior)
    elif m-x < 0:
        intervalo_inferior = (m + x) // 2
        intervalo_superior = ((m - x) + 360) // 2
        mask = np.logical_and(h_channel >= intervalo_inferior, h_channel <= intervalo_superior)
    else:
        intervalo_inferior = (m - x) // 2
        intervalo_superior = (m + x) // 2
        mask = np.logical_and(h_channel >= intervalo_inferior, h_channel <= intervalo_superior)

    h_channel[mask] = (h_channel[mask] + 90)

    hsv_img[:, :, 0] = h_channel

    rgb_img = cv.cvtColor(hsv_img, cv.COLOR_HSV2BGR)    

    cv.imwrite("modificado_" + filename, rgb_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

main()
