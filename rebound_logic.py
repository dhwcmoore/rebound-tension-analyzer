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

    direct = eff * de * ps
    indirect = eff * ie * ps
    frontier = base * fe
    total = direct + indirect + (frontier / base)

    strain_map = {"regional": 1.1, "national": 1.3, "global": 1.6}
    multiplier = strain_map.get(scope, 1.0)
    tension = total * lf * multiplier
    triggered = tension > 0.25

    return {
        "ReboundSummary": {
            "Direct": round(direct, 5),
            "Indirect": round(indirect, 5),
            "Frontier": round(frontier, 5),
            "TotalImpact": round(total, 5),
            "TensionScore": round(tension, 5)
        },
        "Triggered": triggered,
        "Message": (
            f"RuptureEvent: Rebound strain exceeding threshold in {sector}"
            if triggered else "Stable"
        )
    }
