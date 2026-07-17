# GEARS course checkpoints

This branch is the teacher's reference line for the Geant4 beginner course.
Each tag is immutable and is a self-contained checkpoint for a classroom
demonstration or a homework comparison.  Students implement changes on their
own branch; they do not need to start a new Geant4 application.

The checkpoints deliberately keep `GRID10B.gdml` and its `GRID10B/`
dependencies outside Git.  Put those files beside the Lesson 04 macros before
running them.

Build every checkpoint in a clean build directory:

```bash
source /opt/geant4-v11.4.1-install/bin/geant4.sh
cmake -S . -B build -DCMAKE_PREFIX_PATH="/opt/geant4-v11.4.1-install;/opt/expat-2.6.4;/opt/xerces-c-3.2.5" -DEXPAT_ROOT=/opt/expat-2.6.4
cmake --build build -j4
```

Do not use `sudo`.  The explicit Expat prefix is required on the course
server because the system Expat is older than Geant4 11.4.1 requires.

| Tag | Lesson | Focus |
| --- | --- | --- |
| `course-l03-start` | L03 | Build GEARS and run its upstream output tutorial. |
| `course-l03-source-output` | L03 | Fixed-direction gamma macro and a minimal Python spectrum. |
| `course-l04-gdml-import` | L04 | Import the distributed GDML and verify its geometry. |
| `course-l04-target-material` | L04 | Select one logical volume, replace its material and map it to `et[1]`. |
| `course-l04-al-support` | L04 | Add a parameterised 400 mm aluminium support outside the GDML envelope. |
| `course-l05-scan-prototype` | L05 | Generate 100 macros and stack `et[1]` spectra into a provisional matrix. |
| `course-l05-reference-run` | L05 | Reserved for a validated teacher baseline after analysis requirements exist. |
