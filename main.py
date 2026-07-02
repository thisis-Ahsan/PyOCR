import os
from google import genai
from PIL import Image

def extract_invoice_with_vision(image_path, output_md_path="formatted_text_output.md"):
    print("🔄 Initializing Pure-Python Vision Engine...")
    
    # Retrieve API key safely
    api_key = os.environ.get("GEMINI_API_KEY")

    # Initialize client using standard cloud protocols (no local DLL execution)
    client = genai.Client(api_key=api_key)
    
    try:
        print(f"📸 Opening document image: {image_path}")
        image = Image.open(image_path)
        
        # Craft a precise prompt instructing the engine to preserve structural asymmetry
        prompt = (
            "Perform OCR on this invoice image. You must return perfectly formatted Markdown text. "
            "1. Identify the line-item table and format it into a clean Markdown table. "
            "2. Preserve top and bottom metadata (like invoice numbers, dates, billing addresses, totals) "
            "as clean, bolded key-value rows or lists. Do not force them into tables. "
            "3. Keep section headers accurate. Maintain the natural layout flow of the document."
        )
        
        print("⚡ Sending to Layout Analysis Engine (gemini-2.5-flash)...")
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[image, prompt]
        )
        
        markdown_text = response.text
        
        # Save output safely
        with open(output_md_path, "w", encoding="utf-8") as f:
            f.write(markdown_text)
            
        print(f"\n🎉 Success! Visually perfect structured layout saved to: {output_md_path}")
        return markdown_text

    except Exception as e:
        print(f"❌ Extraction error: {e}")
        return None

if __name__ == "__main__":
    invoice_image = "image.png" 
    
    if os.path.exists(invoice_image):
        formatted_md = extract_invoice_with_vision(invoice_image)
        if formatted_md:
            print("\n--- Structural Markdown Preview ---")
            print(formatted_md[:800])
    else:
        print(f"❌ Error: Please place your invoice image at '{invoice_image}'")