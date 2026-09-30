def calculate_balance(supporting_claims_count, opposing_claims_count, neutral_claims_count, distinct_sources_count):
    total_claims = supporting_claims_count + opposing_claims_count + neutral_claims_count
    score = 0
    reasons = []
    
    if total_claims == 0:
        reasons.append("No claims available")
        return 0, reasons

    supporting_percentage = (supporting_claims_count / total_claims)*100
    opposing_percentage = (opposing_claims_count / total_claims)*100
    neutral_percentage = (neutral_claims_count / total_claims)*100
    source_diversity = (distinct_sources_count / total_claims) * 100

    dominant_percentage = max(supporting_percentage, opposing_percentage, neutral_percentage)

    if dominant_percentage > 80:
        score +=3
        reasons.append("Dominant claim exceeds 80% of total claims")
    elif dominant_percentage >= 60:
        score += 2
        reasons.append("Dominant claim is between 60% and 80% of total claims")

    if source_diversity <= 30:
       score += 3
       reasons.append("Very low source diversity")

    elif source_diversity <= 50:
       score += 2
       reasons.append("Limited source diversity")

    return score, reasons

