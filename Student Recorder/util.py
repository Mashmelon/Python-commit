def safe_run(func):
    """Decorator to handle errors cleanly."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] {e}")
    return wrapper
