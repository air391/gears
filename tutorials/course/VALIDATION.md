# Cat-docker validation record

Validated on the shared Geant4 11.4.1 installation as a normal user, without
`sudo`.  This file records observed behavior, rather than treating a tutorial
checkpoint as a detector-calibration result.

## Required environment

```bash
source /opt/geant4-v11.4.1-install/bin/geant4.sh
cmake -S . -B build -DCMAKE_PREFIX_PATH="/opt/geant4-v11.4.1-install;/opt/expat-2.6.4;/opt/xerces-c-3.2.5" -DEXPAT_ROOT=/opt/expat-2.6.4
cmake --build build -j4
```

The explicit Expat prefix is necessary: the operating-system Expat is 2.4.7,
whereas the Geant4 configuration requires at least 2.5.0.

## Observed results

| Item | Result | Evidence / limitation |
| --- | --- | --- |
| Official B1 | pass | Fresh copy, configure, build and `run1.mac` batch run complete. |
| GEARS L03 | pass | `PHYSLIST=FTFP_BERT_EMZ` and `gamma_662keV.mac` write ROOT; uproot/awkward produces a spectrum. |
| GRID10B import | pass with inherited warnings | The compatibility-material table permits import.  The supplied tessellated GDML reports internal overlaps before any course support is added. |
| Target material and `et[1]` | pass | Startup confirms the exact target mapping; a 662 keV run contained non-zero `et[1]` values. |
| Aluminium support | pass against baseline | The support itself was absent from the overlap messages; physical back-face orientation still requires a visual check. |
| L05 macro generation | pass | 100 macros are generated for 20--2000 keV with distinct seeds. |
| L05 full scan | not yet a reference run | A 20 keV event did not complete in the interactive validation window on the overlapped GRID10B geometry.  Establish a low-energy runtime budget and final analysis contract before publishing a reference matrix. |

## Python environment

The server did not initially contain `uproot` or `awkward`.  A user-owned
virtual environment successfully installed `uproot`, `awkward`, `numpy` and
`matplotlib`; this is a course prerequisite to document separately from the
GEARS repository.
