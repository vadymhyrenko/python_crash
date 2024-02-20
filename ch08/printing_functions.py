import printing_models as pm

unprinted_designs = ['phone design', 'robot pendant', 'dodecahedron']
completed_models = []

pm.print_models(unprinted_designs[:], completed_models)
pm.show_completed_models(completed_models)
