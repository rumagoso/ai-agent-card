import json
import sys
from jsonschema import validate, ValidationError

def validate_agent_card(card_path: str, schema_path: str = "agent-card-v0.3.json"):
    """Validate an Agent Card against the official schema."""
    try:
        with open(schema_path, encoding="utf-8") as f:
            schema = json.load(f)
        with open(card_path, encoding="utf-8") as f:
            card = json.load(f)
        
        validate(instance=card, schema=schema)
        print(f"✅ Agent Card '{card_path}' is valid according to v0.3 schema.")
        return True
        
    except ValidationError as e:
        print("❌ Validation error:")
        print(e.message)
        if e.path:
            print(f"Path: {list(e.path)}")
        return False
    except FileNotFoundError as e:
        print(f"❌ File not found: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate-agent-card.py <path_to_agent_card.json>")
        print("Example: python validate-agent-card.py examples/grok-research-assistant-v1.json")
        sys.exit(1)
    
    validate_agent_card(sys.argv[1])
