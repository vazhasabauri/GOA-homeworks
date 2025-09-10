ords = ["moon", "sun", "light", "astronaut", "computer", "library"]
unique_words = {w for w in words if w not in ["moon", "sun"]}
print("all words:", words)
print("unique words:", unique_words)