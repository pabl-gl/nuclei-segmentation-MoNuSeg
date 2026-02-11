import matplotlib.pyplot as plt
from skimage.measure import find_contours


def plot_pipeline(name,img_processed, mask_pred, mask_gt):
    fig, axs = plt.subplots(1, 3, figsize=(12, 5))
    fig.suptitle(name)
    axs[0].imshow(img_processed, cmap="gray")
    axs[0].set_title("Processed")
    axs[0].axis("off")

    axs[1].imshow(mask_pred, cmap="gray",vmin=0, vmax=1)
    axs[1].set_title("Processed Mask")
    axs[1].axis("off")

    axs[2].imshow(mask_gt, cmap="gray")
    axs[2].set_title("GT Mask")
    axs[2].axis("off")
    plt.tight_layout()
    plt.show()


def plot_contours(name,mask_pred, mask_gt):
    contours_pred = find_contours(mask_pred, 0.5)
    contours_gt = find_contours(mask_gt, 0.5)

    fig, axs = plt.subplots(1, 3, figsize=(18, 7))
    fig.suptitle(name)
    axs[0].imshow(mask_pred, cmap='gray',vmin=0, vmax=1)
    axs[0].set_title("Predicted Mask")
    axs[0].axis("off")
    axs[1].imshow(mask_gt, cmap='gray',vmin=0, vmax=1)
    axs[1].set_title("Ground Truth Mask")
    axs[1].axis("off")
    axs[2].imshow(mask_gt, cmap='gray')

    for c in contours_gt:
        axs[2].plot(c[:, 1], c[:, 0], '-g', linewidth=1.3)
    for c in contours_pred:
        axs[2].plot(c[:, 1], c[:, 0], '-r', linewidth=1.2)

    axs[2].set_title("Contours on GT: GT (green) vs Pred (red)")
    axs[2].axis("off")

    plt.tight_layout()
    plt.show()
