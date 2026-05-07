import pandas as pd


def analyze_event_log(file_path: str):
    df = pd.read_csv(file_path)

    required_columns = [
        "case_id",
        "patient_type",
        "activity",
        "start_time",
        "end_time",
        "department",
        "priority",
    ]

    missing_columns = [column for column in required_columns if column not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    df["start_time"] = pd.to_datetime(df["start_time"])
    df["end_time"] = pd.to_datetime(df["end_time"])

    df = df.sort_values(["case_id", "start_time"])

    df["duration_minutes"] = (
        df["end_time"] - df["start_time"]
    ).dt.total_seconds() / 60

    df["next_start_time"] = df.groupby("case_id")["start_time"].shift(-1)

    df["waiting_minutes"] = (
        df["next_start_time"] - df["end_time"]
    ).dt.total_seconds() / 60

    df["waiting_minutes"] = df["waiting_minutes"].fillna(0)

    case_summary = df.groupby("case_id").agg(
        total_duration_minutes=("duration_minutes", "sum"),
        total_waiting_minutes=("waiting_minutes", "sum"),
        max_waiting_minutes=("waiting_minutes", "max"),
        patient_type=("patient_type", "first"),
        priority=("priority", "first"),
        activity_count=("activity", "count"),
    ).reset_index()

    avg_total_duration = case_summary["total_duration_minutes"].mean()
    std_total_duration = case_summary["total_duration_minutes"].std()

    if pd.isna(std_total_duration):
        std_total_duration = 0

    def calculate_risk(row):
        score = 0

        if row["max_waiting_minutes"] > 30:
            score += 20

        if row["max_waiting_minutes"] > 60:
            score += 20

        if row["total_duration_minutes"] > avg_total_duration + 1.5 * std_total_duration:
            score += 20

        if row["priority"] == "urgent" and row["max_waiting_minutes"] > 30:
            score += 25

        if row["activity_count"] < 4:
            score += 15

        return min(score, 100)

    case_summary["risk_score"] = case_summary.apply(calculate_risk, axis=1)

    def classify_risk(score):
        if score >= 60:
            return "High"
        if score >= 30:
            return "Medium"
        return "Low"

    case_summary["risk_level"] = case_summary["risk_score"].apply(classify_risk)

    activity_duration = (
        df.groupby("activity")["duration_minutes"]
        .mean()
        .round(2)
        .reset_index()
    )

    department_waiting = (
        df.groupby("department")["waiting_minutes"]
        .mean()
        .round(2)
        .reset_index()
    )

    high_risk_cases = case_summary[
        case_summary["risk_level"] == "High"
    ].sort_values("risk_score", ascending=False)

    result = {
        "total_cases": int(case_summary["case_id"].nunique()),
        "avg_total_duration": round(case_summary["total_duration_minutes"].mean(), 2),
        "avg_waiting_time": round(case_summary["total_waiting_minutes"].mean(), 2),
        "high_risk_case_count": int(len(high_risk_cases)),
        "case_summary": case_summary.to_dict(orient="records"),
        "activity_duration": activity_duration.to_dict(orient="records"),
        "department_waiting": department_waiting.to_dict(orient="records"),
        "high_risk_cases": high_risk_cases.to_dict(orient="records"),
    }

    return result


if __name__ == "__main__":
    result = analyze_event_log("data/sample_event_log.csv")

    print("=== CareRisk AI Analysis Result ===")
    print(f"Total cases: {result['total_cases']}")
    print(f"Average total duration: {result['avg_total_duration']} minutes")
    print(f"Average waiting time: {result['avg_waiting_time']} minutes")
    print(f"High-risk case count: {result['high_risk_case_count']}")

    print("\n=== High Risk Cases ===")
    for case in result["high_risk_cases"]:
        print(case)
