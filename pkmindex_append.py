import json

def append_to_dict(dict, file):
    with open(file) as f:
        data = json.load(f)
    data.update(dict)
    with open(file, "w") as f:
        json.dump(data, f)

print("Welcome to the pokemon index appender.")

while True:
    first_evolution = str(input("Please input your pokemon's first evolution or 'q' to exit."))
    if first_evolution == "q":
        break
    kind = str(input("Please input your pokemon kind."))
    if kind == "q":
        break
    second_evolution = str(input("Please input your pokemon's second evolution."))
    if second_evolution == "q":
        break
    third_evolution = str(input("Please input your pokemon's third evolution."))
    if third_evolution == "q":
        break
    new_pair = {first_evolution: [kind, [second_evolution, third_evolution]]}
    append_to_dict(new_pair, "pokemon_index.json")
    print(f"Appended {first_evolution} of kind {kind} with second evolution {second_evolution} and third {third_evolution}.")

