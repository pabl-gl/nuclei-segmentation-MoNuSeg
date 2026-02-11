from p2.evaluation import evaluate, print_evaluation
from p2.aux import gt_to_mask
from p2.io import load_case
from p2.iterations import *
from p2.plot import plot_pipeline, plot_contours


if __name__ == "__main__":

    img_id= "TCGA-A7-A13E-01Z-00-DX1.png"
    imgH, imgE, imgN, imgGT = load_case(img_id)

    mask_pred, processedImage = iteration_1(imgH)

    results = evaluate(mask_pred, imgGT)
    print_evaluation(results)

    plot_pipeline(img_id,processedImage, mask_pred,gt_to_mask(imgGT))
    plot_contours(img_id,mask_pred,gt_to_mask(imgGT))

