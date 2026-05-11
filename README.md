# CareRisk AI：醫療照護流程風險分析儀表板

CareRisk AI 是一個醫療照護流程風險分析與視覺化儀表板雛型系統。  
本專案主要用於示範如何將醫療流程事件資料轉換成可分析、可解釋、可視覺化的流程風險指標，並透過 Dashboard 協助使用者理解流程瓶頸、等待時間與高風險案例。

本系統目前使用模擬的 healthcare process event log 進行開發與測試，模擬病患從掛號、檢傷、看診、領藥到離院的流程。由於真實醫療資料涉及個資、倫理審查與資料取得限制，因此第一版先以 synthetic data 建立系統雛型，用於驗證資料流程、分析邏輯與視覺化呈現方式。

## 專案目標

本專案的目標是建立一個醫療流程風險分析 prototype，將流程資料轉換成可量化的指標，包含：

- 活動處理時間
- 活動之間的等待時間
- 病患案例總流程時間
- 高風險案例數量
- 案例層級風險分數
- 風險等級分布
- 高風險案例表格

透過這些指標，系統可以協助使用者初步了解醫療流程中可能存在的延遲、瓶頸與風險案例。

## 系統功能

目前版本已完成以下功能：

- 產生模擬醫療流程事件資料
- 使用 Python 分析醫療流程資料
- 計算活動處理時間與等待時間
- 依據規則式方法計算案例層級風險分數
- 將案例分為 Low、Medium、High 三種風險等級
- 輸出 JSON 分析結果
- 使用 React 建立前端 Dashboard
- 視覺化呈現流程指標、風險分布與高風險案例
- 建立自動化 pipeline，一鍵完成資料產生、分析與前端資料更新

## 系統流程

本專案的資料處理流程如下：

```text
Synthetic Healthcare Event Log
        ↓
Python Backend Analysis
        ↓
Risk Score and Risk Level Calculation
        ↓
JSON Result Export
        ↓
React Dashboard Visualization
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
