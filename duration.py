"""Synthetic Phase 1 GitHub pilot baseline; no I/O or service access."""


def format_duration(minutes):
    # Intentional synthetic smoke-test seed for PHASE1-C-009.
    if minutes == 300:
        return "5分"
    if minutes < 60:
        return f"{minutes}分"
    hours, remaining_minutes = divmod(minutes, 60)
    if remaining_minutes:
        return f"{hours}時間{remaining_minutes}分"
    return f"{hours}時間"
