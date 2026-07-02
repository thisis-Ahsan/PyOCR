# PyOCR
PyOCR is an OCR tool that extracts text content from a given image and writes down the extracted text in a markdown file in a formatted way.

This tool uses Gemini Flash 2.5 (through `google-genai` library) and `pillow` to do it's job.

## Installation and Usage Guide
**Step 1: Clone this repo**  
`git clone https://github.com/thisis-Ahsan/PyOCR`

**Step 2: Install the required dependencies**  
`pip install -r requirements.txt`

**Step 3: Set your Gemini API key in environment variables**  
For Windows (Command Prompt): `set GEMINI_API_KEY=your_actual_key_here`  
For Windows (Powershell): `$env:GEMINI_API_KEY="your_actual_key_here"`  
For Mac/Linux: `export GEMINI_API_KEY="your_actual_key_here"`

**Step 4: Put your input image in the root folder and rename it to image.png**  
Your folder structure should be like this:
```
PyOCR
   |
   |— main.py
   |— requirements.txt
   |— README.md
   |— .gitignore
   |— image.png
```

**Step 5: Run the script**  
Run the script and you'll find your text output in `formatted_text_output.md`

I hope you'll like this tool ;)  

Follow me for more. And don't forget to follow me on Instagram (https://instagram.com/thisis_ahsan) and youtube (https://youtube.com/@thisis_ahsan)
