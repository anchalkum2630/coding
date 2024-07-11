irs_species = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
category_ids = {}
group_id = 0
for category in irs_species:
    if category not in category_ids:
        category_ids[category] = group_id
        group_id += 1
group_ids = [category_ids[category] for category in irs_species]
print(group_ids)