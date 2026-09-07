import yaml
import json
import sys

with open("policies/resilience_rules.yaml") as f:
    policy = yaml.safe_load(f)

with open("reports/result.json") as f:
    result = json.load(f)

required_score = policy["scoring"]["passing_score"]

actual_score = result["score"]

print(f"Required Score : {required_score}")
print(f"Actual Score   : {actual_score}")

if actual_score < required_score:
    print("FAILED: Deployment Blocked")
    sys.exit(1)

print("PASSED: Deployment Approved")
