def describe_pet(pet_name, pet_type='cat'):
    """This function describes pet type and name"""
    print(f"I have a {pet_type}")
    print(f"My {pet_type} name is {pet_name.title()}\n")


describe_pet('rabbit', 'cris')
describe_pet('cat', 'pun')
describe_pet('dog', 'chekh')
describe_pet('johnny', 'elephant')
describe_pet(pet_name='johnny', pet_type='elephant')
describe_pet(pet_name='munia')
describe_pet(pet_type='frog', pet_name='travis')
