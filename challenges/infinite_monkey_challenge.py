import random

sentence = "generate me right now"
alphabet = "abcdefghijklmnopqrstuvwxyz "
n = len(sentence)
print(sentence)
print(n)


def generator():
    generated = random.choices(alphabet, k=n)
    generated_sentence = ''.join(generated)
    return generated_sentence


def compare(goal, string):
    same_chars = 0
    for i in range(len(goal)):
        if goal[i] == string[i]:
            same_chars = same_chars + 1
    return same_chars / len(goal)


def call():
    print("I'm running.\nPlease wait.")
    new_string = generator()
    # The lower 'best' number, the more results will be displayed
    best = 0
    new_score = compare(sentence, new_string)

    while new_score < 1:
        if new_score >= best:
            print(f"Sentence match >> {new_score * 100} || {new_string}")
            best = new_score
        new_string = generator()
        new_score = compare(sentence, new_string)
    print(f"Sentence match >> {new_score * 100} || {new_string}")


call()
