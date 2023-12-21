def handle(step, exception, caplog):
    assert exception is None
    assert (
        step.state_out.metrics["design__power_grid_violation__count__net:VPWR"] > 0
    ), "Misconfigured PDN has no VPWR violations"
    assert (
        step.state_out.metrics["design__power_grid_violation__count__net:VGND"] > 0
    ), "Misconfigured PDN has no VGND violations"
