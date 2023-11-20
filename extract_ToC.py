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
                ToC_boolean = True
                # Adjust this section to find the specific content
                ToC_index = text.index("TABLE OF CONTENTS")
                ToC_text += '\n' + text[ToC_index:]
                if "Conclusion" in text or 'CONCLUSION':
                    break
                else:
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

# Replace 'your_pdf_url' with the actual URL of the PDF file
pdf_url = 'https://www.supremecourt.gov/DocketPDF/21/21-84/188174/20210820154938094_2021.08.20%20MSLF%20Amicus%20In%20Support%20of%20FIRE%20Petition.pdf'
conclusion = extract_ToC_from_pdf_url(pdf_url)
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
