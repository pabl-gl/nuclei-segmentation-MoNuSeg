import csv
import numpy as np
from p2.aux import gt_to_mask
from p2.paths import get_all_image_ids
from p2.io import load_case
from p2.evaluation import evaluate
from p2.plot import plot_contours

from p2.iterations import iteration_1
from p2.iterations import iteration_2
from p2.iterations import iteration_3
from p2.iterations import iteration_4



ITERATION = iteration_4
ITERATION_NAME = ITERATION.__name__


def summarize_from_csv(csv_path):
    dice_vals = []
    count_rel = []
    area_rel = []

    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dice_vals.append(float(row["dice"]))

            count_gt = float(row["count_gt"])
            if count_gt > 0:
                count_rel.append(
                    float(row["count_error"]) / count_gt * 100
                )

            mean_gt_area = float(row["mean_gt_area"])
            if mean_gt_area > 0:
                area_rel.append(
                    float(row["mean_area_error"]) / mean_gt_area * 100
                )

    print("\n====== RESULTADOS GLOBALES ======")
    print(f"Dice medio:         {np.mean(dice_vals):.4f} ± {np.std(dice_vals):.4f}")
    print(f"Error conteo medio: {np.mean(count_rel):.2f}%")
    print(f"Error área media:   {np.mean(area_rel):.2f}%")
    print("================================")


def evaluateToCsv(csv_path):
    image_ids = get_all_image_ids()
    all_results = []

    for img_id in image_ids:
        print(f"Procesando {img_id}...")

        # Cargar datos
        imgH, imgE, imgN, imgGT = load_case(img_id)

        # Segmentación
        mask_pred, _ = ITERATION(imgH)
        #plot_contours(img_id,mask_pred, gt_to_mask(imgGT>1))

        # Evaluación
        results = evaluate(mask_pred, imgGT)
        results["image_id"] = img_id

        all_results.append(results)

    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=all_results[0].keys()
        )
        writer.writeheader()
        writer.writerows(all_results)

    print(f"\nEvaluación completada sobre {len(all_results)} imágenes")
    print(f"Resultados guardados en: {csv_path}")


if __name__ == "__main__":
    csv_path = f"results/{ITERATION_NAME}.csv"
    evaluateToCsv(csv_path)
    summarize_from_csv(csv_path)
