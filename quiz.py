import os
import google.generativeai as genai
import pandas as pd

def generate_quiz_csv(default_quiz=None):
    genai.configure(api_key="AIzaSyA_RLVbfjgikc6OfOZiOByOHLnnBtqnX8M") 

    def get_gemini_response(input_text, prompt):
        model = genai.GenerativeModel('gemini-1.0-pro')
        response = model.generate_content([input_text, prompt])
        return response.text

    def get_gemini_responses():
        try:
            quiz_topic = input('Enter quiz topic: ') 
            input_prompt1 = """
            You are an experienced educator with expertise in various technical domains such as data science, full-stack development, big data engineering, DevOps, and data analysis. Your role involves creating a quiz focused on a specific tech stack, programming language, or any other technical subject. Your task is to generate a list of 10 dictionaries, each containing question_number, question, options, correct_answer, and explanation. These questions should be tailored to the given tech stack or subject matter.

            Here's an example of how the questions should be structured:

            quiz_questions = [
                {
                    "question_number": 1,
                    "question": "Which country won the FIFA World Cup in 2018?",
                    "options": ["Germany", "Argentina", "France", "Brazil"],
                    "correct_answer": "France",
                    "explanation": "France won the FIFA World Cup in 2018 by defeating Croatia in the final."
                },
                ...
            ]

            Ensure that the questions are formatted neatly and adhere to standard punctuation rules, using only commas, periods, question marks, and colons where necessary.

            Important: Ensure that the list formed is named "quiz_questions" to maintain consistency.
            Also, ensure that the questions are of a challenging level to provide a valuable learning experience.

            Please note that the sign ``` should not be included in the response.
            """
            response1 = get_gemini_response(quiz_topic, input_prompt1)

            print("Response 1:")
            print(response1)

            return response1.strip()
        except Exception as e:
            print(f"An error occurred: {e}")
            return default_quiz

    response_text = get_gemini_responses()

    # Remove the "quiz_questions =" part
    response_text = response_text.replace("quiz_questions =", "")
    if "```" in response_text:
        response_text = response_text.replace('```', '')

    try:
        quiz_questions = eval(response_text)
    except Exception as e:
        print(f"Failed to parse quiz questions. Using default. Error: {e}")
        quiz_questions = default_quiz

    data = []
    for question in quiz_questions:
        question_data = {
            "question_number": question["question_number"],
            "question": question["question"],
            "option1": question["options"][0],
            "option2": question["options"][1],
            "option3": question["options"][2],
            "option4": question["options"][3],
            "correct_answer": question["correct_answer"],
            "explanation": question["explanation"]
        }
        data.append(question_data)

    df = pd.DataFrame(data)

    if os.path.exists('quiz_questions.csv'):
        os.remove('quiz_questions.csv')

    df.to_csv('quiz_questions.csv', index=False)

    print("New CSV file created successfully.")

if __name__ == "__main__":
    default_quiz = [
        {
            "question_number": 1,
            "question": "What does HTML stand for?",
            "options": ["Hypertext Markup Language", "Hyperlink and Text Markup Language", "Home Tool Markup Language", "Hyper Text Most Language"],
            "correct_answer": "Hypertext Markup Language",
            "explanation": "HTML stands for Hypertext Markup Language."
        },
        {
            "question_number": 2,
            "question": "Which programming language is known for its use in artificial intelligence and machine learning?",
            "options": ["Java", "Python", "C++", "JavaScript"],
            "correct_answer": "Python",
            "explanation": "Python is known for its extensive use in artificial intelligence and machine learning."
        },
        {
            "question_number": 3,
            "question": "What does CPU stand for?",
            "options": ["Central Processing Unit", "Computer Processing Unit", "Core Processing Unit", "Central Program Unit"],
            "correct_answer": "Central Processing Unit",
            "explanation": "CPU stands for Central Processing Unit, which is the primary component of a computer that performs instructions."
        },
        {
            "question_number": 4,
            "question": "What is the main function of a firewall?",
            "options": ["To protect against viruses", "To prevent unauthorized access", "To increase internet speed", "To store data"],
            "correct_answer": "To prevent unauthorized access",
            "explanation": "The main function of a firewall is to prevent unauthorized access to or from a private network."
        },
        {
            "question_number": 5,
            "question": "What does IoT stand for?",
            "options": ["Internet of Things", "Internet of Technology", "Input Output Transfer", "Innovations of Technology"],
            "correct_answer": "Internet of Things",
            "explanation": "IoT stands for Internet of Things, which refers to the interconnection of everyday objects via the internet."
        }
    ]

    generate_quiz_csv(default_quiz=default_quiz)
