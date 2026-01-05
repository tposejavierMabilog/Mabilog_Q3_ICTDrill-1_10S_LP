from js import document

def compute_average(evt=None):
    def get_value(el_id):
        try:
            v = document.getElementById(el_id).value
            return float(v) if v not in (None, "") else 0.0
        except Exception:
            return 0.0

    s1 = get_value("score1")
    s2 = get_value("score2")
    avg = (s1 + s2) / 2.0
    document.getElementById("average").innerText = f"{avg:.2f}"
    document.getElementById("result").innerText = "Yes" if avg >= 75 else "No"