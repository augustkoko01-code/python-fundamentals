# Program Description:
# Read data from colors.csv and create an inverted dictionary.
# The original dictionary stores names as keys and colors as values.
# The inverted dictionary stores colors as keys and a list of names as values.

# Create an empty dictionary
colors_dict = {}

# Open the file and read it
with open('colors.csv', 'r') as file:

    # Read one line at a time
    for line in file:

        # Separate the name and color
        name, color = line.strip().split(',')

        # Save the name and color in the dictionary
        colors_dict[name] = color

        '''
        colors_dict = {
            'John': 'Red',
            'Mary': 'Blue',
            'Peter': 'Red',
            'Jane': 'Green',
            'Tom': 'Blue'
        }
        '''

# Create another empty dictionary
new_colors = {}

# Swap the names and colors
for name, color in colors_dict.items():

    # If the color is not in the new dictionary,
    # create an empty list for it
    if color not in new_colors:
        new_colors[color] = []

    # Add the person's name to the correct color
    new_colors[color].append(name)

# Display the new dictionary
print(new_colors)

# Output:
# {
#     'Red': ['John', 'Peter'],
#     'Blue': ['Mary', 'Tom'],
#     'Green': ['Jane']
# }
