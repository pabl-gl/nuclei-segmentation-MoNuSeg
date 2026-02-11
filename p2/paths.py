from pathlib import Path

BASE = Path("../Material Celulas")
#PATH_H=Path("../set1")
#PATH_H=Path("../set2")
PATH_H = Path("../Material Celulas/H")
PATH_E = BASE / "E"
PATH_NORM = BASE / "normalizadas"
PATH_GT = BASE / "gt_id"

def get_all_image_ids():
    return sorted([
        p.name for p in PATH_H.iterdir()
        if p.suffix == ".png"
    ])
