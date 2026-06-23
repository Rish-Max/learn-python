emoji_dict = {
    "happy": "😊",
    "sad": "😢",
    "angry": "😠",
    "surprised": "😲",
    "confused": "😕",
    "love": "❤️",
    "heart": "💖",
    "star": "⭐",
    "moon": "🌙",
    "sun": "🌞",
}

def generate_emoji(text):
    for emoji in emoji_dict:
        if emoji in text:
            return emoji_dict[emoji]
    return text

def main():
    text = input("Enter the text to generate emoji: ")
    emoji = generate_emoji(text)
    print(emoji)

main()