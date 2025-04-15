import json
from models import VehicleStatus
from ai_checker import analyze_warning

def main():
    json_path = "sample_response.json"

    try:
        with open(json_path, 'r') as file:
            responses = json.load(file)

        if not isinstance(responses, list):
            responses = [responses]  # Support single object or list

        for i, data in enumerate(responses, start=1):
            print(f"\n🔍 Test Case #{i}")
            try:
                status = VehicleStatus(**data)
                print("✅ Schema valid.")
                print(f"Engine: {status.engine}")
                print(f"Battery: {status.battery_level}%")
                print(f"Fuel: {status.fuel_level}%")
                print(f"Warning: {status.warning_message}")

                # Rule-based alerts
                if status.battery_level < 25:
                    print(f"⚠️  Low battery detected: {status.battery_level}%")
                if status.fuel_level < 15:
                    print(f"⛽ Low fuel detected: {status.fuel_level}%")

                # AI sentiment check
                label, score = analyze_warning(status.warning_message)
                print(f"🧠 Sentiment: {label} ({round(score, 2)})")

            except Exception as e:
                print(f"❌ Validation or processing error: {e}")

    except FileNotFoundError:
        print(f"❌ File not found: {json_path}")
    except json.JSONDecodeError:
        print(f"❌ Invalid JSON format in: {json_path}")

if __name__ == "__main__":
    main()

