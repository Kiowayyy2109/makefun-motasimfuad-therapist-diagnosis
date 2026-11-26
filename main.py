import os

LINE = "Diagnosis: chronic tab-hoarding with acute notification anxiety. Treatment: close one tab per day. At your current rate, recovery is scheduled for 2031."

LIMIT = 200
if len(LINE) != 152 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 152 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
