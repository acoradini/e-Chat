# e-Chat Streamlit

## Overview
e-Chat is a Streamlit application that serves as an interactive chatbot. It allows users to ask questions and receive responses based on content loaded from websites or PDF documents. The chatbot utilizes the Langchain library for natural language processing and response generation.

## Project Structure
```
e-chat-streamlit
├── src
│   ├── streamlit_app.py       # Main entry point for the Streamlit application
│   ├── chatbot.py              # Contains chatbot logic and response generation
│   ├── loaders.py              # Responsible for loading documents from various sources
│   └── utils.py                # Utility functions to support the application
├── .streamlit
│   └── config.toml             # Configuration settings for the Streamlit app
├── requirements.txt            # Lists dependencies required for the project
├── .gitignore                  # Specifies files to be ignored by Git
└── README.md                   # Documentation for the project
```

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd e-chat-streamlit
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the Streamlit application, execute the following command in your terminal:
```
streamlit run src/streamlit_app.py
```

Once the application is running, you can interact with the chatbot by entering your questions. The chatbot will provide responses based on the content loaded from the specified sources.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.