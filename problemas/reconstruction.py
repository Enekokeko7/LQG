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

P = pr.reconstruct(unormals,areas)

vertices = np.array(P.vertices)
vol = P.volume

np.savetxt("/Users/enekoaranguren/Documents/lqg/vertices.csv", vertices, delimiter=',')
np.savetxt("/Users/enekoaranguren/Documents/lqg/volume.csv", vol[None], delimiter=',')

faces = np.zeros((len(normals),len(normals)), dtype=object)
for ii in range(len(normals)):
    for jj in range(len(P.faces[ii].vertices)):
        faces[ii,jj] = P.faces[ii].vertices[jj]+1

np.savetxt("/Users/enekoaranguren/Documents/lqg/faces.csv", faces, delimiter=',')
