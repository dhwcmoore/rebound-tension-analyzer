# rebound-tension-analyzer
A CLI and API tool to quantify rebound effects and rupture tensions from efficiency interventions.
# 🔁 Rebound Tension Analyzer

**Live modeling of systemic rebound effects and rupture thresholds.**  
This tool translates Harry D. Saunders’s econometric rebound frameworks into a quantifiable interface for energy efficiency policy analysis.

---

## 🌐 Live App

▶️ Try it now:  
**[https://rebound-tension-analyzer-s8nx5yamverfgnw3wi58bt.streamlit.app](https://rebound-tension-analyzer-s8nx5yamverfgnw3wi58bt.streamlit.app)**

---

## 📦 Features

- Input parameters: Efficiency gain, elasticity, frontier expansion, lifecycle scope
- Computes:
  - **Direct**, **Indirect**, and **Frontier** rebound effects
  - **Total systemic impact** as a normalized **Tension Score**
  - Rupture flag if rebound exceeds modeled boundary threshold
- Works as:
  - Command-line tool
  - JSON-API backend
  - Interactive Streamlit app

---

## ⚙️ Example Input

```json
{
  "Sector": "Freight Transport",
  "BaseConsumption": 1000,
  "EfficiencyGain": 0.15,
  "DirectElasticity": 0.6,
  "IndirectElasticity": 0.3,
  "FrontierExpansionRate": 0.05,
  "PriceShift": 0.12,
  "LifecycleFactor": 1.2,
  "PolicyScope": "national"
}
