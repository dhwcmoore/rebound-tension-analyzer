import json
import argparse
from rebound_logic import compute_rebound_assessment

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("jsonfile", help="Path to JSON input file")
    args = parser.parse_args()
    with open(args.jsonfile) as f:
        data = json.load(f)
    result = compute_rebound_assessment(data)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
