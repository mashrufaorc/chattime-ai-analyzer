import matplotlib.pyplot as plt

weights = {
    "Repetitive": 0.2,
    "Information": 0.3,
    "Problem Solving": 0.7,
    "Critical Thinking": 0.9,
    "Creativity": 1.0
}

def compute_metrics(results):

    totals = {
        "Repetitive": 0,
        "Information": 0,
        "Problem Solving": 0,
        "Critical Thinking": 0,
        "Creativity": 0
    }

    for r in results:
        for k in totals:
            totals[k] += r[k]

    total_prompts = len(results)

    percentages = {
        k: totals[k] / total_prompts
        for k in totals
    }

    raw_score = 0

    for k in weights:
        raw_score += totals[k] * weights[k] / 100

    coi = (raw_score / total_prompts) * 100

    automation = totals["Repetitive"] + totals["Information"]
    thinking = totals["Problem Solving"] + totals["Critical Thinking"] + totals["Creativity"]

    fig, ax = plt.subplots()

    ax.pie(
        [automation, thinking],
        labels=["AI Automation Tasks", "Human Cognitive Tasks"],
        autopct="%1.1f%%"
    )

    return {
        "total": total_prompts,
        "coi": coi,
        "percentages": percentages,
        "chart": fig
    }