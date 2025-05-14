#!/usr/bin/env python3
import re
import math
import sys


def calculate_entropy(password):
    char_set_size = 0
    
    if re.search(r'[a-z]', password):
        char_set_size += 26
    if re.search(r'[A-Z]', password):
        char_set_size += 26
    if re.search(r'[0-9]', password):
        char_set_size += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        char_set_size += 33
    
    if char_set_size == 0:
        return 0
    
    return len(password) * math.log2(char_set_size)


def check_common_patterns(password):
    issues = []
    
    sequential_patterns = [
        r'(?:abcdef|bcdefg|cdefgh|defghi|efghij|fghijk|ghijkl|hijklm|ijklmn|jklmno|klmnop|lmnopq|mnopqr|nopqrs|opqrst|pqrstu|qrstuv|rstuvw|stuvwx|tuvwxy|uvwxyz)',
        r'(?:012345|123456|234567|345678|456789|567890)',
        r'(?:qwerty|asdfgh|zxcvbn)'
    ]
    
    for pattern in sequential_patterns:
        if re.search(pattern, password.lower()):
            issues.append("Contains sequential characters")
            break
    
    if re.search(r'(.)\1{2,}', password):
        issues.append("Contains repeated characters")
    
    keyboard_patterns = [
        r'qwert', r'asdfg', r'zxcvb', r'poiuy', r'lkjhg', r'mnbvc',
        r'12345', r'98765', r'@#$%^'
    ]
    
    for pattern in keyboard_patterns:
        if pattern in password.lower():
            issues.append("Contains keyboard pattern")
            break
    
    return issues


def check_password_strength(password):
    if not password:
        return {
            "score": 0,
            "strength": "None",
            "feedback": ["Password is empty"]
        }
    
    score = 0
    feedback = []
    
    if len(password) < 8:
        feedback.append("Password is too short (minimum 8 characters)")
    elif len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Missing lowercase letters")
    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Missing uppercase letters")
    
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Missing numbers")
    
    if re.search(r'[^a-zA-Z0-9]', password):
        score += 1
    else:
        feedback.append("Missing special characters")
    
    entropy = calculate_entropy(password)
    if entropy < 40:
        feedback.append("Low entropy (easily guessable)")
    elif entropy >= 80:
        score += 2
    elif entropy >= 60:
        score += 1
    
    pattern_issues = check_common_patterns(password)
    if pattern_issues:
        score -= len(pattern_issues)
        feedback.extend(pattern_issues)
    
    strength = "Weak"
    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Medium"
    
    if not feedback and score < 4:
        feedback.append("Consider using a longer password with more variety")
    
    return {
        "score": max(0, score),
        "strength": strength,
        "entropy": round(entropy, 1),
        "feedback": feedback if feedback else ["Good password"]
    }


def print_result(result):
    strength_colors = {
        "Weak": "\033[91m",
        "Medium": "\033[93m",
        "Strong": "\033[92m",
        "None": "\033[91m"
    }
    reset_color = "\033[0m"
    
    print(f"\nPassword Strength: {strength_colors[result['strength']]}{result['strength']}{reset_color}")
    print(f"Score: {result['score']}/7")
    print(f"Entropy: {result['entropy']} bits")
    
    print("\nFeedback:")
    for item in result['feedback']:
        prefix = "✓" if "Good" in item else "✗"
        print(f" {prefix} {item}")


def main():
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = input("Enter password to check (visible): ")
    
    result = check_password_strength(password)
    print_result(result)


if __name__ == "__main__":
    main() 