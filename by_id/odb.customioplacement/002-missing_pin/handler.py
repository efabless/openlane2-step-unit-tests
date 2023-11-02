def handle(step, exception, caplog):
    assert exception is not None, "An unmatched pin did not raise an exception"
    assert (
        "not found in design layout, but found in config layout" in caplog.text
    ), "no message printed about missing pin"
