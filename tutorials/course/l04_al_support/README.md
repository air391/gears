# L04 aluminium support: an explicit C++ detector addition

## Purpose

Add a `400 × 400 × 400 mm³` `G4_Al` support after GDML import.  The model's
native envelope is only 50 mm thick, so both the assembly and support are
siblings in `GRID10B_course_world`.

## Demonstration

Place the distributed `GRID10B.gdml` and `GRID10B/` dependency directory
beside `baseline.mac`, then run:

```bash
cd tutorials/course/l04_al_support
PHYSLIST=FTFP_BERT_EMZ ../../../build/gears baseline.mac
```

`supportSide` and `supportCenter` at the top of `BuildGRID10BImportWorld()`
are the only intended geometry-edit parameters.  The current `(0, 0, 225 mm)`
placement makes the support touch the imported envelope at its +z face.

## Expected evidence

- The baseline GDML's inherited overlap messages are retained, but the log has
  no overlap mentioning `GRID10B_aluminium_support`.
- Startup prints the target-material and `et[1]` mapping line.
- A visual check confirms that +z is the intended physical back face before
  this configuration is used for any reference result.

## Homework comparison

Preserve the source and physics configuration, make exactly one geometry
change, re-run overlap checking against the inherited baseline, and compare
the target `et[1]` spectrum.

## Next diff

Compare this checkpoint with `course-l05-scan-prototype`.
