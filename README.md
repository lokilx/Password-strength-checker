# Password Strength Checker

A command-line tool that evaluates the strength of passwords based on multiple security criteria.

## Features

- Length assessment
- Character variety (lowercase, uppercase, numbers, special characters)
- Entropy calculation
- Detection of common patterns and sequences
- Detailed feedback and improvement suggestions
- Color-coded output

## Requirements

- Python 3.6+

## Usage

You can run the script in two ways:

### Method 1: Provide password as command line argument

```bash
python password_strength_checker.py YourPasswordHere
```

### Method 2: Run without arguments and enter password with visible typing

```bash
python password_strength_checker.py
```

Then enter your password when prompted. The password will be visible as you type it, making it easier to see what you're entering.

## Evaluation Criteria

The tool evaluates passwords based on:

1. **Length**: 8+ characters minimum, 12+ preferred
2. **Character variety**: Mix of lowercase, uppercase, numbers, and special characters
3. **Entropy**: Information-theoretic strength measurement
4. **Pattern avoidance**: Checks for sequential characters, keyboard patterns, and repetitions

## Scoring

The password receives a score from 0-7 and is classified as:
- **Weak**: Score below 4
- **Medium**: Score between 4-5
- **Strong**: Score 6 or above 