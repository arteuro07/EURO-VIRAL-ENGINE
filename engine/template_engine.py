import sys
from pathlib import Path
from validate_template import *

from export_engine import export_kit

if __name__ == "__main__":
    archive, scenes = export_kit(
        sys.argv[1] if len(sys.argv) > 1
        else "config/velocity_flash.json"
    )
    print("EURO VIRAL ENGINE READY")
    print("Scenes:", len(scenes))
    print("Output:", archive)
