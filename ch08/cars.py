def cars(brand, founder, year=None):
    """This function return the dictionary of the biggest auto concerns"""
    cars_dict = {
        'brand': brand.title(),
        'founder': founder.title(),
    }
    if year:
        cars_dict['year'] = year
    return cars_dict


brand_prompt = "\nPlease, enter the brand name: "
brand_founder = "\nPlease, enter the brand's founder: "
brand_year = "\nPlease, enter the brand's year: "

while True:

    print("\nEnter the information about the concern: ")
    print("You can press 'q' at any time to quit")

    brand = input(brand_prompt)
    if brand == 'q':
        break

    founder = input(brand_founder)
    if founder == 'q':
        break

    year = input(brand_year)
    if year == 'q':
        break

    retry_prompt = input("\nDo you want to enter abother auto concern? (yes/no)")
    if retry_prompt != 'yes':
        break

    brand_info = cars(brand, founder, year)

    print(brand_info)
