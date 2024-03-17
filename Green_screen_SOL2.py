#__________ 2_green_screen_SOL2 __________#
# _ Durand--Vegas Johann _

# Utilisation d'un mask établit à partir de bornes colorées

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Chargement des vidéos
gs_cap = cv2.VideoCapture("green_screen_Alpaca.mov")
bg_cap = cv2.VideoCapture("milky_way.mp4")

# Paramètres de la vidéo de sortie
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
dimensions = (int(gs_cap.get(3)),int(gs_cap.get(4)))
out = cv2.VideoWriter('OUT_SOL2.mp4', fourcc, 30, dimensions)

while bg_cap.isOpened():
    # Lire les images
    gs_ret, gs_frame = gs_cap.read()
    bg_ret, bg_frame = bg_cap.read()
    
    # Creer des bornes
    low_green = np.array([0,100, 0])
    upper_green = np.array([100, 255, 100])
    
    # Créer le mask
    mask = cv2.inRange(gs_frame, low_green, upper_green)
    
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
    cv2.imshow('Result_Sol2', Final_image)

    if cv2.waitKey(1) == ord('q'):
        break
    
gs_cap.release()
bg_cap.release()
out.release()
cv2.destroyAllWindows()


""" Cette solution a un rendu moins grossier que la solution 1. Il reste cependant un léger halo vert sur le contour du Lama. """
