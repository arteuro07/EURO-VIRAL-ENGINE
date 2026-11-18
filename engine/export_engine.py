import csv
import json
import zipfile
from pathlib import Path

from timeline_engine import build_timeline
from effects_engine import describe_effect, describe_transition

ROOT = Path(__file__).resolve().parents[1]

def export_kit(template_path):
    template_path = Path(template_path)
    if not template_path.is_absolute():
        template_path = ROOT / template_path

    template = json.loads(template_path.read_text(encoding="utf-8"))
    timeline = build_timeline(template)

    name = template["id"]
    work = ROOT / "output" / name
    work.mkdir(parents=True, exist_ok=True)

    instructions = []

    for scene in timeline:
        effect = describe_effect(scene["effect"])
        transition = describe_transition(scene["transition"])

        instructions.append({
            **scene,
            "effect_name": effect["name"],
            "effect_instructions": effect["instructions"],
            "transition_instructions": transition
        })

    project = {
        "name": template["name"],
        "format": template["format"],
        "media_slots": template["media_slots"],
        "music": template["music"],
        "scenes": instructions,
        "capcut_note": (
            "Kit de préparation. Reconstituer les pistes "
            "dans CapCut Android. Ce fichier n'est pas un "
            "projet natif CapCut."
        )
    }

    (work / "project.json").write_text(
        json.dumps(project, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    with (work / "timeline.csv").open(
        "w", newline="", encoding="utf-8-sig"
    ) as f:
        writer = csv.writer(f)
        writer.writerow([
            "Scene", "Debut", "Fin", "Duree",
            "Media", "Effet", "Transition", "Instructions"
        ])
        for scene in instructions:
            writer.writerow([
                scene["media"],
                scene["start"],
                scene["end"],
                scene["duration"],
                scene["media"],
                scene["effect_name"],
                scene["transition_instructions"],
                scene["effect_instructions"]
            ])

    guide = [
        f"# {template['name']}",
        "",
        "## Format",
        f"- {template['format']['width']} x {template['format']['height']}",
        f"- {template['format']['fps']} FPS",
        f"- {template['format']['duration']} secondes",
        "- Format vertical 9:16",
        "",
        "## Médias",
        "Remplacer MEDIA_1 à MEDIA_5 par tes propres clips.",
        "",
        "## Montage CapCut Android",
        "1. Créer un projet en 9:16.",
        "2. Importer les cinq médias.",
        "3. Respecter les durées du fichier timeline.csv.",
        "4. Appliquer les effets et transitions indiqués.",
        "5. Ajouter un son autorisé depuis la bibliothèque CapCut.",
        "6. Remplacer les textes par tes propres titres.",
        "7. Exporter en 1080p.",
        "",
        "## Scènes"
    ]

    for scene in instructions:
        guide.extend([
            "",
            f"### {scene['media']} ({scene['start']}–{scene['end']} s)",
            f"- Effet : {scene['effect_name']}",
            f"- Transition : {scene['transition_instructions']}",
            f"- Réglage : {scene['effect_instructions']}"
        ])

    (work / "GUIDE_CAPCUT.md").write_text(
        "\n".join(guide), encoding="utf-8"
    )

    archive = ROOT / "output" / f"{name}_CAPCUT_KIT.zip"

    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as z:
        for file in work.rglob("*"):
            if file.is_file():
                z.write(file, file.relative_to(work))

    return archive, instructions

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "config/velocity_flash.json"
    archive, scenes = export_kit(path)
    print("EXPORT SUCCESS")
    print("Scenes:", len(scenes))
    print("Kit:", archive)
