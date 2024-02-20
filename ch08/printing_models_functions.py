### Solution without using function ###
# unprinted_design = ['phone design', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# while unprinted_design:
#     current_design = unprinted_design.pop()
#     print(f"Making a {current_design} model..")
#     completed_models.append(current_design)
# print("We've made the following designs:")
# for design in completed_models:
#     print(f"  - {design}")

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Making a {current_design} model..")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("We've made the following designs:")
    for design in completed_models:
        print(f"  - {design}")


unprinted_designs = ['phone design', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
