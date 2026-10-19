# FUNCTIONING
print("Dari HP")
# Sub 3 scoring
def scoring_display(signal):
    pass
    print("SCORING AND SCORES: ")
    print(score_formula)

    for i, question in enumerate(questions, start=1):
        short_question = " ".join(question["question"].split()[:2])
        short_answer = " ".join(question["answer"].split()[:2])

        print(f"{i}. Question: {short_question}...")
        print(f"Answer: {short_answer}...")
        print(f"Score: {score} {score_name}")
        print("-" * 30)

    if signal == 'by_function':
        return
    elif signal == 'by_user':
        choice = input("q if done: ")
        if choice == 'q':
            return
            
def scoring_input():  #
    pass  # Pass
    score_formula = []
    while True:
        print("Scoring formula selection: ")
        print("")
def scoring_edit():
    pass  # Pass

def scoring_delete():
    pass  # Pass

# Sub 3 questions and answers
def questions_display(signal):  # display function
    print("QUESTIONS LIST: ")

    if not questions:
        print(f"There is no questions yet. Please input first.")
        new_questions = questions_input()
        questions.extend(new_questions)

    for i, question in enumerate(questions, start=1):
        print(f"{i}. Question: {question['question']}")
        print(f"Answer: {question['answer']}")
        print("-" * 30)

    if signal == 'by_function':
        return
    elif signal == 'by_user':
        choice = input("q if done: ")
        if choice == 'q':
            return

def questions_input():  # input function
    trial_questions = []

    if not questions:
        questions_number = 1
    else:
        questions_number = len(questions) + 1

    while True:
        question = input(f"Enter the {questions_number}. question (q if done): ")
        if question == "q":
            break

        questions_number += 1
        answer = input("Enter the answer: ")
        print("-" * 30)

        new_question = {
            "question": question,
            "answer": answer
        }
        trial_questions.append(new_question)
    return trial_questions

def questions_edit():
    questions_display('by_function')  # So that user will know how's the question they'd edit

    while True:

        if not questions:  # So that if the questions were still empty, this function can't be used
            new_questions = questions_input()
            questions.extend(new_questions)

        question_number = input("Enter for which question you'd like to edit (q if done): ")

        if question_number.lower() == 'q':
            break
        else:
            question_number = int(question_number)
            question_number -= 1
        print()
        print("-" * 30)
        print(f"Current question: {questions[question_number]['question']}")
        print(f"Current answer: {questions[question_number]['answer']}")
        print("-" * 30)
        print()

        question_select = input("Enter whether you'd like to edit both question and answer or one of them (b/q/a): ")

        if question_select.lower() == 'b':
            edited_question = input("Enter the new question: ")
            edited_answer = input("Enter the new answer: ")

            questions[question_number]['question'] = edited_question
            questions[question_number]['answer'] = edited_answer

        elif question_select.lower() == 'q':
            edited_question = input("Enter the new question: ")
            questions[question_number]['question'] = edited_question

        elif question_select.lower() == 'a':
            edited_answer = input("Enter the new answer: ")
            questions[question_number]['answer'] = edited_answer

def questions_delete():
    questions_display('by_function')

    while True:
        question_number = input("Enter which question you want to delete (q if done): ").strip().lower()
        if question_number == 'q':
            break

        question_number = int(question_number)
        question_number -= 1

        questions.pop(question_number)
        question_number += 1
        print(f"Question number {question_number} has been deleted.")

# Sub 2
def scoring_menu():
    while True:
        print("========================")
        print("=    CUSTOMIZE MENU    =")
        print("========================")
        print("1. Display scores and scoring system.")
        print("2. Input scoring system.")
        print("3. Edit scoring system.")
        print("4. Delete scoring system.")
        print("5. Back to customize menu.")
        print("6. Back to main menu.")

        choice = input("Enter for which menu to open (1-6): ").strip()
        if choice == '1':
            print()
            print("-" * 30)
            scoring_display()

        elif choice == '2':
            print()
            print("-" * 30)
            scoring_input()

        elif choice == '3':
            print()
            print("-" * 30)
            scoring_edit()

        elif choice == '4':
            print()
            print("-" * 30)
            scoring_delete()

        elif choice == '5':
            break
        elif choice == '6':
            return 'back_customize'
        else:
            print("Please input a valid choice.")

def questions_menu():
    while True:
        print("========================")
        print("=    CUSTOMIZE MENU    =")
        print("========================")
        print("1. Display questions and answers.")
        print("2. Input questions and answers.")
        print("3. Edit questions and answers.")
        print("4. Delete questions and answers.")
        print("5. Back to customize menu.")
        print("6. Back to main menu.")

        choice = input("Enter for which menu to open (1-6): ").strip()
        if choice == '1':
            print()
            print("-" * 30)
            questions_display('by_user')

        elif choice == '2':
            print()
            print("-" * 30)
            new_questions = questions_input()
            questions.extend(new_questions)

        elif choice == '3':
            print()
            print("-" * 30)
            questions_edit()

        elif choice == '4':
            print()
            print("-" * 30)
            questions_delete()

        elif choice == '5':
            break
        elif choice == '6':
            return 'back_customize'
        else:
            print("Please input a valid choice.")

# Sub 1
def start_menu():  # Pass
    pass  # Pass
    return 'by_function'

def customize_menu():
    while True:
        print("========================")
        print("=    CUSTOMIZE MENU    =")
        print("========================")
        print("1. Questions and answers.")
        print("2. Scoring system.")
        print("3. Back to main menu")

        choice = input("Enter for which menu to open (1-3) : ").strip()
        if choice == '1':
            print()
            print("-" * 30)
            signal = questions_menu()
            if signal == 'back_customize':
                return 'back_main'

        elif choice == '2':
            print()
            print("-" * 30)
            scoring_menu()

        elif choice == '3':
            break
        else:
            print("Please input a valid choice.")

# Main
def main_program():
    while True:
        print("========================")
        print("=   APPLICATION MENU   =")
        print("========================")
        print("1. Do the Quizzes.")
        print("2. Customize.")
        print("3. Exit.")
        print("----------")

        choice = input("Select menu (1/2/3/4): ")
        if choice == '1':
            print()
            print("-" * 30)
            signal = start_menu()
            if signal == 'back_main':
                continue

        elif choice == '2':
            print()
            print("-" * 30)
            signal = customize_menu()
            if signal == 'back_main':
                continue

        elif choice == '3':
            print()
            print("-" * 30)
            print("Thank you for using our application!")
            break

        else:
            print("Please enter a valid choice.")

# MAIN PROGRAM
questions = []  # Set the global list
main_program()  # The whole thing btw