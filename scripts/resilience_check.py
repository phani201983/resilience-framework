# scripts/resilience_check.py

import yaml
import json

score = 100

with open("architecture/application.yaml") as f:
    data = yaml.safe_load(f)

for service in data["services"]:

    if service.get("replicas", 1) < 2:
        score -= 20

    if not service.get("healthCheck", False):
        score -= 10

    if not service.get("resources", False):
        score -= 10

result = {
    "application": data["application"]["name"],
    "score": score
}

with open("reports/result.json","w") as f:
    json.dump(result,f)

print(result)