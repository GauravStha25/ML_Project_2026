from PIL import Image
import numpy as np
import tifffile as tiff

img = tiff.imread("C:\\Users\\dance\\OneDrive\\Documents\\Python\\ML_Project_2026\\Images\\20260923-cldn-lyn2-GFP-col28a2a-lyn2-mKate-31-33-hpf\\Position 1\\20260923-cldn-lyn2-GFP-col28a2a-lyn2-mKate-31-33-hpf-4pos1.tif")
print(img.shape)

img_pil = Image.open("C:\\Users\\dance\\OneDrive\\Documents\\Python\\ML_Project_2026\\Images\\20260923-cldn-lyn2-GFP-col28a2a-lyn2-mKate-31-33-hpf\\Position 1\\20260923-cldn-lyn2-GFP-col28a2a-lyn2-mKate-31-33-hpf-4pos1.tif")
img_pil.show()


x=0