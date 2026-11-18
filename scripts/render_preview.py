import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "anime_phonk"
OUT.mkdir(parents=True, exist_ok=True)

video = OUT / "VELOCITY_AWAKENING_PREVIEW.mp4"
cover = OUT / "COVER.jpg"

font = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

filters = [
    "drawbox=x='mod(t*260,iw)':y=0:w=5:h=ih:color=0xB000FF@0.65:t=fill",
    "drawbox=x=0:y='mod(t*340,ih)':w=iw:h=4:color=0xFF1744@0.55:t=fill",
    "drawbox=x=0:y=0:w=iw:h=ih:color=white@0.48:t=fill:enable='between(t,2,2.09)+between(t,8.9,9.02)'",
    f"drawtext=fontfile={font}:text='EURO VIRAL':fontcolor=white:fontsize=42:x=(w-text_w)/2:y=h*0.18:borderw=2:bordercolor=0xA000FF",
    f"drawtext=fontfile={font}:text='VELOCITY':fontcolor=white:fontsize=105:x=(w-text_w)/2:y=h*0.36:borderw=5:bordercolor=0x9B00FF:shadowcolor=0xFF1744:shadowx=5:shadowy=5:enable='between(t,0,2)'",
    f"drawtext=fontfile={font}:text='AWAKENING':fontcolor=0xFF315D:fontsize=85:x=(w-text_w)/2:y=h*0.45:borderw=3:bordercolor=white:enable='between(t,0,2)'",
    f"drawtext=fontfile={font}:text='REPLACE YOUR CLIP':fontcolor=white:fontsize=56:x=(w-text_w)/2:y=h*0.44:borderw=3:bordercolor=0xA000FF:enable='between(t,2,5)'",
    f"drawtext=fontfile={font}:text='VELOCITY MODE':fontcolor=white:fontsize=68:x=(w-text_w)/2:y=h*0.44:borderw=4:bordercolor=0xFF1744:enable='between(t,5,9)'",
    f"drawtext=fontfile={font}:text='MAXIMUM IMPACT':fontcolor=white:fontsize=65:x=(w-text_w)/2:y=h*0.44:borderw=4:bordercolor=0xA000FF:enable='between(t,9,12)'",
    f"drawtext=fontfile={font}:text='YOUR MOMENT':fontcolor=white:fontsize=76:x=(w-text_w)/2:y=h*0.44:borderw=4:bordercolor=0xFF1744:enable='between(t,12,15)'",
    "vignette=PI/4"
]

cmd = [
    "ffmpeg", "-y",
    "-f", "lavfi",
    "-i", "color=c=0x080014:s=1080x1920:r=30:d=15",
    "-vf", ",".join(filters),
    "-an",
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-crf", "20",
    "-pix_fmt", "yuv420p",
    "-movflags", "+faststart",
    str(video)
]

subprocess.run(cmd, check=True)

subprocess.run([
    "ffmpeg", "-y", "-ss", "1",
    "-i", str(video), "-frames:v", "1",
    "-q:v", "2", str(cover)
], check=True)

print("PREVIEW SUCCESS")
print("VIDEO:", video)
print("COVER:", cover)
