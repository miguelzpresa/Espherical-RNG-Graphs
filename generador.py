import numpy as np
from itertools import combinations
from scipy.special import comb
from numba import njit,prange
#import pandas as pd
import time
import argparse
import numpy as np
from numba import njit, prange
np.random.seed(20)

@njit(parallel=True, cache=True)
def pointd1(distri, grupo):
    points = np.zeros((grupo, 2))
    for i in prange(grupo):
        phi = round(np.arccos(1 - 2 * np.random.uniform(0, 1)), 4)
        theta = round(np.random.uniform(0, 2 * np.pi), 4)
        points[i, 0] = phi
        points[i, 1] = theta
    return points

@njit(parallel=True, cache=True)
def pointd2(distri, grupo):
    points = np.zeros((grupo, 2), dtype=np.float64)
    for i in prange(grupo):
        phi = round(np.random.uniform(0, np.pi), 4)
        theta = round(np.random.uniform(0, 2 * np.pi), 4)
        points[i, 0] = phi
        points[i, 1] = theta
    return points

parser = argparse.ArgumentParser()
parser.add_argument("--grupo", type=int, help="Número de grupos")
parser.add_argument("--distri", type=int, help="Tipo de distribución")
args = parser.parse_args()

grupo = args.grupo
distri = args.distri
n_g = 100000

P = list()
distancias = list()
c_dist_n = np.zeros(401, dtype=int)
c_dist = np.zeros(401, dtype=int)
c_bonds = np.zeros(5, dtype=int)
comblen = int(comb(grupo, 2))
#bonds = np.zeros((25000, comblen), dtype=int)
id_b =list()
rango =[ round(0+ 0.007854*(i),5) for i in range(0,401)]
id_id_b = np.zeros(25000, dtype=int)
aux1 = 0 # iterador para el arreglo de bonds
indices = np.array([24999, 49999, 74999, 99999])
nodes_data = {}

if distri == 1:
    pd = pointd1
    dis = ""
else:
    pd = pointd2
    dis = "-NON"

start_time = time.time()

for curr_g in range(n_g):
    points = pd(distri, grupo)
    P.append(points)
    nodes_data = {tuple(p):0 for p in list(points)}
    #bondss = np.zeros(comblen, dtype=int)
    aux2 = 0
    for i, pair in enumerate(combinations(points, 2)):
        bond = 1
        d = round(np.arccos(np.sin(pair[0][0]) * np.sin(pair[1][0]) * np.cos(pair[0][1] - pair[1][1]) + np.cos(pair[0][0]) * np.cos(pair[1][0])), 4)
        for point in points:
            if not np.array_equal(point, pair[0]) and not np.array_equal(point, pair[1]):
                d1 = round(np.arccos(np.sin(pair[0][0]) * np.sin(point[0]) * np.cos(pair[0][1] - point[1]) + np.cos(pair[0][0]) * np.cos(point[0])), 4)
                d2 = round(np.arccos(np.sin(pair[1][0]) * np.sin(point[0]) * np.cos(pair[1][1] - point[1]) + np.cos(pair[1][0]) * np.cos(point[0])), 4)
                if d1 < d and d2 < d:
                    bond = 0
                    c_dist_n[np.digitize(np.array([d]),rango)] += 1
                    break
        if bond == 1:
            aux2 += 1
            id_b.append(i)
            c_dist[np.digitize(np.array([d]),rango)] += 1
            distancias.append(d)
            for point in pair:
                nodes_data[tuple(point)] += 1

    id_id_b[aux1] = aux2 #----------------------------------------------aux es el susituto de len(temporal(distancias)),me ahorraria una variable y la operacion lens sobre distancias
    for val in nodes_data.values():
        c_bonds[val] += 1



    del nodes_data

    aux1 += 1
    if np.isin(curr_g, indices):
        P = np.array(P)
        id_b = np.array(id_b, dtype=int)
        distancias = np.array(distancias)
        np.save(f'Points-{grupo}{dis}-{str(curr_g)[:2]}-10_5.npy', P)
        np.save(f'Distancias-{grupo}{dis}-{str(curr_g)[:2]}-10_5.npy', distancias)

        np.save(f'bonds-{grupo}{dis}-{str(curr_g)[:2]}-10_5.gz', id_b)
        np.save(f'id_b-{grupo}{dis}-{str(curr_g)[:2]}-10_5.gz', id_id_b)

        del P, distancias, id_b, id_id_b
        P = list()
        distancias = list()
        id_b = list()
        id_id_b = np.zeros(25000, dtype=int)

        #bonds = np.zeros((25000, comblen), dtype=int)
        aux1 = 0
        if curr_g == 99999:
            np.save(f'Count-dist_n_-{grupo}{dis}-{str(curr_g)[:2]}-10_5.gz', c_dist_n)
            np.save(f'Count-dist-{grupo}{dis}-{str(curr_g)[:2]}-10_5.gz', c_dist)
            np.save(f'Count-bonds-{grupo}{dis}-{str(curr_g)[:2]}-10_5.gz', c_bonds)
            #np.save(f'Global_C-{grupo}-{str(curr_g)[:2]}-10_5.gz', np.concatenate(( c_bonds ,c_dist_n)))

end_time = time.time()
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time} segundos")

#python rng10.py --grupo 80 --distri 2
