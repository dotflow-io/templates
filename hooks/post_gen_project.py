"""Post-generation hook: move all files up one level into the parent directory."""

import os
import shutil
from pathlib import Path

project_dir = Path(os.getcwd())
parent_dir = project_dir.parent

for item in project_dir.iterdir():
    dest = parent_dir / item.name
    if dest.exists():
        if dest.is_dir():
            shutil.rmtree(dest)
        else:
            dest.unlink()
    shutil.move(str(item), str(parent_dir))

project_dir.rmdir()
