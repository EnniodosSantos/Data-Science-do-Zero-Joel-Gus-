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

Matrix = List[List[float]]

from typing import Tuple
def shape(A: Matrix) -> Tuple[int, int]:
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 #numero de elementos na primeira linha
    return num_rows, num_cols

def get_row(A: Matrix, i:int) -> Vector:
    return A[i]

def get_column(A: Matrix, j:int) -> Vector:
    return [A_i[j] for A_i in A]

from typing import Callable

def make_matrix(num_rows:int,
                num_cols:int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    return[[entry_fn(i,j) #com i, crie uma lista
            for j in range(num_cols)] 
           for i in range(num_rows)] #crie uma lista para cada i

def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)
    