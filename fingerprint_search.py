"""Fingerprint comparison script using ORB features and BFMatcher.

This module provides functions to extract ORB descriptors from
fingerprint images and compare them to calculate a similarity score.
It exposes a CLI that receives two images and prints whether they
match, based on a configurable threshold.
"""

from __future__ import annotations

import argparse
import cv2
from typing import Tuple, List


def extract_features(image_path: str) -> Tuple[List[cv2.KeyPoint], cv2.Mat]:
    """Load a fingerprint image and compute ORB keypoints and descriptors."""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"No se pudo leer la imagen: {image_path}")
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(image, None)
    return keypoints, descriptors


def match_fingerprints(reference: str, sample: str, ratio: float = 0.75) -> float:
    """Compute a similarity score between two fingerprint images.

    A score closer to 1 means the fingerprints are more similar.
    """
    _, des1 = extract_features(reference)
    _, des2 = extract_features(sample)
    if des1 is None or des2 is None:
        return 0.0
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
    matches = bf.knnMatch(des1, des2, k=2)
    good = [m for m, n in matches if m.distance < ratio * n.distance]
    return len(good) / max(len(matches), 1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Busca coincidencias entre huellas digitales")
    parser.add_argument("referencia", help="Ruta a la imagen de referencia")
    parser.add_argument("muestra", help="Ruta a la imagen a comparar")
    parser.add_argument("--umbral", type=float, default=0.3, help="Umbral de similitud (0-1)")
    args = parser.parse_args()
    score = match_fingerprints(args.referencia, args.muestra)
    if score >= args.umbral:
        print(f"Huellas coinciden ({score:.2f})")
    else:
        print(f"Huellas NO coinciden ({score:.2f})")


if __name__ == "__main__":
    main()
