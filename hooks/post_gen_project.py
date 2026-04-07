"""Post-generation hook: flatten project and optionally fetch cloud templates."""

import json
import os
import shutil
import tempfile
from pathlib import Path
from urllib.request import urlopen

CLOUD_URL = "https://raw.githubusercontent.com/dotflow-io/template/master/cloud"

PROJECT_DIR = Path(os.getcwd())
PARENT_DIR = PROJECT_DIR.parent

CLOUD = "{{ cookiecutter.cloud }}"
PROJECT_NAME = "{{ cookiecutter.project_name }}"
MODULE_NAME = "{{ cookiecutter.module_name }}"


def flatten_project():
    """Move generated files from project subfolder to parent directory."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)

        for item in PROJECT_DIR.iterdir():
            shutil.move(str(item), str(tmp_dir / item.name))

        PROJECT_DIR.rmdir()

        for item in tmp_dir.iterdir():
            dest = PARENT_DIR / item.name
            if dest.exists():
                shutil.rmtree(dest) if dest.is_dir() else dest.unlink()
            shutil.move(str(item), str(dest))


def fetch_cloud_templates():
    """Download cloud infrastructure files for the selected platform."""
    if CLOUD == "none":
        return

    registry = json.loads(
        urlopen(f"{CLOUD_URL}/registry.json", timeout=10).read()
    )

    platform = registry["platforms"].get(CLOUD)
    if not platform:
        return

    project_tag = "{" + "{PROJECT_NAME}" + "}"
    module_tag = "{" + "{MODULE_NAME}" + "}"

    for filename in platform["files"]:
        content = urlopen(f"{CLOUD_URL}/{CLOUD}/{filename}", timeout=10).read().decode()
        content = content.replace(project_tag, PROJECT_NAME)
        content = content.replace(module_tag, MODULE_NAME)
        (PARENT_DIR / filename).write_text(content)


flatten_project()

try:
    fetch_cloud_templates()
except Exception as err:
    print(f"Warning: Could not fetch cloud templates: {err}")
