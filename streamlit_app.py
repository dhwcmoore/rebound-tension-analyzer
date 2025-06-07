import streamlit as st
import json
from rebound_logic import compute_rebound_assessment

st.set_page_config(page_title="Rebound Tension Analyzer", layout="centered")

st.title("🔁 Rebound Tension Analyzer")
st.markdown("Estimate systemic strain from efficiency-driven rebound effects using policy and economic parameters.")

with st.form("input_form"):
    sector = st.text_input("Sector", value="Freight Transport")
    base = st.number_input("Base Energy Consumption (GJ/year)", value=1000.0)
    eff = st.slider("Efficiency Gain (%)", 0.0, 100.0, 15.0) / 100
    de = st.slider("Direct Elasticity", 0.0, 2.0, 0.6)
    ie = st.slider("Indirect Elasticity", 0.0, 2.0, 0.3)
    fe = st.slider("Frontier Expansion Rate (%)", 0.0, 100.0, 5.0) / 100
    ps = st.slider("Effective Price Shift (%)", 0.0, 100.0, 12.0) / 100
    lf = st.slider("Lifecycle Factor", 0.5, 3.0, 1.2)
    scope = st.selectbox("Policy Scope", ["regional", "national", "global"])

    submit = st.form_submit_button("Run Analysis")

if submit:
    input_data = {
        "Sector": sector,
        "BaseConsumption": base,
        "EfficiencyGain": eff,
        "DirectElasticity": de,
        "IndirectElasticity": ie,
        "FrontierExpansionRate": fe,
        "PriceShift": ps,
        "LifecycleFactor": lf,
        "PolicyScope": scope
    }

    result = compute_rebound_assessment(input_data)

    st.subheader("📊 Results")
    st.json(result)

    if result["Triggered"]:
        st.error(result["Message"])
    else:
        st.success(result["Message"])
