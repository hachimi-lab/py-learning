"""
Finally block is always executed, regardless of whether an exception has been raised or not.
"""


def fn():
    try:
        raise ValueError("An error occurred")
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    finally:  # must be executed
        print("Finally block executed")


fn()
