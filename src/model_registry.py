import json
import os
REGISTRY_FILE = './models/registry.json'

def register_model(model_name, model_type, metrics, path):
    record = {"model_name": model_name, "model_type": model_type, "metrics": metrics, "path": path}
    registry = []
    if os.path.exists(REGISTRY_FILE):
        with open(REGISTRY_FILE, 'r') as f:
            registry = json.load(f)
    registry.append(record)
    with open(REGISTRY_FILE, 'w') as f:
        json.dump(registry, f, indent=4)
    print(f"{model_name} 成功注册！")