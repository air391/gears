# L04 target material: select one imported crystal in C++

## Purpose

The original GRID10B GDML has no GEARS `(S)` sensitive-volume marker.  This
checkpoint selects exactly the logical volume `CRYSTAL001_GAGGCe`, changes
only it to `G4_PLASTIC_SC_VINYLTOLUENE`, verifies it has one placement, and
assigns that placement copy number one.  Its event total is therefore `et[1]`.

## Demonstration

Use the distributed GDML and `import_check.mac` from the previous checkpoint.
At startup, require this line:

```text
GEARS course: CRYSTAL001_GAGGCe -> G4_PLASTIC_SC_VINYLTOLUENE, et[1]
```

Then use the L03 gamma macro with `GRID10B.gdml` as its geometry source and
inspect branch `et` with the Python reader.

## Expected evidence

- A missing or shared target stops the run rather than silently scoring data.
- The GAGG name is retained; other crystal logical volumes are unchanged.
- Non-zero target energy is accessible as `et[1]`.

## Homework comparison

Show the startup line, the `et[1]` spectrum and the code diff.  Do not rename
the GDML to force GEARS' `(S)` convention.

## Next diff

Compare this checkpoint with `course-l04-al-support`.
