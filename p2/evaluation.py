import numpy as np
from skimage.measure import label
from p2.aux import extract_metrics


def dice_object_level(pred_mask, gt_mask):
    pred_lab=pred_mask
    # Flatten
    gt_f = gt_mask.ravel()
    pred_f = pred_lab.ravel()

    # Build intersection matrix using bincount
    max_gt = gt_f.max() + 1
    max_pred = pred_f.max() + 1

    inter = np.bincount(
        gt_f * max_pred + pred_f,
        minlength=max_gt * max_pred
    )
    inter = inter.reshape(max_gt, max_pred)

    # Compute areas
    area_gt = np.bincount(gt_f, minlength=max_gt)
    area_pred = np.bincount(pred_f, minlength=max_pred)

    # Dice matrix
    dice_mat = 2 * inter / (area_gt[:, None] + area_pred[None, :] + 1e-8)

    # Remove background row/column
    dice_mat = dice_mat[1:, 1:]

    # GT → Pred
    dice_gt = dice_mat.max(axis=1)

    # Pred → GT
    dice_pred = dice_mat.max(axis=0)

    return 0.5 * (dice_gt.mean() + dice_pred.mean())


def evaluate(processedMask, gt_id):
    # --- Métricas por objeto ---
    num_pred, pred_areas, mean_pred_area = extract_metrics(processedMask)
    num_gt, gt_areas, mean_gt_area = extract_metrics(gt_id)

    dice = dice_object_level(processedMask, gt_id)
    count_error = abs(num_pred - num_gt)
    mean_area_error = abs(mean_pred_area - mean_gt_area)

    return {
        "dice": dice,

        "count_pred": num_pred,
        "count_gt": num_gt,
        "count_error": count_error,

        "mean_pred_area": mean_pred_area,
        "mean_gt_area": mean_gt_area,
        "mean_area_error": mean_area_error
    }



def print_evaluation(results):
    count_pred = results['count_pred']
    count_gt   = results['count_gt']
    count_err  = results['count_error']

    mean_pred = results['mean_pred_area']
    mean_gt   = results['mean_gt_area']
    mean_err  = results['mean_area_error']

    count_pct = (count_err / count_gt * 100) if count_gt != 0 else 0
    mean_pct  = (mean_err  / mean_gt * 100) if mean_gt != 0 else 0

    print("\n" + "=" * 50)
    print("        EVALUACIÓN")
    print("=" * 50)

    print("\n--- SEGMENTACIÓN ---")
    print(f"Dice:                {results['dice']:.4f}")

    print("--- CONTEO DE NÚCLEOS ---")
    print(f"Núcleos predichos:   {count_pred}")
    print(f"Núcleos GT:          {count_gt}")
    print(f"Error absoluto:      {count_err}")
    print(f"Error relativo:      {count_pct:.2f}%\n")

    print("--- MEDICIÓN DE ÁREAS ---")
    print(f"Área media predicha: {mean_pred:.3f}")
    print(f"Área media GT:       {mean_gt:.3f}")
    print(f"Error absoluto:      {mean_err:.3f}")
    print(f"Error relativo:      {mean_pct:.2f}%")

    print("=" * 50 + "\n")
