import pypdf
import pyttsx3

def convert_pdf_to_speech(pdf_path, output_audio_path):
    # 1. Initialize the offline TTS synthesis engine
    engine = pyttsx3.init()
    
    # Optional: Configure voice profile analytics properties
    engine.setProperty('rate', 160)  # Speaking pace speed metrics
    
    extracted_text = ""
    
    # 2. Extract text data segments from target PDF document
    with open(pdf_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        print(f"🔄 Processing document... Found {len(reader.pages)} pages to scan.")
        
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            if text:
                extracted_text += text + " "
                
    # 3. Stream data output matrix into a synthesized audio file
    if extracted_text.strip():
        print("🔊 Text conversion validated. Rendering audio array...")
        engine.save_to_file(extracted_text, output_audio_path)
        engine.runAndWait()
        print(f"🏆 Audiobook generated successfully: '{output_audio_path}'")
    else:
        print("⚠️ Processing Error: No structural characters could be extracted.")

if __name__ == "__main__":
    # Make sure to run 'pip install pypdf pyttsx3' in your terminal first!
    convert_pdf_to_speech("sample.pdf", "audiobook.mp3")
