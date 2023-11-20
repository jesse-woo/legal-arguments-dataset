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

                conclusion_boolean = True
                # Adjust this section to find the specific content
                conclusion_index = text.index("CONCLUSION")
                conclusion_text += '\n' + text[conclusion_index:]
                if "Respectfully submitted," not in text:
                    break
                else:
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

# Replace 'your_pdf_url' with the actual URL of the PDF file
pdf_url = 'https://www.supremecourt.gov/DocketPDF/21/21-12/186854/20210805165140416_41247%20pdf%20Daugherty.pdf'
conclusion = extract_conclusion_from_pdf_url(pdf_url)
print(conclusion)


# with open('single_brief_list.pkl', 'rb') as f:
#     list_of_briefs = pickle.load(f)

# for brief in list_of_briefs:


    # clean_brief = clean_text(brief)
    # print(clean_brief)
    # strip_brief = replace_newline(brief)
    # for idx, word in enumerate(strip_brief.split()):
    #    # if 'CONCLUSION' in word:
    #         print(word)
