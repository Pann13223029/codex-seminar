"""Copy the example skills into the practice tracks so they work without installing.

Codex loads skills from .agents/skills in the folder you open, so tracks 98
and 99 ship with the skills they use. Edit skills in skills/, then run:

    python tools/sync_skills.py
"""

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACKS = {
    "98-present-your-work": ["survey-summary", "presentation-page"],
    "99-follow-my-example": ["data-explore", "presentation-page"],
}

for track, skills in TRACKS.items():
    target = ROOT / track / ".agents" / "skills"
    target.mkdir(parents=True, exist_ok=True)
    for name in skills:
        shutil.rmtree(target / name, ignore_errors=True)
        shutil.copytree(ROOT / "skills" / name, target / name)
        print(f"{track}: {name}")
