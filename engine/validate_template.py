import json
import sys
from pathlib import Path

path = Path(sys.argv[1] if len(sys.argv) > 1 else
            "config/velocity_flash.json")

data = json.loads(path.read_text(encoding="utf-8"))
timeline = data["timeline"]

assert data["format"]["width"] == 1080
assert data["format"]["height"] == 1920
assert data["format"]["fps"] == 30
assert data["format"]["duration"] == 15
assert data["media_slots"] == 5
assert len(timeline) == 5

for i, scene in enumerate(timeline):
    assert scene["end"] > scene["start"]
    assert scene["slot"] == i + 1
    if i:
        assert timeline[i-1]["end"] == scene["start"]

assert timeline[0]["start"] == 0
assert timeline[-1]["end"] == 15

print("EURO VIRAL ENGINE")
print("Template:", data["name"])
print("Durée:", data["format"]["duration"], "secondes")
print("Médias:", data["media_slots"])
print("Résolution: 1080x1920")
print("VALIDATION: SUCCESS")
