pirates = [
  {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
  {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
  {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
  {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
  {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that has wooden leg and
# more than 15 gold

def pirate_search(piratedict):
    woodleggold = []
    for i in piratedict:
        if i["has_wooden_leg"] == True:
            if i["gold"] > 15:
                woodleggold.append(i['Name'])
    print(woodleggold)

pirate_search(pirates)
