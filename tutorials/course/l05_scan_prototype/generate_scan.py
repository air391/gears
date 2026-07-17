"""Generate the 100 fixed-energy GEARS macros for the course scan."""

from pathlib import Path
import argparse
import csv


parser = argparse.ArgumentParser()
parser.add_argument("--events", type=int, default=5000)
parser.add_argument("--out", type=Path, default=Path("macros"))
args = parser.parse_args()

args.out.mkdir(parents=True, exist_ok=True)
energies_keV = [20 + 20 * index for index in range(100)]
with (args.out / "scan_manifest.csv").open("w", newline="") as manifest:
    writer = csv.DictWriter(manifest, fieldnames=["index", "energy_keV", "events", "macro", "root"])
    writer.writeheader()
    for index, energy in enumerate(energies_keV):
        stem = f"E_{energy:04d}keV"
        macro = args.out / f"{stem}.mac"
        macro.write_text(
            f"""/control/verbose 1
/random/setSeeds {100000 + 2 * index} {100001 + 2 * index}
/geometry/source GRID10B.gdml
/run/initialize
/gps/particle gamma
/gps/energy {energy} keV
/gps/pos/type Plane
/gps/pos/shape Square
/gps/pos/centre 0 0 -500 mm
/gps/pos/halfx 250 mm
/gps/pos/halfy 250 mm
/gps/direction 0 0 1
/tracking/verbose 0
/analysis/setFileName {stem}.root
/run/printProgress 1000
/run/beamOn {args.events}
""",
            encoding="utf-8",
        )
        writer.writerow(
            {"index": index, "energy_keV": energy, "events": args.events,
             "macro": macro.name, "root": f"{stem}.root"}
        )

print(f"wrote {len(energies_keV)} macros to {args.out}")
