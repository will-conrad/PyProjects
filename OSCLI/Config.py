import json

configPath = "config.json"
defaultConfig = {
    "ip": "127.0.0.1",
    "receive_port": "8001"
}
def loadConfig():
    try:
        with open(configPath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        with open("config.json", "w") as f:
            json.dump(defaultConfig, f)
            return json.load(f)
def loadData(path):
    return json.loads(path)