import json

from medilink_contract import build_summary


def main() -> None:
    patient = {
        "patient_id": "P-1001",
        "name": "Alex Morgan",
    }
    appointments = [
        {
            "appointment_id": "A-2001",
            "date": "2026-10-15",
            "department": "Community Health",
        }
    ]

    summary = build_summary(patient, appointments)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
