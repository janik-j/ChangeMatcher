# ChangeMatchers

ChangeMatchers is an AI-powered platform that analyzes ESG/CRSD reports and matches companies with local sustainability opportunities, including research projects, startups, and initiatives.


## Prerequisites
- Python 3.x
- Google AI Studio account with Gemini API access
- Valid Gemini API key (obtain from [Google AI Studio](https://makersuite.google.com/app/apikey))


## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/janik-j/ChangeMatcher.git
    cd changematchers
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application
1. **Launch Streamlit**
    ```bash
    streamlit run app.py
    ```

2. **Access the Application**
    - The app will automatically open in your default web browser at [http://localhost:8501](http://localhost:8501).
    - If running remotely, use the Network URL provided in the terminal output to access the application.

3. **Configure API Key**
    - Enter your Gemini API key in the sidebar when prompted to enable report analysis.

4. **Click "Find Matching Opportunities"**
5. **Review the AI-generated matches and analysis**


## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.


## License
This project is licensed under the MIT License.