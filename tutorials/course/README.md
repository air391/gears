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
| Later tags | L03--L05 | Added one after another by the corresponding checkpoint. |
