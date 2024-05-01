# Voice Recognition / Summary

## The site is at: https://vrfrontend.web.app/

**Client Side (Frontend)**:
* The client side is primarily being created by bootstrapping with create-react-app (CRA) along side with tailwind modern css styling for ease of style selection.

**Server Side (Backend)**:
* The backend consists of two portions:
    * Backend py file (transcribe.py):
        * This is the main file that perform all the needed feature of the app including Voice Recognition (Supported by openai-whisper model) and summarize (Supported by openai's Chatgpt3.5-turbo model)
* Endpoint Flask App (app.py):
    * This is the home for all functions (def from transcribe.py) endpoint creation (to be used through http requests)
    * Note that the first default endpoint is just for testing purposes only (to test if the endpoint creation actually work!)
    * The endpoint creation is being hosted by Google Cloud (gcloud)

**NOTE**: for reusing this project code files, for openai-api-key, make sure to create your own api key for the chatgpt3.5 turbo and put them as an environment variables in your own .env file on your repository.