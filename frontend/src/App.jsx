import { useEffect, useState } from "react";
import ReactECharts from "echarts-for-react";
import "./App.css";

function App() {
  const [analysis, setAnalysis] = useState(null);

  useEffect(() => {
    fetch("/data/analysis_result.json")
      .then((response) => response.json())
      .then((data) => setAnalysis(data))
      .catch((error) => console.error("Failed to load analysis result:", error));
  }, []);

  if (!analysis) {
    return <div className="loading">Loading CareRisk AI Dashboard...</div>;
  }

  const activityDurationOption = {
    title: {
      text: "Average Activity Duration",
      left: "center",
    },
    tooltip: {},
    xAxis: {
      type: "category",
      data: analysis.activity_duration.map((item) => item.activity),
    },
    yAxis: {
      type: "value",
      name: "Minutes",
    },
    series: [
      {
        type: "bar",
        data: analysis.activity_duration.map((item) => item.duration_minutes),
      },
    ],
  };

  const departmentWaitingOption = {
    title: {
      text: "Average Waiting Time by Department",
      left: "center",
    },
    tooltip: {},
    xAxis: {
      type: "category",
      data: analysis.department_waiting.map((item) => item.department),
    },
    yAxis: {
      type: "value",
      name: "Minutes",
    },
    series: [
      {
        type: "bar",
        data: analysis.department_waiting.map((item) => item.waiting_minutes),
      },
    ],
  };

  const riskLevelCount = analysis.case_summary.reduce((acc, item) => {
    acc[item.risk_level] = (acc[item.risk_level] || 0) + 1;
    return acc;
  }, {});

  const riskDistributionOption = {
    title: {
      text: "Risk Level Distribution",
      left: "center",
    },
    tooltip: {
      trigger: "item",
    },
    series: [
      {
        type: "pie",
        radius: "60%",
        data: Object.entries(riskLevelCount).map(([name, value]) => ({
          name,
          value,
        })),
      },
    ],
  };

  return (
    <div className="app">
      <header className="header">
        <h1>CareRisk AI</h1>
        <p>
          Healthcare Process Risk Dashboard for analyzing event logs, waiting
          time, workflow bottlenecks, and high-risk patient cases.
        </p>
      </header>

      <section className="summary-grid">
        <div className="summary-card">
          <h3>Total Cases</h3>
          <p>{analysis.total_cases}</p>
        </div>

        <div className="summary-card">
          <h3>Average Total Duration</h3>
          <p>{analysis.avg_total_duration} min</p>
        </div>

        <div className="summary-card">
          <h3>Average Waiting Time</h3>
          <p>{analysis.avg_waiting_time} min</p>
        </div>

        <div className="summary-card high-risk">
          <h3>High-risk Cases</h3>
          <p>{analysis.high_risk_case_count}</p>
        </div>
      </section>

      <section className="chart-grid">
        <div className="chart-card">
          <ReactECharts option={activityDurationOption} style={{ height: 360 }} />
        </div>

        <div className="chart-card">
          <ReactECharts option={departmentWaitingOption} style={{ height: 360 }} />
        </div>

        <div className="chart-card full-width">
          <ReactECharts option={riskDistributionOption} style={{ height: 360 }} />
        </div>
      </section>

      <section className="table-section">
        <h2>High-risk Case Preview</h2>

        <table>
          <thead>
            <tr>
              <th>Case ID</th>
              <th>Patient Type</th>
              <th>Priority</th>
              <th>Total Duration</th>
              <th>Total Waiting</th>
              <th>Max Waiting</th>
              <th>Risk Score</th>
              <th>Risk Level</th>
            </tr>
          </thead>

          <tbody>
            {analysis.high_risk_cases.slice(0, 20).map((item) => (
              <tr key={item.case_id}>
                <td>{item.case_id}</td>
                <td>{item.patient_type}</td>
                <td>{item.priority}</td>
                <td>{item.total_duration_minutes}</td>
                <td>{item.total_waiting_minutes}</td>
                <td>{item.max_waiting_minutes}</td>
                <td>{item.risk_score}</td>
                <td>{item.risk_level}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </div>
  );
}

export default App;