# %% [markdown]
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/255ribeiro/cadquery_basics/blob/master/docs/tuto_colab/multi_pav_cq_ramdom_disp_resolvido.ipynb)

# %% [markdown]
# # Exercício resolvido: Pavimentos deslocados
# ## Fernando Ferraz Rbeiro
# 
# 
# 
# 

# %% [markdown]
# #### Instalação dos pacotes

# %%
import sys
IN_COLAB = 'google.colab' in sys.modules
if IN_COLAB:
    print("Running in Colab, installing packages...")
    !pip install cadquery cadquery-simpleviewer
else:
    print("Not running in Colab, skipping package installation.")

# %% [markdown]
# ### Importação dos pacotes

# %%
import itertools
import cadquery as cq
from cadquery_simpleviewer.viewer import show
import numpy as np


# %%
cota_inicial = 0
pap = 3
n_pav = 30
displace = 3

### --- code
displace_dir = np.array([-1, 0, 1])

lista_pav = []
for i in range(n_pav + 1):

  # direções de deslocamento
  dir_x = np.random.choice(displace_dir) * displace
  # dir_y = np.random.choice(displace_dir) * displace


  cota_atual =   cota_inicial + (pap * i)
  cota_atual = round(cota_atual, 2)
  # criar caixa na cota atual
  box = cq.Workplane("XY").box(30 , 30, pap, centered=[True, True, False]).translate((dir_x, 0, cota_atual))

  lista_pav.append(box)
  # print(f"Cota do pavimento {i} = {cota_atual}")
# print(lista_pav)

show(lista_pav)

# %%
# Create an assembly and add the objects
assy = cq.Assembly()
for i in range(len(lista_pav)):
    assy.add(lista_pav[i], name=f'pav_{i}')

# Export the assembly to a STEP file
assy.export(
    "output.step", 
    mode="default" # ou mode = "fused" para extrair os objetos unidos (solid union)
    )


