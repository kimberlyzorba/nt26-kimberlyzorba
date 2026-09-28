from pathlib import Path

filnamn = Path(__file__).parent / "r1-show-run.txt"

routes = []
interfaces = []

with open(filnamn, encoding="utf-8") as f:
    for rad in f:
        rad = rad.strip()

        if rad.startswith("ip route "):
            routes.append(rad)

        if rad.startswith("interface "):
            interfaces.append(rad)

print(f"Hittade {len(routes)} statiska rutter:")
for rad in routes:
    print(rad)

print(f"\nHittade {len(interfaces)} interface:")
for rad in interfaces:
    print(rad)
