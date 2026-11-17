"""İndirilenler klasöründeki en yeni ses dosyasını bir videonun anlatımı yapar.

python ses_al.py 01        -> en yeni mp3'ü videolar/01-.../assets/audio/narration.mp3 olarak taşır
Sonra: python hepsini_uret.py 01   (videoyu bu sesle yeniden üretir)
"""
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).parent
DOWNLOADS = Path.home() / "Downloads"

no = sys.argv[1]
video = next(d for d in sorted((HERE / "videolar").iterdir()) if d.name.startswith(no))
files = sorted([*DOWNLOADS.glob("*.mp3"), *DOWNLOADS.glob("*.wav")], key=lambda f: f.stat().st_mtime)
if not files:
    sys.exit("İndirilenler klasöründe ses dosyası yok.")
src = files[-1]
dst = video / "assets" / "audio" / ("narration" + src.suffix)
dst.parent.mkdir(parents=True, exist_ok=True)
shutil.move(str(src), dst)
print(f"{src.name} -> {dst.relative_to(HERE)}")
