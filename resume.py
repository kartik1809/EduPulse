import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import io
import base64

def run_ats_tracking_system():
    genai.configure(api_key="AIzaSyC9WYRBFUfhbjZnmdWRsf_Y7rBea--l6Ms")
    
    def get_gemini_response(input, pdf_content, prompt):
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content([input, pdf_content[0], prompt])
        return response.text

    def input_pdf_setup(file_path):
        with open(file_path, "rb") as file:
            images = pdf2image.convert_from_bytes(file.read())
        first_page = images[0]
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='jpeg')
        img_byte_arr = img_byte_arr.getvalue()
        pdf_parts = [{
            'mime_type': "image/jpeg",
            'data': base64.b64encode(img_byte_arr).decode()
        }]
        return pdf_parts

    input_text = input("Tell me about the job description:- ")
    file_path = input("Enter the path to the PDF file(for eg. Sample.pdf): ")
    if os.path.exists(file_path):
        
        input_prompt1 = """
         You are an experienced HR with tech experience in the field of data science, full stack development, 
         Big data engineering, DEVOPS, Data Analyst, your task is to review the provided resume against the job description for 
         these profile. 
         Find out both the skills hard skills and soft skills from resume and give a table consisting serial number,
           and the main hard skills like languages, tech skills and soft skills like communication skills, leadership etc.
           the table should have 3 columns- serial number, hard skill, soft skill.
        """
        input_prompt2 = """
        You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science, full stack development, 
         Big data engineering, DEVOPS, Data Analyst, and deep ATS functionality, 
        your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
        the job description. First the output should come as percentage, the percentage 
         should be the most accurate one and genuine and then next line contains the last final thoughts.
         If it matches really then the percentage should be greater than 80.
        """
        submit1 = input("Do you want to know about the resume? (yes/no): ").lower() == 'yes'
        if submit1:
            pdf_content = input_pdf_setup(file_path)
            response = get_gemini_response(input_prompt1, pdf_content, input_text)
            print("The response is:")
            print(response)
        submit2 = input("Do you want to know your percentage match with the job description(yes/no)").lower() == 'yes'
        if submit2:
            pdf_content = input_pdf_setup(file_path)
            response = get_gemini_response(input_prompt2, pdf_content, input_text)
            print("The response is:")
            print(response)
        else:
            print("No action selected.")
    else:
        print("File does not exist.")

if __name__=='__main__':
    run_ats_tracking_system()
