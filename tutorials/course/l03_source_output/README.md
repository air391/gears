# L03 source and output: a 662 keV parallel gamma beam

## Purpose

Replace the upstream isotropic HPGe tutorial with the course's minimal,
normally incident gamma measurement.  The source and output are controlled by
the macro; unchanged GEARS reads the physics-list name from `PHYSLIST` when
the process starts.

## Demonstration

```bash
cd tutorials/course/l03_source_output
PHYSLIST=FTFP_BERT_EMZ ../../../build/gears gamma_662keV.mac
python3 plot_spectrum.py l03_662keV.root
```

Use a Python environment containing `uproot`, `awkward`, `numpy` and
`matplotlib`.  The main analysis quantity is the event-level `et[1]` value.

## Expected evidence

- Startup identifies `FTFP_BERT_EMZ` in the physics-list log.
- `l03_662keV.root` contains tree `t` and branch `et`.
- `l03_662keV_spectrum.png` is a non-empty energy-deposition spectrum.
- GEARS writes only events that contain recorded steps; this first spectrum is
  therefore a distribution of recorded events, not an absolute efficiency.

## Homework comparison

Change exactly one source parameter (for example gamma energy), preserve the
macro and log, and explain the spectrum change.  Record commit, seed policy,
event count and physics-list name.

## Next diff

Compare this checkpoint with `course-l04-gdml-import`.
