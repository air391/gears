# L05 scan prototype: 100 incident energies to a spectrum stack

## Purpose

Produce a reproducible teaching prototype, not the final science response
format.  The scan includes both endpoints: `20 + 20*i keV`, `i = 0...99`, so
the last energy is 2 MeV.

## Demonstration

Put the distributed GDML beside this directory, then:

```bash
python3 generate_scan.py --events 5000
for macro in macros/E_*.mac; do PHYSLIST=FTFP_BERT_EMZ ../../../build/gears "$macro"; done
python3 analyse_scan.py
```

The macros contain explicit, distinct random seeds and write a
`scan_manifest.csv` alongside the source configuration.  Run in a fresh work
directory if a previous scan output exists.  Before scheduling all 100 points,
benchmark the low-energy endpoint on the course server: the supplied GRID10B
geometry has inherited tessellated overlaps and 20 keV was not yet fast enough
to complete in the interactive validation window.

## Expected evidence

- Exactly 100 macros and 100 ROOT files exist, from 20 keV through 2000 keV.
- Every ROOT file has tree `t` and vector branch `et`.
- The output PNG has truth energy on rows and deposited energy on columns.

## Scientific boundary

`response_matrix_prototype.npz` stores unnormalised bin counts with a
provisional 5 keV deposited-energy axis.  It does not yet define the official
file format, zero-deposition convention, efficiency normalisation, binning or
uncertainty report.  GEARS currently omits zero-step events from its ROOT tree,
so this prototype cannot infer an absolute efficiency.  Those requirements
need the science-analysis contract and, if required, an event-level output
extension.

## Homework comparison

Bring the manifest, one input spectrum, the matrix image, and a one-page
self-check that records GDML, code commit, source, physics list, seeds and
event count.

## Next diff

`course-l05-reference-run` will add a teacher-generated baseline only after
the response-format contract is approved.
