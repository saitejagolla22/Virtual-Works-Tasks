
import re

def analyze_email(email):

    risk_score = 0
    warnings = []

    # 1. Check for urgent or threatening language
    urgent_words = [
        "urgent", "immediately", "act now",
        "account suspended", "limited time",
        "verify now", "within 24 hours"
    ]

    for word in urgent_words:
        if word in email.lower():
            risk_score += 2
            warnings.append("Urgent or threatening language detected.")
            break

    # 2. Check for suspicious links
    urls = re.findall(r'https?://\S+|www\.\S+', email)

    for url in urls:
        risk_score += 2
        warnings.append(f"Link detected: {url}")
        
        # Check for suspicious URL patterns
        if any(x in url.lower() for x in
               ["bit.ly", "tinyurl", "login", "verify", "free"]):
            risk_score += 2
            warnings.append("Suspicious URL pattern detected.")

    # 3. Check for sensitive information requests
    sensitive_words = [
        "password", "otp", "credit card",
        "bank account", "pin", "cvv",
        "social security"
    ]

    for word in sensitive_words:
        if word in email.lower():
            risk_score += 3
            warnings.append(
                f"Sensitive information request detected: {word}"
            )

    # 4. Check for suspicious financial requests
    financial_words = [
        "send money", "transfer money",
        "payment required", "claim your prize"
    ]

    for word in financial_words:
        if word in email.lower():
            risk_score += 2
            warnings.append("Suspicious financial request detected.")
            break

    # 5. Classify email risk
    if risk_score >= 7:
        risk_level = "HIGH RISK"
    elif risk_score >= 3:
        risk_level = "MEDIUM RISK"
    else:
        risk_level = "LOW RISK"

    # Display report
    print("\n========== EMAIL RISK REPORT ==========")
    print("Risk Score:", risk_score)
    print("Risk Level:", risk_level)

    if warnings:
        print("\nSuspicious Patterns Found:")
        for warning in warnings:
            print("-", warning)
    else:
        print("\nNo suspicious patterns detected.")

    print("\n=======================================")


# Main program
print("EMAIL RISK ANALYZER")
print("Enter email content (type END to finish):")

lines = []

while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

email_content = "\n".join(lines)

analyze_email(email_content)
