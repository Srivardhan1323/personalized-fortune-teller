# fortune.py

import random

def get_fortune(mood):
    # List of fortunes based on user's mood
    fortunes = {
        "happy": [
            "Keep smiling, good vibes are contagious!",
            "Joy is your natural state—embrace it.",
            "You're shining today, SriVardhan! Stay happy!"
        ],
        "sad": [
            "Tough times never last, but tough people do.",
            "The sun will shine again—hang in there.",
            "It's okay to feel down. Better days are coming."
        ],
        "neutral": [
            "Balance is good. Something exciting is coming!",
            "A small surprise will brighten your day.",
            "Stay open to possibilities—you never know!"
        ]
    }

    # If mood doesn't match, give a default message
    default_fortunes = [
        "Hmm... mood unclear. But good things are ahead!",
        "Life has a funny way of surprising you.",
        "No matter what, you've got this!"
    ]

    return random.choice(fortunes.get(mood.lower(), default_fortunes))

def main():
    # Personal details
    full_name = "SriVardhan"
    admission_number = "21JE0517"

    # Welcome message
    print("🔮 Welcome to Your Personalized Fortune Teller 🔮")
    print(f"Presented by: {full_name} (Admission No: {admission_number})")
    print("-" * 60)

    # Get mood input
    mood = input("How are you feeling today? (happy/sad/neutral): ")

    # Show fortune
    fortune = get_fortune(mood)
    print("\n✨ Your Fortune:")
    print(fortune)

if __name__ == "__main__":
    main()
