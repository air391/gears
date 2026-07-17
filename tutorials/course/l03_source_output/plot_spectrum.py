"""Make the first per-event scintillator energy-deposition spectrum."""

from pathlib import Path
import sys

import awkward as ak
import matplotlib.pyplot as plt
import numpy as np
import uproot


root_path = Path(sys.argv[1] if len(sys.argv) > 1 else "l03_662keV.root")
with uproot.open(root_path) as root_file:
    tree = root_file["t"]
    deposited_keV = tree["et"].array()
    # GEARS reserves et[0] for all sensitive volumes; this checkpoint uses
    # the only sensitive scintillator, whose physical copy number is one.
    padded = ak.pad_none(deposited_keV, 2, axis=1)
    energy = ak.to_numpy(ak.fill_none(padded[:, 1], 0.0))

np.save("l03_662keV_edep_keV.npy", energy)
plt.hist(energy, bins=160, range=(0, 700), histtype="step", color="C0")
plt.xlabel("scintillator event energy deposition [keV]")
plt.ylabel("events / bin")
plt.tight_layout()
plt.savefig("l03_662keV_spectrum.png", dpi=160)
print(f"events={len(energy)}; nonzero={(energy > 0).sum()}; output=l03_662keV_spectrum.png")
