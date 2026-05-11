import shutil
import subprocess
import sys
from pathlib import Path


def run_command(command: list[str], cwd: Path) -> None:
    print(f"\nRunning command: {' '.join(command)}")

    result = subprocess.run(
        command,
        cwd=cwd,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(command)}")


def main() -> None:
    project_root = Path(__file__).resolve().parent

    data_dir = project_root / "data"
    frontend_data_dir = project_root / "frontend" / "public" / "data"

    generated_csv = data_dir / "generated_event_log.csv"
    analysis_json = data_dir / "analysis_result.json"
    frontend_analysis_json = frontend_data_dir / "analysis_result.json"

    print("=== CareRisk AI Automated Pipeline Started ===")

    print("\nStep 1: Generate synthetic healthcare event log")
    run_command(
        [sys.executable, str(project_root / "backend" / "generate_sample_data.py")],
        cwd=project_root,
    )

    if not generated_csv.exists():
        raise FileNotFoundError(f"Generated CSV not found: {generated_csv}")

    print("\nStep 2: Analyze healthcare process risk")
    run_command(
        [sys.executable, str(project_root / "backend" / "analyze_event_log.py")],
        cwd=project_root,
    )

    if not analysis_json.exists():
        raise FileNotFoundError(f"Analysis JSON not found: {analysis_json}")

    print("\nStep 3: Copy analysis result to frontend public data folder")
    frontend_data_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(analysis_json, frontend_analysis_json)

    print("\n=== CareRisk AI Automated Pipeline Completed ===")
    print(f"Generated CSV: {generated_csv}")
    print(f"Analysis JSON: {analysis_json}")
    print(f"Frontend JSON: {frontend_analysis_json}")

    print("\nYou can now run the dashboard:")
    print("cd frontend")
    print("npm run dev")


if __name__ == "__main__":
    main()