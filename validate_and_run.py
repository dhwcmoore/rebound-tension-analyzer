import json
import sys
from jsonschema import validate, ValidationError
from rebound_logic import compute_rebound_assessment

# Load input
with open("example.json") as f:
    input_data = json.load(f)

# Load schema
with open("schema.json") as f:
    schema = json.load(f)

# Validate and run
try:
    validate(instance=input_data, schema=schema)
    print("✅ Input valid. Running model...\n")
    result = compute_rebound_assessment(input_data)
    print(json.dumps(result, indent=2))
except ValidationError as e:
    print("❌ Schema validation failed:")
    print(e.message)
    sys.exit(1)
