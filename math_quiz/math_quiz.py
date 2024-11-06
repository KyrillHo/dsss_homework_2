import random


def random_from_to(min, max):
    """
    Selects a random integer between two values.
    """
    return random.randint(min, max)


def random_operator():
    """
    Selects a random operator.
    """
    return random.choice(['+', '-', '*'])


def calculate_problem(n1, n2, o):
    """
    Calculates the the math tast given the inputs.
    """
    promblem_str = f"{n1} {o} {n2}" #equation as string
    #depending on operator calulate the equation
    if o == '+': answer = n1 + n2    
    elif o == '-': answer = n1 - n2
    else: answer = n1 * n2

    return promblem_str, answer

def math_quiz():
    score = 0 
    number_of_questions = 3
    

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(number_of_questions):
        n1 = random_from_to(1, 10); n2 = random_from_to(1, 5); o = random_operator()

        PROBLEM, ANSWER = calculate_problem(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        try:
            useranswer = int(useranswer)
        except:
            print("User Input is not valid!")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{number_of_questions}")

if __name__ == "__main__":
    math_quiz()
