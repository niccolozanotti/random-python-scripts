import emoji

def replace_emoji_with_description(text):
    # Define a dictionary for custom replacements
    custom_replacements = {
        "🌼": "margherita",
        "😈": "diavola",
        "🥔": "patatine",
        "🍄‍🟫": "funghi",
        "🍄": "funghi",
        "🍖": "prosciutto crudo",
        "❌": "senza"
    }
    
    # Convert each emoji in text to its description or custom replacement
    for char in text:
        if char in emoji.EMOJI_DATA:
            # Check if there's a custom replacement for the emoji
            if char in custom_replacements:
                description = custom_replacements[char]
            else:
                # Use the default emoji description if no custom replacement is found
                description = emoji.demojize(char, delimiters=("", ""))
                description = description.replace("_", " ")

            # Replace the emoji with the chosen description
            text = text.replace(char, description)
    
    return text

# Example usage
def get_user_input():
    inputs = []
    print("Enter your pizzas with emoji string. Press Ctrl+C to finish.\n")
    
    try:
        while True:
            user_input = input("Enter a string: ")
            inputs.append(user_input)
    except KeyboardInterrupt:
        print("\nInput stopped by user.")
        return inputs

pizzas_with_emojis = get_user_input()
    # ["😈 x2","🌼 x 3","🥔fritta x2","Porcini 🍄‍🟫", "🍖🍄‍🟫x4","🌼 🌾❌","🥔 e salsiccia x5","Patate e salsiccia bianca"]
pizzas_plain = []

for pizza in pizzas_with_emojis:
    plain_pizza = replace_emoji_with_description(pizza)
    pizzas_plain.append(plain_pizza)
    print(plain_pizza)
