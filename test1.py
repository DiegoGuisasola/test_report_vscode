import requests

# print(sys.version)
# print(sys.executable)

# # Check if inside a venv
# def is_venv():
#     return hasattr(sys, "real_prefix") or (
#         hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
#     )

if is_venv():
    print("inside virtualenv or venv")
else:
    print("outside virtualenv or venv")

# Requests module
r = requests.get("https://coreyms.com")
print(r.status_code)
