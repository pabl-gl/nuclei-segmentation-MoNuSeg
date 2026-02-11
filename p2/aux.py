import numpy as np
from skimage.measure import regionprops

def extract_metrics(mask):
    props = regionprops(mask)
    areas = [int(p.area) for p in props]
    num = len(areas)
    mean_area = np.mean(areas) if areas else 0
    return num, areas, mean_area

def print_metrics(img):
    num, areas, area_mean = extract_metrics(img)
    print("Núcleos:", num)
    print("Primeras áreas:", areas[:10])
    print("Área media:", area_mean)

def gt_to_mask(gt_id): return gt_id > 0