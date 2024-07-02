# Making the fruits' list
fruits = {
"Apple":"130",
"Avocado":"50",
"Banana":"110",
"Cantaloupe":"50",
"Grapefruit":"60",
"Grapes":"90",
"Honeydew Melon":"50",
"Kiwifruit":"90",
"Lemon":"15",
"Lime":"20",
"Nectarine":"60",
"Orange":"80",
"Peach":"60",
"Pear":"100",
"Pineapple":"50",
"Plums":"70",
"Strawberries":"50",
"Sweet Cherries":"100",
"Tangerine":"50",
"Watermelon":"80"
}

# implement a program that prompts consumers users to input a fruit (case-insensitively)
fruit_input = input("Item: ").title()

if fruit_input in fruits:
        print("Calories:", fruits[fruit_input])

