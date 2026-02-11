import numpy as np
from scipy.ndimage import label
from skimage.color import rgb2gray
from skimage.filters import gaussian, threshold_local
from skimage.morphology import dilation, disk
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
from scipy import ndimage as ndi

from skimage.measure import label

def iteration_1(imgH):
    H = rgb2gray(imgH).astype(np.float32)
    filt = gaussian(H, 3.5)

    t = threshold_local(
        filt,
        block_size=55,   # depende del tamaño nuclear
        offset=0.15# desplaza el umbral hacia núcleos
    )

    mask = filt < t
    labels = label(mask)

    return labels, filt

def iteration_2(imgH):
    H = rgb2gray(imgH).astype(np.float32)
    filt = gaussian(H, 3.5)

    t = threshold_local(
        filt,
        block_size=55,   # depende del tamaño nuclear
        offset=0.15 # desplaza el umbral hacia nucleos
    )

    mask = filt < t
    mask = dilation(mask, disk(2))
    labels = label(mask)

    return labels, filt


def iteration_3(img):
    H = rgb2gray(img).astype(np.float32)
    filt = gaussian(H, 4.5)

    t = threshold_local(
        filt,
        block_size=81,
        offset=0.10
    )

    mask = filt < t
    mask = dilation(mask, disk(2))
    labels = label(mask)

    return labels, filt



def iteration_4(img):
    H = rgb2gray(img).astype(np.float32)
    filt = gaussian(H, sigma=4.5)

    t = threshold_local(
        filt,
        block_size=81,
        offset=0.10
    )

    mask = filt < t
    mask = dilation(mask, disk(2))

    dist = ndi.distance_transform_edt(mask)

    peaks = peak_local_max(
        dist,
        min_distance=16,   # controla sobresegmentación
        labels=mask
    )

    markers = np.zeros_like(mask, dtype=np.int32)
    for i, (r, c) in enumerate(peaks, start=1):
        markers[r, c] = i

    # --- Watershed ---
    labels_ws = watershed(-dist, markers, mask=mask)

    return labels_ws, filt


