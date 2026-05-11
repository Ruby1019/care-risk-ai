# CareRisk AI

## 中文專案介紹

CareRisk AI 是一個醫療照護流程風險分析與視覺化儀表板雛型系統。  
本專案主要用於示範如何將醫療流程事件資料轉換成可分析、可解釋、可視覺化的流程風險指標，並透過 Dashboard 協助使用者理解流程瓶頸、等待時間與高風險案例。

本系統目前使用模擬的 healthcare process event log 進行開發與測試，模擬病患從掛號、檢傷、看診、領藥到離院的流程。由於真實醫療資料涉及個資、倫理審查與資料取得限制，因此第一版先以 synthetic data 建立系統雛型，用於驗證資料流程、分析邏輯與視覺化呈現方式。

---

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

---

## 目前已完成功能

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
- 建立啟動腳本，協助快速啟動完整專案流程

---

## 系統流程

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
```

其中，`run_pipeline.py` 會自動執行資料產生、風險分析與 JSON 更新流程，使整個專案更容易重複執行與展示。

---

## 專案架構

```text
care-risk-ai/
│
├── backend/
│   ├── generate_sample_data.py
│   └── analyze_event_log.py
│
├── data/
│   ├── generated_event_log.csv
│   ├── sample_event_log.csv
│   └── analysis_result.json
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── docs/
│   └── research_background.md
│
├── run_pipeline.py
├── start_project.sh
├── README.md
└── requirements.txt
```

---

## 後端分析流程

後端使用 Python 進行資料處理與風險分析。

主要流程包含：

1. 產生模擬醫療流程資料
2. 讀取 healthcare event log
3. 計算每個活動的處理時間
4. 計算活動之間的等待時間
5. 彙整每個病患案例的總流程時間與總等待時間
6. 根據等待時間、流程時間與優先等級計算風險分數
7. 將案例分為 Low、Medium、High 三種風險等級
8. 輸出分析結果為 JSON 檔案

---

## 前端 Dashboard

前端使用 React 與 ECharts 建立 Dashboard，呈現以下資訊：

- Total Cases
- Average Total Duration
- Average Waiting Time
- High-risk Cases
- Average Activity Duration Chart
- Average Waiting Time by Department Chart
- Risk Level Distribution
- High-risk Patient Case Preview

Dashboard 會讀取後端產生的 `analysis_result.json`，並將分析結果視覺化。

---

## 自動化流程

本專案包含一個自動化 pipeline：

```bash
python run_pipeline.py
```

執行後會自動完成：

1. 產生模擬醫療流程資料
2. 執行後端風險分析
3. 輸出 JSON 分析結果
4. 複製 JSON 到前端 Dashboard 可讀取的位置

若要啟動完整專案，可以使用：

```bash
./start_project.sh
```

此腳本會先執行資料產生與分析流程，再啟動 React Dashboard。

---

## 如何執行

### 1. 安裝 Python 套件

```bash
pip install -r requirements.txt
```

### 2. 執行自動化資料分析流程

```bash
python run_pipeline.py
```

### 3. 啟動前端 Dashboard

```bash
cd frontend
npm install
npm run dev
```

啟動後，依照 Terminal 顯示的網址開啟，例如：

```text
http://localhost:5173/
```

### 4. 使用一鍵啟動腳本

如果使用 macOS，也可以直接執行：

```bash
./start_project.sh
```

此腳本會自動完成資料產生、資料分析、前端資料更新與 Dashboard 啟動流程。

---

## 研究意義

CareRisk AI 目前是一個研究型 prototype，主要目的是展示如何將醫療流程事件資料轉換為流程風險指標與視覺化結果。

本專案可延伸至以下研究方向：

- Healthcare Information Systems
- Digital Health
- Healthcare Process Management
- AI-assisted Decision Support
- Process Mining
- Explainable AI
- Healthcare Workflow Risk Analysis

目前版本使用 rule-based risk scoring 作為可解釋的 baseline。未來若能取得匿名化真實醫療資料，可進一步驗證風險規則、調整模型參數，並評估系統在真實醫療流程中的應用價值。

---

## 未來延伸方向

後續可擴充方向包含：

- 使用真實或匿名化醫療流程資料進行驗證
- 加入 process mining 分析實際流程與標準流程的差異
- 加入 machine learning 預測高風險案例
- 加入 explainable AI 解釋風險來源
- 加入 AI-assisted improvement suggestions
- 支援使用者上傳 CSV 進行即時分析
- 將系統部署至線上平台展示

---

## 專案定位

本專案不是臨床診斷系統，而是一個醫療流程管理與決策支援的雛型系統。  
其核心目標是協助使用者理解醫療流程中的等待時間、流程瓶頸與高風險案例，並作為未來醫療資訊系統、智慧醫療與流程風險分析研究的基礎。

---

# English Project Overview

CareRisk AI is a prototype healthcare process risk analysis and visualization dashboard.  
This project demonstrates how healthcare process event logs can be transformed into measurable, interpretable, and visualizable risk indicators. The dashboard helps users understand workflow bottlenecks, waiting time, and high-risk patient cases.

The current version uses synthetic healthcare process event logs for development and testing. These synthetic logs simulate a simplified patient journey, including registration, triage, consultation, medication, and discharge. Since real healthcare data involves privacy, ethical approval, and data access limitations, the first version uses synthetic data to validate the system workflow, analysis logic, and visualization design.

---

## Project Objectives

The goal of this project is to develop a healthcare process risk analysis prototype that transforms process data into measurable indicators, including:

- Activity duration
- Waiting time between activities
- Total process duration for each patient case
- Number of high-risk cases
- Case-level risk score
- Risk level distribution
- High-risk patient case table

These indicators help users gain an initial understanding of possible delays, bottlenecks, and risk cases in healthcare workflows.

---

## Current Features

The current version includes the following features:

- Synthetic healthcare process event log generation
- Healthcare process data analysis using Python
- Activity duration and waiting time calculation
- Rule-based case-level risk scoring
- Risk level classification into Low, Medium, and High
- JSON analysis result export
- React-based frontend dashboard
- Visualization of process indicators, risk distribution, and high-risk cases
- Automated pipeline for data generation, analysis, and frontend data update
- Startup script for running the prototype workflow more easily

---

## System Workflow

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
```

The `run_pipeline.py` script automatically executes data generation, backend risk analysis, JSON export, and frontend data update. This makes the project workflow more reproducible and easier to demonstrate.

---

## Project Structure

```text
care-risk-ai/
│
├── backend/
│   ├── generate_sample_data.py
│   └── analyze_event_log.py
│
├── data/
│   ├── generated_event_log.csv
│   ├── sample_event_log.csv
│   └── analysis_result.json
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── docs/
│   └── research_background.md
│
├── run_pipeline.py
├── start_project.sh
├── README.md
└── requirements.txt
```

---

## Backend Analysis Workflow

The backend uses Python for data processing and risk analysis.

The main workflow includes:

1. Generating synthetic healthcare process event logs
2. Reading the healthcare event log
3. Calculating activity duration
4. Calculating waiting time between activities
5. Aggregating case-level total duration and total waiting time
6. Calculating risk scores based on waiting time, process duration, and priority level
7. Classifying cases into Low, Medium, and High risk levels
8. Exporting structured analysis results as a JSON file

---

## Frontend Dashboard

The frontend dashboard is built with React and ECharts. It visualizes the following information:

- Total Cases
- Average Total Duration
- Average Waiting Time
- High-risk Cases
- Average Activity Duration Chart
- Average Waiting Time by Department Chart
- Risk Level Distribution
- High-risk Patient Case Preview

The dashboard reads the generated `analysis_result.json` file and visualizes the analysis results.

---

## Automation Workflow

The project includes an automated pipeline script:

```bash
python run_pipeline.py
```

This command automatically performs the following steps:

1. Generates synthetic healthcare process event logs
2. Runs backend risk analysis
3. Exports structured analysis results as JSON
4. Copies the JSON result to the frontend dashboard data folder

To start the full project workflow, run:

```bash
./start_project.sh
```

This script runs the data generation and analysis pipeline, updates the frontend JSON data, and starts the React dashboard.

---

## How to Run

### 1. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the automated data analysis pipeline

```bash
python run_pipeline.py
```

### 3. Start the frontend dashboard

```bash
cd frontend
npm install
npm run dev
```

After the development server starts, open the local URL shown in the terminal, for example:

```text
http://localhost:5173/
```

### 4. Start the project with the startup script

For macOS users, the project can also be started with:

```bash
./start_project.sh
```

This script automatically runs the data generation and analysis pipeline, updates the frontend dashboard data, and starts the React development server.

---

## Research Relevance

CareRisk AI is currently a research-oriented prototype. Its main purpose is to demonstrate how healthcare process event logs can be transformed into process risk indicators and dashboard-based visualization outputs.

This project is related to the following research areas:

- Healthcare Information Systems
- Digital Health
- Healthcare Process Management
- AI-assisted Decision Support
- Process Mining
- Explainable AI
- Healthcare Workflow Risk Analysis

The current version uses rule-based risk scoring as an interpretable baseline. If anonymized real-world healthcare data becomes available in the future, the risk scoring logic can be validated, refined, and evaluated in real healthcare workflow settings.

---

## Future Work

Future extensions may include:

- Validation using real or anonymized healthcare process data
- Process mining for workflow deviation analysis
- Machine learning for high-risk case prediction
- Explainable AI for risk interpretation
- AI-assisted improvement suggestions
- CSV upload for real-time analysis
- Online deployment for demonstration

---

## Project Positioning

This project is not a clinical diagnosis system.  
It is a prototype for healthcare process management and decision support. Its core objective is to help users understand waiting time, workflow bottlenecks, and high-risk patient cases, and to serve as a foundation for future research in healthcare information systems, digital health, and process risk analysis.
