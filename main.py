import os
from fastapi import FastAPI, File, UploadFile, Form
from PyPDF2 import PdfReader
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.output_parsers import StrOutputParser
from langdetect import detect

app = FastAPI()
os.environ["MISTRAL_API_KEY"] = "zVndWQkVst3KivKwIivW6TgCg1384KLA"
output_parser = StrOutputParser()

def detect_language(text):
    try:
        return detect(text)  # Returns language code (e.g., 'fr' for French)
    except:
        return "unknown"

@app.post("/generate-questions")
async def generate_questions(
    file: UploadFile = File(...),
    question_types: str = Form(...),
    difficulty_level: str = Form(...),
    num_questions: int = Form(...),  # Ensure that num_questions is provided
):
    try:
        # Validate num_questions
        if  num_questions <= 0:
            return {"error": "The number of questions must be greater than 0."}

        # Read PDF
        reader = PdfReader(file.file)
        input_text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        language = detect_language(input_text)

        # Define question types
        selected_types = question_types.split(",")
        instructions = {
            "MCQ": "Generate"+ str(num_questions)+"multiple-choice questions from the input and provide response in the language of the document.",
            "Question-Réponse": "Generate"+ str(num_questions)+ "open-ended questions from the input and provide response in the language of the document.",
            "Oui/Non": "Generate" +str(num_questions)+"yes/no questions from the input and provide response in the language of the document."
        }

        instructions_french = {
            "MCQ": "Générez " +str(num_questions)+"questions à choix multiples à partir de l'entrée et fournissez la réponse dans la langue du document.",
            "Question-Réponse": "Générez"+ str(num_questions)+"questions réponse à partir de l'entrée et fournissez la réponse dans la langue du document.",
            "Oui/Non": "Générez" +str(num_questions)+"questions Oui/Non à partir de l'entrée et fournissez la réponse dans la langue du document."
        }

        difficulty_instructions = {
            "Facile": "Generate"+ str(num_questions)+"simple questions with basic understanding.",
            "Moyenne": "Generate" +str(num_questions)+"questions with intermediate difficulty.",
            "Difficile": "Generate "+str(num_questions)+"complex questions requiring advanced understanding."
        }

        # Combine instructions based on language and question type
        if language == "fr":
            combined_instruction="Répondez en français."
            combined_instruction += " ".join([instructions_french[t] for t in selected_types if t in instructions_french])
            combined_instruction += f" {difficulty_instructions.get(difficulty_level, '')} "
            combined_instruction+="chaque question doit avoir sa réponse"
            combined_instruction+="  Répondez en français."
        else:
            combined_instruction = " ".join([instructions[t] for t in selected_types if t in instructions])
            combined_instruction += f" {difficulty_instructions.get(difficulty_level, '')}"
            combined_instruction+= "every question must have its response"

        # Add instruction for number of questions
       # combined_instruction += f" Please generate exactly {num_questions} questions."

        # Create the prompt
        prompt = ChatPromptTemplate.from_messages([
            ("system", combined_instruction),
            ("user", "{input_text}")
        ])

        # Initialize the Mistral model
        llm = ChatMistralAI(model="mistral-small")
        chain = prompt | llm | output_parser
        questions = chain.invoke({"input_text": input_text})

        # Format the output (assuming the response is a list of questions in string format)
        formatted_questions = [q.strip() for q in questions.split("\n") if q.strip()]

        # Return only the required number of questions
        return {"questions": formatted_questions}

    except Exception as e:
        return {"error": str(e)}
