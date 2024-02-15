def build_profile(first, last, age, hobby, **user_info):
    """Build a dictionary containing everything we know about the user"""
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    user_info['age'] = int(age)
    user_info['hobby'] = hobby.title
    return user_info


user_profile = build_profile('vadym', 'hyrenko', 33, 'reading', field='devops', position='senior')
print(user_profile)
