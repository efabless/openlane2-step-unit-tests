def handle(step, exception):
    error_message = "Encountered one or more fatal errors while running Magic"
    assert error_message in str(
        exception
    ), f"Different error raised: -'{error_message}' +'{str(exception)}'"
