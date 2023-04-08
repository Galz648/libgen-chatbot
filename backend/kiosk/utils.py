from typing import List
from scipy import spatial

def cosine_similarity(A: List[float], B: List[float]):
    return 1 - spatial.distance.cosine(A, B)
