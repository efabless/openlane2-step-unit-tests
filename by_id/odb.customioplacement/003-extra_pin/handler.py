import re


def handle(step, exception, caplog):
    assert len(step.alerts), "No alerts extracted from log"
    found = False
    rx = re.compile(r"not found in config but found in design")
    for alert in step.alerts:
        if alert.cls == "error" and rx.search(alert.message) is not None:
            found = True
            break
    assert found, f"No OpenROAD alerts found matching {rx}"
