# CareRisk AI

CareRisk AI is an AI-assisted healthcare process risk dashboard project designed to analyze healthcare process event logs, identify workflow bottlenecks, calculate case-level risk scores, and generate structured analysis results for future dashboard visualization.

This project focuses on the intersection of healthcare information systems, digital health, healthcare process management, and AI-assisted decision support.

## Project Motivation

Healthcare workflows often involve multiple departments, waiting periods, and handoff points. Delays, missing steps, repeated activities, or abnormal process patterns may increase operational risk and reduce service quality.

CareRisk AI aims to support healthcare process improvement by transforming healthcare process event logs into measurable indicators, including waiting time, process duration, risk score, and risk level.

## Current Project Status

The current version has completed the backend data analysis workflow.

Completed features:

- Generate synthetic healthcare process event logs
- Calculate activity duration
- Calculate waiting time between activities
- Calculate total process duration for each patient case
- Identify high-risk cases
- Generate case-level risk scores
- Classify cases into Low, Medium, and High risk levels
- Export analysis results as a JSON file for future dashboard use

Planned features:

- Interactive dashboard
- Data upload interface
- Risk visualization charts
- AI-assisted improvement suggestions
- PDF or report export
- Deployment with Docker

## Example Healthcare Process

The current synthetic dataset simulates a simplified healthcare process:

```text
Registration → Triage → Consultation → Medication → Discharge
