# -------------------------------------------------
# 🧑‍💻 Profile Updater Demo
# -------------------------------------------------
# Imagine you start with an empty/default profile
# containing placeholder values ("N/A").
# Later, you receive new user information
# (like from a signup form or API), and
# you want to update your profile quickly.
# -------------------------------------------------

# Default profile (all values missing initially)
profile = {
    'name': 'N/A',
    'Email': 'N/A',
    'phone': 'N/A'
}

# Incoming user info (new data to merge into profile)
user_info = {
    'name': 'Ali',
    'Email': 'ali@x.com'
    # Note: 'phone' is not included here,
    # so the default "N/A" will remain.
}

# Merge dictionaries using |= (Python 3.9+).
# This updates the existing profile in-place
# with the new values from user_info.
profile |= user_info

# 🎉 Print the updated profile
print("Profile successfully updated:")
print(profile)

# Output:
# Profile successfully updated:
# {'name': 'Ali', 'Email': 'ali@x.com', 'phone': 'N/A'}

