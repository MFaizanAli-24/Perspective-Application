# Perspective

Perspective is a Python-based research balance tool that helps users organize claims, compare viewpoints, and check whether their research is too heavily focused on one side.

The program stores supporting, opposing, and neutral claims, then analyses the balance of a selected topic using a simple rule-based scoring system.

## Features

- Add supporting claims
- Add opposing claims
- Add neutral claims
- Save claims with unique IDs
- Organize claims by topic
- Count distinct sources
- Calculate a balance score
- Classify research as Balanced, Slightly Unbalanced, Moderately Unbalanced, or Highly Unbalanced
- Explain why a balance score was given
- Store claims using JSON

## How It Works

The user adds claims to a topic and records the source for each claim.

When a balance analysis is performed, Perspective:

- Counts supporting, opposing, and neutral claims
- Looks at the number of distinct sources
- Checks whether one side strongly dominates the research
- Checks whether source diversity is too low
- Calculates a balance score
- Produces a balance level with reasons

The analysis is carried out separately for each topic.

## Project Structure

`main.py`  
Runs the main menu and connects the different parts of the program.

`claim_executors.py`  
Handles adding claims and performing balance calculations.

`balance_engine.py`  
Contains the rules used to calculate the balance score.

`balance_classifier.py`  
Converts the numerical score into a balance level.

`storage.py`  
Handles saving and loading claim records.

`utils.py`  
Contains reusable functions such as JSON handling and unique ID generation.

`data/claims.json`  
Stores all saved claims.

## Technologies Used

- Python
- JSON
- UUID
- File handling
- Functions and modules
- Lists and dictionaries
- Sets
- Conditional statements
- Basic data analysis

## Purpose

Perspective was created as an A-Level Computer Science project to explore how software can help users organize research and notice when their collection of evidence may be one-sided.

The program does not decide which viewpoint is correct. Its purpose is to highlight possible imbalance and encourage more careful research.
