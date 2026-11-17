"""videolar/ altındaki, henüz mp4'ü olmayan her videoyu üretir (ses → render → kapak → carousel).

python hepsini_uret.py           -> eksikleri üret
python hepsini_uret.py 03 05     -> sadece adı 03 / 05 ile başlayan klasörler (yeniden)
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
OPENMONTAGE = HERE.parent / "OpenMontage"
secim = sys.argv[1:]
for d in sorted((HERE / "videolar").iterdir()):
    if not (d / "script.json").exists():
        continue
    if secim and not any(d.name.startswith(s) for s in secim):
        continue
    if not secim and list((d / "cikti").glob("*.mp4")):
        continue
    print(f"=== {d.name}", flush=True)
    r = subprocess.run([sys.executable, "-m", "psikoloji_reels.build", str(d), "--render", "--cover", "--carousel"],
                       cwd=OPENMONTAGE)
    print(f"=== {d.name}: {'TAMAM' if r.returncode == 0 else 'HATA'}", flush=True)
