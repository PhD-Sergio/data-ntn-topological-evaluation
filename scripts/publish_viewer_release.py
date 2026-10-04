"""Upload idempotently, then dispatch Pages using the dataset's exact release SHA."""

import argparse
import json
from pathlib import Path
import subprocess
import tempfile

from viewer_dataset import ASSET, REPOSITORY, git, release_info


def api(path):
    return json.loads(subprocess.check_output(["gh", "api", path], text=True))


def publish(tag, assets, dispatch_only):
    commit = git(
        Path(__file__).resolve().parents[1], "rev-parse", f"refs/tags/{tag}^{{commit}}"
    )
    release_info(REPOSITORY, tag, commit)
    release = api(f"repos/{REPOSITORY}/releases/tags/{tag}")
    if release["draft"] or release["prerelease"]:
        raise ValueError(
            "Publish a stable dataset release before uploading or dispatching"
        )
    if not dispatch_only:
        names = {a["name"] for a in release["assets"]}
        wanted = (ASSET, ASSET + ".sha256")
        if set(wanted) & names:
            if not set(wanted) <= names:
                raise ValueError(
                    "Incomplete existing viewer release assets; repair the release explicitly"
                )
            # Retries reuse the already published bundle instead of replacing an
            # immutable asset. Compare file-level manifest and release identity,
            # since gzip/tar timestamps need not be byte-identical on another run.
            from viewer_dataset import unpack, validate, read_json

            with tempfile.TemporaryDirectory() as tmp:
                directory = Path(tmp)
                for name in wanted:
                    subprocess.run(
                        [
                            "gh",
                            "release",
                            "download",
                            tag,
                            "--repo",
                            REPOSITORY,
                            "--pattern",
                            name,
                            "--dir",
                            str(directory),
                        ],
                        check=True,
                    )
                old = unpack(
                    directory / ASSET,
                    directory / (ASSET + ".sha256"),
                    directory / "old",
                )
                new = unpack(
                    assets / ASSET, assets / (ASSET + ".sha256"), directory / "new"
                )
                if validate(old) != validate(new) or read_json(
                    old / "release.json"
                ) != read_json(new / "release.json"):
                    raise ValueError(
                        "This release already contains a different viewer bundle; publish a new version"
                    )
            print("Reusing matching published viewer assets")
        else:
            subprocess.run(
                [
                    "gh",
                    "release",
                    "upload",
                    tag,
                    *[str(assets / n) for n in wanted],
                    "--repo",
                    REPOSITORY,
                ],
                check=True,
            )
    else:
        payload = {
            "event_type": "viewer-dataset-released",
            "client_payload": {"tag": tag, "commit": commit},
        }
        subprocess.run(
            [
                "gh",
                "api",
                "--method",
                "POST",
                "repos/Fundacio-i2CAT/LEOPath/dispatches",
                "--input",
                "-",
            ],
            input=json.dumps(payload),
            text=True,
            check=True,
        )
        print(f"Dispatched LEOPath Pages build for {tag} ({commit[:12]})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--assets", type=Path)
    parser.add_argument("--dispatch-only", action="store_true")
    args = parser.parse_args()
    if not args.dispatch_only and not args.assets:
        parser.error("--assets is required when publishing")
    try:
        publish(args.tag, args.assets, args.dispatch_only)
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Viewer release error: {error}\n")
