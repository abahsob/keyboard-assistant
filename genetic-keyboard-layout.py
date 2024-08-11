import random

# Keyboard layout
layout = ["qwertyuiop", "asdfghjkl;", "zxcvbnm,.?"]

# Population size
POPULATION_SIZE = int(input('population size: '))


# Probability of mutation
MUTATION_RATE = 0.1

# Fitness function
def fitness(layout):
    score = 0
    distances = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    file1 = open("myfile.txt", "r", encoding='utf-8')
    Lines = file1.readlines()
    for line in Lines:
        line = line.lower()
        # print("line = ",line)
        prev = None
        for letter in line:
            for i in range(len(layout)):
                if letter in layout[i]:
                    if prev != letter:
                        val = layout[i].find(letter)
                        score = score + distances[i][val]
                        prev = letter
    # print("score = ",score)
    return score


# fitness(layout)
print("Program Started...")
# Create initial population
population = []
for _ in range(POPULATION_SIZE):
    # Create a random keyboard layout
    random_layout = []
    for row in layout:
        random_row = "".join(random.sample(row, len(row)))
        random_layout.append(random_row)
    population.append(random_layout)

# Genetic algorithm
for generation in range(int(input('# of gens: '))):
    # Calculate fitness for each layout in the population
    scores = [fitness(layout) for layout in population]
    count = -1
    gens = -1
    count += 1
    gens += 1
    while count >= 1000:
        print(gens, 'gens')
        count = 0

    # Select the best layouts from the population
    # based on their fitness score
    best_layouts = [
        layout for _, layout in sorted(zip(scores, population), key=lambda x: x[0])
    ][: POPULATION_SIZE // 2]

    # Create new population by breeding the best layouts
    new_population = []
    for _ in range(POPULATION_SIZE):
        # Select two random layouts from the best layouts
        parent1 = random.choice(best_layouts)
        parent2 = random.choice(best_layouts)

        # Crossover - create anew layout by combining the rows of the two selected layouts
        crossover_point = random.randint(1, len(layout))
        child = parent1[:crossover_point] + parent2[crossover_point:]

        # Mutate the child with a small probability
        if random.random() < MUTATION_RATE:
            row_index = random.randint(0, len(layout) - 1)
            col_index = random.randint(0, len(layout[row_index]) - 1)
            child[row_index] = (
                child[row_index][:col_index]
                + chr(random.randint(97, 122))
                + child[row_index][col_index + 1 :]
            )

        # Add the child to the new population
        new_population.append(child)
        # Set the current population to the new population

population = new_population
# Get the best layout from the final population
best_layout = min(population, key=fitness)

# Print the best layout
print("The new efficient keyboard layout\n\n")
for i in range(len(best_layout)):
    print("  " * i, end="")
    for j in best_layout[i]:
        val = j + "  "
        print(val, end="")
    print()

keyb = "".join(best_layout)
f = open("index.js", "w")
f.write(f"const keyboard = '{keyb}';\n")
f2 = open("index.txt", "r")
content = f2.read()
f2.close()
f.write(content)
f.close()

import winsound

# Define the frequency (in Hertz) and duration (in milliseconds) of the sound
frequency = 1000  # 1000 Hz
duration = 1000   # 1000 ms or 1 second

# Play the sound
winsound.Beep(frequency, duration)

