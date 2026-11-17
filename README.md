# aixcelerate-mood-guesser
A simple Python project that predicts whether a sentence expresses a Happy or Sad mood using clue words.

# Mood Guesser

## Level 3: Testing

Accuracy on the 5 practice sentences: 80%

### 1. Which sentence went wrong, and why?

The sentence "Today was a great day" was predicted as Sad instead of Happy. This happened because the word "great" was not included in my happy_words list. So the program did not find any Happy clue word and predicted Sad.

### 2. One change that would make my program better:

I can add more useful positive and negative clue words to improve the accuracy of my program.

## Learning Questions

### 1. Total score of "good party today" and its mood:

good = +2
party = +1
today = 0

Total score = +3

The mood is Happy because the total score is positive.

### 2. Total score of "bad exam day" and its mood:

bad = -2
exam = 0
day = -1

Total score = -3

The mood is Sad because the total score is negative.

### 3. Why did "exam" get a score of 0, and is that good or bad?

The word "exam" appears once in Happy sentences and once in Sad sentences. So both scores cancel each other and the final score becomes 0. This is useful because the word does not favour either mood.

### 4. Why is "not good" labelled Happy, and how could it be fixed?

The word "good" has a positive score of +2. The program does not understand the meaning of "not". So it labels the sentence as Happy. This can be fixed by adding negation detection to the program.

## AI Declaration

I used an AI tool: Yes

If yes, what I asked it:

I used ChatGPT to understand Python concepts, write and check my program, correct errors, create the Python file and learn how to upload my project to GitHub.

## Reflection

What was hardest, and what I learned that I did not know before:

The hardest part was understanding how to write functions and use loops and conditions. I learned how to work with Python lists, functions, loops and strings. I also learned how to test a program, calculate accuracy and upload a Python project to GitHub.
