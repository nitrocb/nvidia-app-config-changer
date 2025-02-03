import os
import json

# Pfad zur NVIDIA App Config-Datei (Anpassen, falls nötig)
CONFIG_PATH = os.path.expandvars(r"ApplicationStorage.json")
OUTPUT = os.path.expandvars(r"Test.json")

# Sicherstellen, dass die Datei existiert
if not os.path.exists(CONFIG_PATH):
    print(f"Configfile not found: {CONFIG_PATH}")
    exit(1)

# Konfigurationsdatei laden
with open(CONFIG_PATH, "r", encoding="utf-8") as file:
    try:
        config = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error while loading configfile: {e}")
        exit(1)

for app in config["Applications"]:
    app["Application"]["Disable_FG_Override"] = False
    app["Application"]["Disable_RR_Override"] = False
    app["Application"]["Disable_SR_Override"] = False
    app["Application"]["Disable_RR_Model_Override"] = False
    app["Application"]["Disable_SR_Model_Override"] = False

with open(OUTPUT, "w", encoding="utf-8") as file:
    json.dump(config, file, indent=4)