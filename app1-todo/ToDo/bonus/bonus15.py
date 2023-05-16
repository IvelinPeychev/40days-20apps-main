import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question)
    print(question["question_text"])
    for index, alternatives in enumerate(question['alternatives']):
        print(index+1, "-", alternatives)
    user_answer = int(input("Enter your answer: "))
    question['user_answer'] = user_answer
    if question['user_answer'] == question['correct_answer']:
        score += 1
    print(f'The correct answer for " {question["question_text"]} " is {question["correct_answer"]}.'\
           f' You choose {question["user_answer"]}. Your score is {score}.')


print(score, " / ",  len(data))
