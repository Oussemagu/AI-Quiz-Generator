# AI Quiz Generator (Twise Challenge)

This project was developed for the Twise challenge and creates an interactive web application that generates relevant questions from PDF documents.  It features a user-friendly interface for uploading PDFs, extracting text, and generating diverse question formats (MCQ, Yes/No, Short Answer) using the Mistral AI model.

## Features

*   **PDF Upload:** Easily upload PDF files through a dedicated interface element.
*   **Text Extraction:** Extracts the textual content from uploaded PDFs for analysis by the AI model.
*   **Question Generation:** Leverages the Mistral AI model to generate a variety of relevant questions (Multiple Choice, Yes/No, Short Answer) based on the PDF content.
*   **Interactive User Interface:** Presents generated questions in a clear and intuitive user interface, enhancing the user experience.
*   **FastAPI Backend:** Employs a FastAPI backend to efficiently handle requests and interact with the AI model.
*   **Streamlit Frontend:**  Utilizes Streamlit to create an interactive and user-friendly web interface.
*   **Difficulty Levels:**  Allows users to select the difficulty level of the generated questions (e.g., Easy, Medium, Hard).
*   **Answer Generation:**  Generates answers for the questions along with the questions themselves.

## Technologies Used

*   Python
*   FastAPI
*   Streamlit
*   Mistral AI
*   PyPDF2
*   Langchain
*   Langdetect
*   Uvicorn (for running the FastAPI backend)
*   Docker & Docker Compose (for easy deployment)


## Installation

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/Oussemagu/AI-Quiz-Generator.git](https://github.com/Oussemagu/AI-Quiz-Generator.git)
    cd AI-Quiz-Generator
    ```

2.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    pip install -r requirements_streamlit.txt
    ```

3.  **Set up Environment Variables:**

    Create a `.env` file in the root directory of the project and add your Mistral API key:

    ```
    MISTRAL_API_KEY=your_actual_mistral_api_key
    ```

4.  **Run the Application using Docker Compose (Recommended):**

    ```bash
    docker-compose up -d
    ```

    This will build the Docker images and start the containers in detached mode.

5.  **Access the Application:**

    Open your web browser and go to `http://localhost:8501`.

6.  **Run the Application Manually (Alternative):**

    **(Only use this if you're not using Docker)**
    ```bash
    uvicorn main:app --reload  # Start the FastAPI backend
    streamlit run app.py      # Start the Streamlit frontend in a separate terminal
    ```

## Usage

1.  Upload a PDF file using the file upload component on the Streamlit web interface.
2.  Select the desired question types (MCQ, Yes/No, Short Answer). 
3.  Choose the difficulty level.
4.  Click the "Generate Questions" button.
5.  The generated questions will be displayed in the interface.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any bug fixes, feature requests, or improvements.

