# L03 start: compile and run an existing GEARS example

## Purpose

Prove that the single-file GEARS application builds against the course Geant4
installation before changing any detector, source or output code.

## Demonstration

From the repository root, build with the command in `tutorials/course/README.md`,
then run:

```bash
cd tutorials/output
../../build/gears radiate.mac
```

## Expected evidence

- The process exits successfully and writes `gears.root` after the recording
  run in `radiate.mac`.
- The existing `HPGe(S)` sensitive-volume convention produces an `et` branch.

## Homework comparison

Students keep this checkout as their GEARS starting point, build it on their
own branch, and save the exact commit, macro and run log.  The next checkpoint
replaces this broad upstream example with the course's fixed-direction gamma
source.

## Next diff

Compare this checkpoint with `course-l03-source-output`.
