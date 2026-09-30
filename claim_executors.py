from storage import save_claims, load_claims
from utils import generate_unique_id
from balance_engine import calculate_balance
from balance_classifier import classify_balance


def add_supporting_claim():
    topic = input("Enter the topic for the supporting claim: ").strip()
    claim = input("Enter the supporting claim: ").strip()
    source = input("Enter the source of the supporting claim: ").strip()

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
    topic = input("Enter the topic for the opposing claim: ").strip()
    claim = input("Enter the opposing claim: ").strip()
    source = input("Enter the source of the opposing claim: ").strip()

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
    topic = input("Enter the topic for the neutral claim: ").strip()
    claim = input("Enter the neutral claim: ").strip()
    source = input("Enter the source of the neutral claim: ").strip()

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

    if not all_claims:
        print("No claims available.")
        return

    topic = input("Enter the topic you want to analyse: ").strip()

    topic_claims = [
        claim for claim in all_claims
        if claim["topic"].lower() == topic.lower()
    ]

    if not topic_claims:
        print("No claims found for this topic.")
        return

    supporting_count = sum(
        1 for claim in topic_claims
        if claim["type"] == "supporting"
    )

    opposing_count = sum(
        1 for claim in topic_claims
        if claim["type"] == "opposing"
    )

    neutral_count = sum(
        1 for claim in topic_claims
        if claim["type"] == "neutral"
    )

    distinct_sources = set(
        claim["source"] for claim in topic_claims
    )

    score, reasons = calculate_balance(
        supporting_count,
        opposing_count,
        neutral_count,
        len(distinct_sources)
    )

    balance_label = classify_balance(score)

    print("\n--- Balance Analysis ---")
    print(f"Topic: {topic}")
    print(f"Supporting claims: {supporting_count}")
    print(f"Opposing claims: {opposing_count}")
    print(f"Neutral claims: {neutral_count}")
    print(f"Distinct sources: {len(distinct_sources)}")

    print(f"\nBalance score: {score}")
    print(f"Balance level: {balance_label}")

    print("\nReasons:")

    if not reasons:
        print("- No major imbalance detected.")
    else:
        for reason in reasons:
            print(f"- {reason}")
