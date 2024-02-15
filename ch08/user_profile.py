def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about the user"""
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
