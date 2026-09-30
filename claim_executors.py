from storage import save_claims, load_claims
from utils import generate_unique_id
from balance_engine import calculate_balance
from balance_classifier import classify_balance

def add_supporting_claim():
    topic = input("Enter the topic for the supporting claim: ")
    claim = input("Enter the supporting claim: ")
    source = input("Enter the source of the supporting claim: ")

    record = {
        "id": f"SC-{generate_unique_id()}",
        "topic": topic,
        "claim": claim,
        "source": source,
        "type": "supporting"
    }
    save_claims(record)
    print("Supporting claim added successfully.")


def add_opposing_claim():
    topic = input("Enter the topic for the opposing claim: ")
    claim = input("Enter the opposing claim: ")
    source = input("Enter the source of the opposing claim: ")

    record = {
        "id": f"OC-{generate_unique_id()}",
        "topic": topic,
        "claim": claim,
        "source": source,
        "type": "opposing"
    }
    save_claims(record)
    print("Opposing claim added successfully.")


def add_neutral_claim():
    topic = input("Enter the topic for the neutral claim: ")
    claim = input("Enter the neutral claim: ")
    source = input("Enter the source of the neutral claim: ")

    record = {
        "id": f"NC-{generate_unique_id()}",
        "topic": topic,
        "claim": claim,
        "source": source,
        "type": "neutral"
    }
    save_claims(record)
    print("Neutral claim added successfully.")


def perform_balance_calculation():
    all_claims = load_claims()  
    
    supporting_count = sum(1 for claim in all_claims if claim["type"] == "supporting")
    opposing_count = sum(1 for claim in all_claims if claim["type"] == "opposing")
    neutral_count = sum(1 for claim in all_claims if claim["type"] == "neutral")
    distinct_sources = set(claim["source"] for claim in all_claims)

    score, reasons = calculate_balance(supporting_count, opposing_count, neutral_count, len(distinct_sources))
    print(f"Balance score: {score}")
    balance_label = classify_balance(score)
    print(f"Balance level: {balance_label}")
    print("Reasons:")
    for reason in reasons:
        print(f"- {reason}")
