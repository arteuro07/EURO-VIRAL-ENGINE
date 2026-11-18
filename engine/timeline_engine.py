def build_timeline(template):
    scenes = []
    for scene in template["timeline"]:
        scenes.append({
            "start": scene["start"],
            "end": scene["end"],
            "duration": scene["end"] - scene["start"],
            "media": f"MEDIA_{scene['slot']}",
            "effect": scene["effect"],
            "transition": scene["transition"]
        })
    return scenes
