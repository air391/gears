"""Stack fixed-energy GEARS spectra into a teaching response-matrix prototype."""

from pathlib import Path
import csv

import awkward as ak
import matplotlib.pyplot as plt
import numpy as np
import uproot


macro_dir = Path("macros")
with (macro_dir / "scan_manifest.csv").open(newline="") as manifest:
    rows = list(csv.DictReader(manifest))

# A provisional 0--2 MeV, 5 keV deposited-energy axis.  This is deliberately
# not a promised science data format or an efficiency-normalised response.
deposited_edges_keV = np.linspace(0, 2000, 401)
matrix = []
true_energies_keV = []
for row in rows:
    root_path = Path(row["root"])
    if not root_path.exists():
        raise FileNotFoundError(f"missing scan output: {root_path}")
    with uproot.open(root_path) as root_file:
        et = root_file["t"]["et"].array()
    target_energy = ak.to_numpy(ak.fill_none(ak.pad_none(et, 2, axis=1)[:, 1], 0.0))
    matrix.append(np.histogram(target_energy, bins=deposited_edges_keV)[0])
    true_energies_keV.append(float(row["energy_keV"]))

matrix = np.asarray(matrix)
np.savez(
    "response_matrix_prototype.npz",
    true_energies_keV=np.asarray(true_energies_keV),
    deposited_edges_keV=deposited_edges_keV,
    counts=matrix,
)

image = plt.pcolormesh(
    deposited_edges_keV,
    np.asarray(true_energies_keV),
    np.maximum(matrix, 1),
    shading="auto",
    norm="log",
)
plt.colorbar(image, label="events / deposited-energy bin")
plt.xlabel("deposited energy [keV]")
plt.ylabel("true gamma energy [keV]")
plt.tight_layout()
plt.savefig("response_matrix_prototype.png", dpi=180)
print(f"matrix={matrix.shape}; output=response_matrix_prototype.png")
