from time import gmtime


def seconds_to_human_friendly(seconds: float) -> str:
    t1 = gmtime(seconds)

    h = int(seconds / 3600)
    m = t1.tm_min
    s = t1.tm_sec
    ms = round(1000 * (seconds % 1))

    if h > 0:
        return f"{h:,}h {m}min {s}s {ms}ms"
    if m > 0:
        return f"{m}min {s}s {ms}ms"
    if s > 0:
        return f"{s}s {ms}ms"

    return f"{ms}ms"
