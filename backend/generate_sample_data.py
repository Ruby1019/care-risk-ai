import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


ACTIVITIES = [
    ("Registration", "Front Desk", 5, 15),
    ("Triage", "Emergency", 8, 20),
    ("Consultation", "Clinic", 15, 45),
    ("Medication", "Pharmacy", 5, 25),
    ("Discharge", "Front Desk", 5, 15),
]

PATIENT_TYPES = ["adult", "elderly", "child"]
PRIORITIES = ["normal", "urgent"]


def random_datetime(base_date: datetime, max_minutes_offset: int) -> datetime:
    return base_date + timedelta(minutes=random.randint(0, max_minutes_offset))


def generate_case(case_index: int, base_date: datetime) -> list[dict]:
    case_id = f"P{case_index:04d}"
    patient_type = random.choice(PATIENT_TYPES)

    priority = random.choices(
        PRIORITIES,
        weights=[0.75, 0.25],
        k=1,
    )[0]

    current_time = random_datetime(base_date, max_minutes_offset=8 * 60)

    rows = []

    missing_activity_probability = 0.03
    repeated_activity_probability = 0.05
    long_wait_probability = 0.15

    activities = ACTIVITIES.copy()

    if random.random() < missing_activity_probability:
        removable_activities = [
            activity for activity in activities
            if activity[0] not in ["Registration", "Discharge"]
        ]
        activity_to_remove = random.choice(removable_activities)
        activities.remove(activity_to_remove)

    for activity_name, department, min_duration, max_duration in activities:
        duration_minutes = random.randint(min_duration, max_duration)

        start_time = current_time
        end_time = start_time + timedelta(minutes=duration_minutes)

        rows.append(
            {
                "case_id": case_id,
                "patient_type": patient_type,
                "activity": activity_name,
                "start_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
                "end_time": end_time.strftime("%Y-%m-%d %H:%M:%S"),
                "department": department,
                "priority": priority,
            }
        )

        if random.random() < long_wait_probability:
            waiting_minutes = random.randint(45, 120)
        else:
            waiting_minutes = random.randint(5, 40)

        if priority == "urgent":
            waiting_minutes = max(3, waiting_minutes - random.randint(5, 20))

        current_time = end_time + timedelta(minutes=waiting_minutes)

        if random.random() < repeated_activity_probability and activity_name == "Consultation":
            repeated_duration = random.randint(10, 30)
            repeated_start = current_time
            repeated_end = repeated_start + timedelta(minutes=repeated_duration)

            rows.append(
                {
                    "case_id": case_id,
                    "patient_type": patient_type,
                    "activity": "Consultation",
                    "start_time": repeated_start.strftime("%Y-%m-%d %H:%M:%S"),
                    "end_time": repeated_end.strftime("%Y-%m-%d %H:%M:%S"),
                    "department": "Clinic",
                    "priority": priority,
                }
            )

            current_time = repeated_end + timedelta(minutes=random.randint(5, 30))

    return rows


def generate_sample_event_log(case_count: int = 500) -> pd.DataFrame:
    base_date = datetime(2026, 1, 1, 8, 0, 0)

    all_rows = []

    for case_index in range(1, case_count + 1):
        case_date = base_date + timedelta(days=random.randint(0, 30))
        case_rows = generate_case(case_index, case_date)
        all_rows.extend(case_rows)

    df = pd.DataFrame(all_rows)
    df = df.sort_values(["case_id", "start_time"])

    return df


def main():
    output_dir = Path("data")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "generated_event_log.csv"

    df = generate_sample_event_log(case_count=500)
    df.to_csv(output_path, index=False)

    print("=== Sample Event Log Generated ===")
    print(f"Output file: {output_path}")
    print(f"Total rows: {len(df)}")
    print(f"Total cases: {df['case_id'].nunique()}")
    print()
    print(df.head(10))


if __name__ == "__main__":
    main()