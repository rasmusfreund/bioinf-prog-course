
import math
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 

import Bio.PDB

def degrees(rad_angle) :
    """Converts any angle in radians to degrees.
    If the input is None, then it returns None.
    For numerical input, the output is mapped to [-180,180]
    """
    if rad_angle is None :
        return None
    angle = rad_angle * 180 / math.pi
    while angle > 180 :
        angle = angle - 360
    while angle < -180 :
        angle = angle + 360
    return angle


models = Bio.PDB.PDBParser().get_structure("1HMP", "1HMP.pdb")
chain = models[0]
polypeptides = Bio.PDB.PPBuilder().build_peptides(chain)
poly = polypeptides[0]

phi_list = []
psi_list = []
for phi, psi in poly.get_phi_psi_list():
    if phi is not None and psi is not None:
        phi_list.append(degrees(phi))
        psi_list.append(degrees(psi))

ax = sns.kdeplot(np.array(phi_list), np.array(psi_list),
                 cmap="Reds", shade=True, shade_lowest=False)
plt.scatter(np.array(phi_list), np.array(psi_list), marker="x")
plt.title("Ramachandran plot")
plt.xlabel(r'$\Psi$')
plt.ylabel(r'$\Phi$')
plt.show()














#ax = sns.kdeplot(np.array(psi_list))



# for model in Bio.PDB.PDBParser().get_structure("1HMP", "1HMP.pdb") :
#     for chain in model :
#         polypeptides = Bio.PDB.PPBuilder().build_peptides(chain)
#         for poly_index, poly in enumerate(polypeptides):
#             print("Model {} Chain {}".format(str(model.id), str(chain.id)))
#             print("(part {} of {})".format(poly_index+1, len(polypeptides)))
#             print("length {}".format(len(poly)))
#             print("from {}{}".format(poly[0].resname, poly[0].id[1]))
#             print("to {}{}".format(poly[-1].resname, poly[-1].id[1]))
#             phi_psi = poly.get_phi_psi_list()
#             for res_index, residue in enumerate(poly) :
#                 res_name = "{}{}".format(residue.resname, residue.id[1])
#                 print(res_name, phi_psi[res_index])



