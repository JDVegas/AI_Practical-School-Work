#__________ 2_green_screen_SOL1 __________#
# _ Durand--Vegas Johann _

# Utilisation d'histogrammes construits à partir de patchs

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Chargement des vidéos
gs_cap = cv2.VideoCapture("green_screen_Alpaca.mov")
bg_cap = cv2.VideoCapture("milky_way.mp4")

# Paramètres de la vidéo de sortie
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
dimensions = (int(gs_cap.get(3)),int(gs_cap.get(4)))
out = cv2.VideoWriter('OUT_SOL1.mp4', fourcc, 30, dimensions)

while bg_cap.isOpened():
    # Lire les images
    gs_ret, gs_frame = gs_cap.read()
    bg_ret, bg_frame = bg_cap.read()
        
    # Creer un patch
    patch = gs_frame[50:100, 50:100]

    
    channels = [0,1] # channels
    sizes = [256, 256] # size per-channel
    ranges = [0, 255, 0, 255] # ranges of values per-channel
    
    # Build histograms:
    hist = cv2.calcHist([patch], channels, None, sizes, ranges)

    # Compute the histogram back projection:
    lhMap = cv2.calcBackProject([gs_frame], channels, hist, ranges, 255)

    # Automatic threshold _ Methode Otsu
    ret,mask = cv2.threshold(lhMap,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    #Creation de copies
    gs_frame_M = np.copy(gs_frame)
    bg_frame_M = np.copy(bg_frame)
    
    # Application du mask
    gs_frame_M[mask != 0] = [0,0,0]
    bg_frame_M[mask == 0] = [0,0,0]
    
    # Assemblage final
    Final_image = gs_frame_M + bg_frame_M

    # Affichage des résultats et enregistrement
    out.write(Final_image)
    cv2.imshow('Result_Sol1', Final_image)

    if cv2.waitKey(1) == ord('q'):
        break
    
gs_cap.release()
bg_cap.release()
out.release()
cv2.destroyAllWindows()

""" Cette solution n'est pas très efficace. La seconde solution est un peu plus
performante. """
