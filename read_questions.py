def read_questions_from_file(file_path):
    questions = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        current_question = {}
        for line in lines:
            line = line.strip()
            if line.startswith("Q"):
                if current_question:
                    questions.append(current_question)
                current_question = {"text": "", "choices": []}
                question_parts = line.split(': ', 1)
                if len(question_parts) == 2:
                    current_question["text"] = question_parts[1].strip()
                else:
                    current_question["text"] = line
            else:
                current_question["choices"].append(line)
        if current_question:
            questions.append(current_question)
    return questions
# Example usage:
file_path = '/Users/arslantariq/Desktop/Football_stat_AWS/questions.txt'  # Path to your .txt file
questions = read_questions_from_file(file_path)
for question in questions:
    print(question)
