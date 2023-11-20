from datasets import load_dataset
import pickle
import re
import requests
import pdfplumber
def clean_text(var_in):

    example_str_clean = re.sub(
        "[^A-Za-z']+", " ", var_in).strip()
    return example_str_clean
def remove_numbers(text):
    return re.sub(r'\d+', '', text)
def replace_newline(text):
    text_with_newline = text.replace("\\n", "\n")
    return text_with_newline
dataset_scotus_filings = load_dataset("pile-of-law/pile-of-law", 'scotus_filings')
print(type(dataset_scotus_filings))
print(dataset_scotus_filings['train'])
ds_val_scotus_fillings = dataset_scotus_filings['train']

def extract_ToC_from_pdf_url(pdf_url):
    response = requests.get(pdf_url)
    print(type(response))
    with open('content.pdf', 'wb') as f:
        f.write(response.content)
    with pdfplumber.open('content.pdf') as pdf:
        ToC_text = ""
        ToC_boolean = False
        for page in pdf.pages:
            text = page.extract_text()
            if "TABLE OF CONTENTS" in text:
                if "Conclusion" not in text:
                    ToC_boolean = True
                    # Adjust this section to find the specific content
                    ToC_index = text.index("TABLE OF CONTENTS")
                    ToC_text += '\n' + text[ToC_index:]
                    continue
                    # break
            if "Conclusion" in text:
                Conclusion_index = text.index("Conclusion")
                ToC_text += '\n' + text[:Conclusion_index]
                break

            if ToC_boolean:
                ToC_text += text
    ToC_text = remove_numbers(ToC_text)
    return ToC_text

def extract_conclusion_from_pdf_url(pdf_url):
    response = requests.get(pdf_url)
    print(type(response))
    with open('content.pdf', 'wb') as f:
        f.write(response.content)
    with pdfplumber.open('content.pdf') as pdf:
        conclusion_text = ""
        conclusion_boolean = False
        for page in pdf.pages:
            text = page.extract_text()
            if "CONCLUSION" in text:
                if "Respectfully submitted," not in text:
                    conclusion_boolean = True
                    # Adjust this section to find the specific content
                    conclusion_index = text.index("CONCLUSION")
                    conclusion_text += '\n' + text[conclusion_index:]
                    continue
            # if "APPENDIX" in text:
            #     break
            if "APPENDIX" in text:
                appendix_index = text.index("APPENDIX")
                conclusion_text += '\n' + text[:appendix_index]
                break
            if "Respectfully submitted," in text:
                submitted_index = text.index("Respectfully submitted,")
                conclusion_text += text[:submitted_index]
                break

            if conclusion_boolean:
                conclusion_text += text
    # conclusion_text = remove_numbers(conclusion_text)
    return conclusion_text
