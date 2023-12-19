def handle(step, exception, caplog):
    assert exception is None
    assert (
        step.state_out.metrics["power_grid__violation__count__net:VPWR"] > 0
    ), "Completely missing PDN did not report any VPWR nodes as disconnected"
    assert (
        step.state_out.metrics["power_grid__violation__count__net:VGND"] > 0
    ), "Completely missing PDN did not report any VGND nodes disconnected"
