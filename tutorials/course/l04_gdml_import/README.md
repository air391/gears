# L04 GDML import: preserve the model, enlarge its world

## Purpose

Import the supplied `GRID10B.gdml` without editing its XML.  The checkpoint
wraps its native envelope in a 1 m vacuum world so later C++ additions have a
valid common mother volume.

## Demonstration

Copy the distributed `GRID10B.gdml` and its `GRID10B/` directory beside this
macro, then run:

```bash
cd tutorials/course/l04_gdml_import
PHYSLIST=FTFP_BERT_EMZ ../../../build/gears import_check.mac
```

For a visual inspection, start GEARS without a macro and execute the commented
visualisation commands after `import_check.mac` has initialised the geometry.

## Expected evidence

- `/geometry/test/run` is saved as a baseline.  The supplied tessellated GDML
  already reports several internal overlaps; this checkpoint must not add an
  overlap for `GRID10B_assembly` or the outer course world.
- Startup reports the named GDML compatibility-material table; the distributed
  XML remains unchanged.  These aliases are an import baseline, not final
  material calibration.
- The imported assembly is visible inside `GRID10B_course_world`.
- The distributed GDML remains unmodified and is not staged in Git.

## Homework comparison

Save the overlap log and one geometry screenshot.  Locate the four candidate
logical-volume names before selecting a sensitive crystal in the next step.

## Next diff

Compare this checkpoint with `course-l04-target-material`.
