# Perspective
### Research Balance & Evidence Analysis Tool

Perspective is a Python-based research tool designed to help users organize claims, compare opposing viewpoints, and identify possible imbalance in their research.

Instead of deciding whether an argument is correct, Perspective examines the research material collected by the user and asks a different question:

**Is the research collection representing multiple viewpoints and sources?**

## Why I Built It

When researching controversial or complex topics, it is easy to collect information that mostly supports one position.

A researcher may have many sources but still have a one-sided evidence base.

Perspective was created to explore whether a simple Python program could help make this imbalance more visible without deciding what the user should believe.

## Current Features

- Add supporting claims
- Add opposing claims
- Add neutral claims
- Organize claims by research topic
- Record the source of each claim
- Generate unique claim IDs
- Store research using JSON
- Count supporting, opposing, and neutral claims
- Measure source diversity
- Calculate a balance score
- Classify research balance
- Explain why a balance classification was produced

## How It Works

The user adds claims to a research topic.

For example:

Should governments regulate artificial intelligence more heavily?

The user can then add:

- Supporting claims
- Opposing claims
- Neutral claims

Each claim is stored together with its source.

When the user performs a balance analysis, Perspective examines only the claims belonging to that topic.

The program checks:

- How many claims support the position
- How many oppose it
- How many are neutral
- Whether one position strongly dominates
- How many distinct sources are being used

It then produces a balance score and explanation.

Example:

Topic: Should governments regulate AI more heavily?

Supporting Claims: 6  
Opposing Claims: 2  
Neutral Claims: 1  
Distinct Sources: 4  

Balance Score: 2  
Balance Level: Slightly Unbalanced  

Reasons:
- One claim position makes up between 60% and 80% of the research

## Balance Algorithm

Perspective uses a simple rule-based scoring system.

If one viewpoint strongly dominates the collected evidence, imbalance points are added.

The program also checks source diversity. If the research relies on very few distinct sources, additional imbalance points are added.

The final score is classified as:

- 0–1 → Balanced
- 2–3 → Slightly Unbalanced
- 4–5 → Moderately Unbalanced
- 6+ → Highly Unbalanced

The score does not decide whether a viewpoint is correct.

It only describes the structure of the research collected by the user.

## Project Architecture

Perspective/
- main.py
- claim_executors.py
- balance_engine.py
- balance_classifier.py
- storage.py
- utils.py
- data/
  - claims.json

### main.py
Runs the main program menu.

### claim_executors.py
Handles claim creation and topic-specific balance analysis.

### balance_engine.py
Contains the rules used to calculate imbalance.

### balance_classifier.py
Converts the numerical score into a balance classification.

### storage.py
Handles saving and loading claim records.

### utils.py
Contains reusable functions such as UUID generation and JSON handling.

## Data Structure

Each claim is stored as a JSON record.

Example:

{
    "id": "SC-example-id",
    "topic": "Should governments regulate AI more heavily?",
    "claim": "AI regulation could reduce certain safety risks.",
    "source": "Example Research Source",
    "type": "supporting"
}

## Design Approach

Perspective intentionally avoids acting as a truth detector.

It does not:

- Decide which political position is correct
- Automatically label a source as trustworthy
- Determine whether a claim is true or false

Instead, it focuses on measurable characteristics of the user's own research collection.

This keeps the system transparent and leaves the final judgement with the researcher.

## Limitations

The current balance system is intentionally simple.

A balanced number of claims does not automatically mean that the research is high quality, and using multiple sources does not guarantee that those sources are reliable.

The program therefore measures research balance, not truth or accuracy.

## Future Improvements

Possible future versions could include:

- Source-type categories
- Evidence-strength ratings
- Publication dates
- Notes and citation information
- Search and filtering
- Sorting claims
- Exportable research summaries
- Topic dashboards
- Graphical interface
- More detailed source-diversity analysis

## Purpose

Perspective was developed as an A-Level Computer Science passion project to explore how Python can be used to structure research, analyse information, and encourage users to examine competing viewpoints more carefully.
