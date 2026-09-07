import yaml
import json
import sys

policy = yaml.safe_load(open("policies/resilience_rules.yaml"))
result = json.load(open("reports/result.json"))

required = policy["minimum_score"]

if result["score"] < required:
    print("FAILED")
    sys.exit(1)

print("PASSED")
