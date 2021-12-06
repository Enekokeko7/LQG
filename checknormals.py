import polyhedrec as pr
import numpy as np

f = open('normals.txt', 'r')

content = f.read()
content = content.strip('][').split(',')


for ii in range(len(content)):
    content[ii] = float(content[ii])

normals, unormals, areas = [], [], []

for ii in range(int(len(content)/3)):
    line = [content[3*ii], content[3*ii+1], content[3*ii+2]]
    mod = np.linalg.norm(line)

    normals.append(line)
    unormals.append(line/mod)
    areas.append(mod)

suma = [a*u for a,u in zip(areas,unormals)]
suma = sum(suma)
print(suma)
