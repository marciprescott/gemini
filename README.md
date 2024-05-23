Installation

Prerequisites:

Ensure you have Python 3.11.5 installed on your system. You can check by running python --version or python3 --version in your terminal.
Additional dependencies might be required. These will be listed in a file called requirements.txt. Install them using 
pip install -r requirements.txt.

Clone the Repository:

Open your terminal and navigate to the directory where you want to clone the project.

Use the git clone command followed by the URL of your GitHub repository:

Bash
git clone https://github.com/marciprescott/gemini.git


Configuration

Important:

Security: Never store your Google API key directly in the code or the README file. It's a security risk!
Obtain Google API Key:

Create a project on Google Cloud Platform (GCP): https://console.cloud.google.com/.
Enable the Google AI Platform APIs (specifically the GenerativeAI API) for your project.
Create an API key in your GCP project for authentication.
Set Environment Variable:

There are two main approaches to set the API key securely:
Environment variables: This is the  RECOMMENDED APPROACH. Store the API key in an environment variable named GOOGLE_API_KEY. You can set environment variables differently depending on your operating system:

Linux/macOS:
Bash
export GOOGLE_API_KEY=your_api_key


Replace your_api_key with your actual API key. You can also set environment variables permanently in your shell configuration files (e.g., .bashrc or .zshrc).
Windows:
Search for "environment variables" in the Start menu and edit system environment variables.
Create a new system variable named GOOGLE_API_KEY and set its value to your API key.
Configuration File (Optional):  If environment variables are not feasible, consider creating a separate configuration file (e.g., config.py) to store your API key. However, this approach exposes the key within your codebase, so exercise caution.

USAGE

Navigate to Project Directory:

Open your terminal and navigate to the directory where you cloned the project using cd:

Bash
cd <your-repo-name>


Replace <your-repo-name> with the actual name of the directory containing the project files.

Run the Script:

Locate the gemini.py script that interacts directly with BARD.

Run the script using the Python command:

Bash
python gemini.py

The script will take user input and generate content using Bard's API.
There is  also a skincare quiz under survey.py if you are curious as to your skin type and concerns, feel free to run survey.py!
I am adding integration with claude and will eventually have one with GhatGPT as well.  

