
%%writefile main.py

train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad")
]


# Level 1: Count the moods

def count_moods(data):
    happy_count = 0
    sad_count = 0

    for sentence, mood in data:
        if mood == "Happy":
            happy_count += 1
        elif mood == "Sad":
            sad_count += 1

    return (happy_count, sad_count)


# Level 2: Clue words

happy_words = [
    "won", "full", "excited", "surprise", "tasty",
    "selected", "learned", "favourite", "party"
]

sad_words = [
    "lost", "failed", "lonely", "upset", "cancelled",
    "missed", "stopped", "moving", "rained"
]


def guess_mood(sentence):

    sentence = sentence.lower()

    clean_sentence = ""

    for char in sentence:
        if char.isalnum() or char.isspace():
            clean_sentence += char

    words = clean_sentence.split()

    happy_count = 0
    sad_count = 0

    for word in happy_words:
        if word in words:
            happy_count += 1

    for word in sad_words:
        if word in words:
            sad_count += 1

    if happy_count > sad_count:
        return "Happy"
    else:
        # Tie: Choose Sad because no clear Happy clue is found.
        return "Sad"


# Level 3: Test the program

practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy")
]


print("Mood Count:", count_moods(train_data))

correct = 0

for sentence, actual_mood in practice_data:

    predicted_mood = guess_mood(sentence)

    print("Sentence:", sentence)
    print("Actual:", actual_mood)
    print("Predicted:", predicted_mood)
    print()

    if predicted_mood == actual_mood:
        correct += 1

accuracy = (correct / len(practice_data)) * 100

print("Correct Answers:", correct)
print("Total Questions:", len(practice_data))
print("Accuracy:", accuracy, "%")
