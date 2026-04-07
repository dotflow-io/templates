"""Post-generation hook: optionally fetch cloud templates."""

import json
import os
from pathlib import Path
from urllib.request import urlopen

CLOUD_URL = "https://raw.githubusercontent.com/dotflow-io/template/master/cloud"

PROJECT_DIR = Path(os.getcwd())

CLOUD = "{{ cookiecutter.cloud }}"
PROJECT_NAME = "{{ cookiecutter.project_name }}"
MODULE_NAME = "{{ cookiecutter.module_name }}"
AWS_ACCOUNT_ID = "{{ cookiecutter.aws_account_id }}"
AWS_REGION = "{{ cookiecutter.aws_region }}"


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
    account_tag = "{" + "{AWS_ACCOUNT_ID}" + "}"
    region_tag = "{" + "{AWS_REGION}" + "}"

    for filename in platform["files"]:
        content = urlopen(f"{CLOUD_URL}/{CLOUD}/{filename}", timeout=10).read().decode()
        content = content.replace(project_tag, PROJECT_NAME)
        content = content.replace(module_tag, MODULE_NAME)
        content = content.replace(account_tag, AWS_ACCOUNT_ID)
        content = content.replace(region_tag, AWS_REGION)
        (PROJECT_DIR / filename).write_text(content)


try:
    fetch_cloud_templates()
except Exception as err:
    print(f"Warning: Could not fetch cloud templates: {err}")
