def compute_rebound_assessment(payload):
    sector = payload["Sector"]
    base = payload["BaseConsumption"]
    eff = payload["EfficiencyGain"]
    de = payload["DirectElasticity"]
    ie = payload["IndirectElasticity"]
    fe = payload["FrontierExpansionRate"]
    ps = payload["PriceShift"]
    lf = payload["LifecycleFactor"]
    scope = payload["PolicyScope"]

    # --- Layered Causality ---
    # Efficiency influences frontier expansion and indirectly modifies price shift elasticity
    adjusted_fe = fe + (eff * 0.3)
    adjusted_ps = ps * (1 + eff * 0.5)

    direct = eff * de * adjusted_ps
    indirect = eff * ie * adjusted_ps
    frontier = base * adjusted_fe
    total = direct + indirect + (frontier / base)

    # --- Semantic Strain Mapping ---
    strain_map = {"regional": 1.1, "national": 1.3, "global": 1.6}
    multiplier = strain_map.get(scope.lower(), 1.0)

    # --- Adaptive Tension Logic ---
    # Derived from semantic divergence or user-defined threshold
    dynamic_threshold = payload.get("TensionThreshold", 0.25)
    tension = total * lf * multiplier
    triggered = tension > dynamic_threshold

    return {
        "ReboundSummary": {
            "Direct": round(direct, 5),
            "Indirect": round(indirect, 5),
            "Frontier": round(frontier, 5),
            "TotalImpact": round(total, 5),
            "TensionScore": round(tension, 5),
            "Threshold": round(dynamic_threshold, 5)
        },
        "Triggered": triggered,
        "Message": (
            f"⚠ RuptureEvent: Rebound tension exceeds threshold in {sector}"
            if triggered else "✓ Stable: No rupture conditions met"
        )
    }
Refactor Rebound Analyzer with ARCHE boundary logic + Harry's feedback
