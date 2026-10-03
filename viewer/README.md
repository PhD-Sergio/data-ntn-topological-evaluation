# Static viewer data

This directory is the versioned input for the LEOPath Cesium viewer. It contains
four synthetic single-shell models, generated TLEs, 24 ground stations, and seven
controlled failure demonstrations exported by the Python forwarding code.

These demonstrations are separate from the paper's evaluation campaigns. The CSV
aggregates elsewhere in this repository do not contain individual forwarding
walks; they are not used to invent replay routes. Each replay records its policy,
configuration, code hashes and dependency versions. `inputs/` preserves the
metadata used to check the shell configurations against the evaluation dataset.

`bundle.json` lists SHA-256 hashes for every data file. It identifies the simulator
commit and forwarding source hash. Release packaging adds the dataset tag and
exact dataset commit to `release.json` inside the downloadable archive.

## Regenerate and validate

In a LEOPath checkout with its Python dependencies installed, regenerate the
replays when shell configurations or forwarding policy change:

```bash
python scripts/export_viewer_replay.py --shells telesat starlink kuiper oneweb --topology grid
python scripts/export_viewer_replay.py --shells telesat --topology ring
python scripts/export_viewer_replay.py --shells telesat --topology grid_seam
python scripts/export_viewer_replay.py --shells kuiper --topology brick_a
python scripts/export_viewer_dataset.py --dataset /path/to/data-ntn-topological-evaluation --output /tmp/viewer-next
```

Export into a fresh directory, review its provenance, then replace `viewer/` with
those files and keep this README. Commit the bundle together with updated
campaign inputs. The exporter rejects mismatched shell parameters. Release
packaging rejects changed evaluation metadata until the bundle is regenerated.

In this dataset checkout:

```bash
python scripts/viewer_dataset.py validate viewer --dataset-root .
python scripts/verify_viewer_replays.py viewer/replays
```

## Release and Pages deployment

The existing LEOPath Pages site remains at
<https://fundacio-i2cat.github.io/LEOPath/cesium/>.

One-time setup:

1. Install the paired workflow changes in LEOPath and this repository.
2. Add the Actions secret `LEOPATH_PAGES_DISPATCH_TOKEN` to this dataset
   repository. Use a fine-grained token restricted to `Fundacio-i2CAT/LEOPath`
   with **Contents: write**, or an equivalently scoped GitHub App token. The
   dataset's ordinary `GITHUB_TOKEN` cannot dispatch into the other repository.
3. Publish a new stable dataset release that includes `viewer/`. Existing
   v1.0.0/v1.0.1 tags have no viewer bundle and remain untouched. Publish the
   first viewer-bearing dataset release before merging the LEOPath deployment
   workflow; its `main` build resolves the latest stable dataset release.

A published stable release validates and packages its tagged commit, uploads
`leopath-viewer.tar.gz` and its checksum, then dispatches LEOPath's Documentation
workflow. Pre-releases do not replace the public site. A failed deployment leaves
the previously deployed Pages artifact in place.

The Pages build verifies the release tag/commit and checksums, tests replay paths,
and installs the data in the static build output. The viewer displays the dataset version,
commit, and a link to prior releases. It makes no Python/backend requests.

Retries preserve already uploaded matching assets; conflicting data under an
existing version is rejected. Use **Publish viewer dataset → Run workflow** with
an existing stable tag to retry after resolving a missing secret. To deploy a
previous bundle, run LEOPath's **Documentation** workflow with its `dataset_tag`.
A later normal code build uses the latest stable release again.

For local previews in LEOPath:

```bash
LEOPATH_DATASET_DIR=/path/to/data-ntn-topological-evaluation bash scripts/build-docs-site.sh
python -m http.server 8765 --directory site/cesium
```

The UI labels this as an unreleased dataset preview, not a published version.

## Attribution

Dataset: NTN LEO Satellite Routing Evaluation Data, Sergio Giménez-Antón,
Eduard Grasa and Jordi Perelló; CC BY 4.0. Simulator: LEOPath, AGPL-3.0.
