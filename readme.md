# Voice Recognition / Summary

## The site is at: [https://vrfrontend.web.app/](https://vrfrontend.web.app/)

## Table of Contents
- [Features](#features)
- [Client Side (Frontend)](#client-side-frontend)
- [Server Side (Backend)](#server-side-backend)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Features
- Voice Recognition using OpenAI Whisper model
- Summary generation using OpenAI's ChatGPT 3.5 Turbo model

## Client Side (Frontend)
The client side is primarily being created by bootstrapping with create-react-app (CRA) along with Tailwind CSS for ease of style selection.

## Server Side (Backend)
The backend consists of two portions:
- **Backend py file (`transcribe.py`)**:
  - This is the main file that performs all the needed features of the app including Voice Recognition (supported by OpenAI Whisper model) and summary generation (supported by OpenAI's ChatGPT 3.5 Turbo model).
- **Endpoint Flask App (`app.py`)**:
  - This is the home for all functions (defined in `transcribe.py`) and endpoint creation (to be used through HTTP requests).
  - The first default endpoint is just for testing purposes (to test if the endpoint creation actually works!).
  - The endpoint creation is hosted by Google Cloud (gcloud).

**NOTE**: For reusing this project's code files, ensure you create your own API key for ChatGPT 3.5 Turbo and set it as an environment variable in your own `.env` file in your repository.

## Installation

### Prerequisites
- Node.js
- npm (Node Package Manager)
- Python
- Flask
- OpenAI API key

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/andrewchou949/voiceRecognition.git
    cd voiceRecognition
    ```
2. Install the frontend dependencies:
    ```bash
    cd Client
    npm install
    ```
3. Install the backend dependencies:
    ```bash
    cd Server
    pip install -r requirements.txt
    ```
4. Set up your environment variables:
   - Create a `.env` file in the `Server` directory and add your OpenAI API key:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     ```

## Usage
1. Start the backend server:
    ```bash
    cd Server
    flask run
    ```
2. Start the frontend server:
    ```bash
    cd Client
    npm start
    ```

## Project Structure
```plaintext
voiceRecognition
├── .DS_Store
├── .gitignore                    # Git ignore file
├── Client                        # Directory for the frontend code
│   └── ...                       # Frontend files
├── Server                        # Directory for the backend code
│   ├── transcribe.py             # Main backend file for features
│   ├── app.py                    # Flask app for endpoint creation
│   └── ...                       # Other backend files
├── readme.md                     # Project readme
```

### Components
- **Client/**: Contains the frontend React application.
- **Server/**: Contains the backend Flask application.
- **transcribe.py**: The main file for voice recognition and summary features.
- **app.py**: The entry point for the backend server.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.