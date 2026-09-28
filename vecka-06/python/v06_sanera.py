from pathlib import Path

kalla = Path.home() / "r1-rakonfig.txt"
utfil = Path(__file__).resolve().parent.parent / "configs" / "r1-show-run.txt"
kansliga_ord = ("secret", "password", "snmp-server community")

rader = kalla.read_text(encoding="utf-8").splitlines()
saker_rader = [
    rad for rad in rader
    if not any(ordet in rad.lower() for ordet in kansliga_ord)
]

utfil.write_text("\n".join(saker_rader) + "\n", encoding="utf-8")
print(f"Sparade {len(saker_rader)} rader i {utfil}")
print(f"Tog bort {len(rader) - len(saker_rader)} känsliga rader")