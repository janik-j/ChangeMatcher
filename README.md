# ChangeMatchers

ChangeMatchers is an AI-powered platform that analyzes ESG/CRSD reports and matches companies with local sustainability opportunities, including research projects, startups, and initiatives.

## Features
- **AI-Powered Analysis**: Utilizes Google's Gemini AI to analyze ESG/CRSD reports
- **Smart Matching**: Automatically matches reports with relevant local opportunities
- **Location-Based**: Filters opportunities by city and industry
- **Detailed Analysis**: Provides match scores, alignment points, potential impact, and implementation timeline
- **User-Friendly Interface**: Built with Streamlit for easy interaction

## Prerequisites
- Python 3.x
- Google AI Studio account with Gemini API access
- Valid Gemini API key (obtain from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Installation
```bash
git clone https://github.com/yourusername/changematchers.git
cd changematchers
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Application
1. Start the Streamlit application:
```bash
streamlit run app.py
```
2. The application will open in your default web browser at `http://localhost:8501`
3. Enter your Gemini API key in the sidebar when prompted

Note: If you're running the application remotely, you can access it using the Network URL provided in the terminal output.

## Usage
1. Enter your Gemini API key in the sidebar
2. Select your city and industry from the sidebar dropdowns
3. Enter the URL of your ESG/CRSD report (PDF format)
4. Click "Find Matching Opportunities"
5. Review the AI-generated matches and analysis

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License.