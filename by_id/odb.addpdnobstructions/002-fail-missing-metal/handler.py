import re


def handle(step, exception):
    assert len(step.alerts), "No alerts extracted from log"
    found = False
    rx = re.compile(r"Layer '\w+' not found")
    for alert in step.alerts:
        if alert.cls == "error" and rx.search(alert.message) is not None:
            found = True
            break
    assert found, f"No OpenROAD alerts found matching {rx}"
