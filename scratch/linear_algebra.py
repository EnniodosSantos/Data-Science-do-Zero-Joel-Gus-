from typing import List
Vetor = List[float]

def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return[v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors: List[Vector]) -> Vector:
    #verifica se estão vazios
    assert vetores

    #verfica se os vetores tem o mesmo tamanho
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vetores) #"different sizes"

    return[sum(vector[i] for vetor in vetores)
        for i in range(num_eleme)]

def scalar_multiply(c: float, v: Vector) -> Vetor:
    return [c * v_i for v_i in v]
    
def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1/n, vetor_soma(vetores))

def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w)
    return sum(v_i * w_i for v_i, w_i in zip(v,w))

def sum_of_squares(v: Vector) -> float:
    return dot(v, v)

import math

def magnitude(v: Vector) -> float:

  return math.sqrt(sum_of_squares(v))
    
def squared_distance(v: Vector, w: Vector) -> float:
  return sum_of_squares(subtract(v,w))

def distance(v: Vector,w: Vector) -> float:
    return math.sqrt(squared_distance(v,w))

#ou facilitando

def distance(v: Vector,w: Vector) -> float:
  return magnitude(subtracao(v,w))