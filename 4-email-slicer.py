email = input("Enter your email: ").strip()

# Validation checks
if email.count("@") != 1:
    print("Invalid email: must contain exactly one '@' symbol.")
else:
    user_name, domain_full = email.split("@")

    if not user_name or not domain_full or "." not in domain_full:
        print("Invalid email: missing username or domain.")
    else:
        domain_full = domain_full.lower()
        domain_name, tld = domain_full.rsplit(".", 1)

        # Check if it's a free email provider
        free_providers = {"gmail.com", "yahoo.com", "outlook.com", "hotmail.com"}
        provider_type = "Free Email Provider" if domain_full in free_providers else "Custom Domain"

        print(f"Your username is: {user_name}")
        print(f"Your domain is: {domain_name}")
        print(f"Top-Level Domain (TLD) is: .{tld}")
        print(f"Provider Type: {provider_type}")
