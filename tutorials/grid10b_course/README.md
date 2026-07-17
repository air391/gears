# GRID10B course tutorial

This is the only GEARS entry point after the B1 lessons.

1. Put `GRID10B.gdml` and its `GRID10B/` dependency directory here.
2. Build the fixed course commit and run `baseline.mac`.
3. Confirm geometry orientation visually and run the overlap test.
4. Read the two hooks in `gears.cc`: exact-name sensitive selection and
   `BuildGRID10BCourseWorld()`.

The source changes `CRYSTAL001_GAGGCe` to
`G4_PLASTIC_SC_VINYLTOLUENE`, then wraps the GDML geometry in a larger vacuum
world so a 400 mm aluminium support can be added.  The provisional +z support
position and GPS direction must be verified together before production use.

Required evidence: a clean overlap check, startup material printout, and
event-level target energy in the ROOT `et[1]` array.
