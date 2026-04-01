# %% [markdown]
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/255ribeiro/cadquery_basics/blob/master/docs/tuto_colab/multi_pav_loft_.ipynb)

# %% [markdown]
# # Exercício resolvido: Pavimentos com Loft
# ## Fernando Ferraz Rbeiro
# 
# 
# 
# 

# %% [markdown]
# ### Instalação dos pacotes

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
import cadquery as cq
from cadquery_simpleviewer.viewer import show
import numpy as np

# %% [markdown]
# ### criação de caixas no cadquery

# %%
# ── Parâmetros ───────────────────────────────────────────────────────────────
cota_inicial  = 0
pap           = 18
n_pav         = 5
rot_inc       = 5
smooth_factor = 1 / (np.pi * 2)


# ══════════════════════════════════════════════════════════════════════════════
# VERSÃO 1 — rect com scale e rotação
# ══════════════════════════════════════════════════════════════════════════════
wp = cq.Workplane("XY")
print('loop start')
for i in range(n_pav + 1):
    cota_atual   = round(cota_inicial + pap * i, 2)
    scale_factor = np.abs(np.sin(i) * smooth_factor + 1)
    offset       = pap if i > 0 else 0
    print(f'wire {i} start')

    wire = (
        cq.Workplane("XY")
        .rect(30 * scale_factor, 40 * scale_factor)
        .wires().val()
        .rotate((0, 0, 0), (0, 0, 1), i * rot_inc)   # rotação no wire
        .translate((0, 0, cota_atual))                 # posiciona na cota
    )
    print(f'wire {i} added')

    wp = wp.add(wire).toPending()

result_rect = wp.loft()



# %%
show(result_rect, tessellation_tolerance=.2)

# %%
# ── Parâmetros ───────────────────────────────────────────────────────────────
cota_inicial  = 0
pap           = 18
n_pav         = 5
rot_inc       = 10
smooth_factor = 1 / (np.pi * 2)

# ══════════════════════════════════════════════════════════════════════════════
# VERSÃO 2 — perfil DXF com scale e rotação
# ══════════════════════════════════════════════════════════════════════════════
def scale_xy(shape, scale =[1,1,1], translate=[0,0,0]):
    """Scales X and Y and translates Z in a single matrix operation."""
    m = cq.Matrix([
        [scale[0],  0,        0,        translate[0]],
        [0,         scale[1], 0,        translate[1]],
        [0,         0,        scale[2], translate[2]],
        [0,         0,        0,        1           ]
    ])
    return shape.transformGeometry(m)

perfil      = cq.importers.importDXF("perfil_autocad.dxf", include=["profile_01"])
# perfil    = cq.importers.importStep("perfil.step").val().scale(0.001)
perfil_wire = perfil.wires().val()

wp = cq.Workplane("XY")
print('loop start')
for i in range(n_pav + 1):
    cota_atual   = round(cota_inicial + pap * i, 2)
    scale_factor = np.abs(np.sin(i) * smooth_factor + 1)
    print(f'start wire {i}')
    wire = (
        scale_xy(perfil_wire,
                 scale=(scale_factor, scale_factor, 1)
                 )
        .rotate((0, 0, 0), (0, 0, 1), i * rot_inc)   # rotação no wire
        .translate((0, 0, cota_atual))                 # posiciona na cota
    )
    print(f'wire {i} added')

    wp = wp.add(wire).toPending()

result_dxf = wp.loft()


# %%
show(result_dxf)


