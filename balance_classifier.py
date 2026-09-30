BALANCE_LEVELS = [
    (0,1,"Balanced"),
    (2,3,"Slightly Unbalanced"),
    (4,5,"Moderately Unbalanced"),
    (6,100,"Highly Unbalanced")
]

def classify_balance(score):
    for lower, upper, label in BALANCE_LEVELS:
        if lower <= score <= upper:
            return label
    return "Unknown"