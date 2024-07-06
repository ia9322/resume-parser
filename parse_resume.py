import fitz 
import json

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def parse_resume_to_json(resume_text):
    parsed_data = {
        "contact_information": {
            "email": "",
            "phone": "",
            "address": ""
        },
        "education": [],
        "achievements": [],
        "skills": [],
        "certifications": [],
        "projects": []
    }

    lines = resume_text.split('\n')
    for line in lines:
        if 'Name:' in line:
            parsed_data['name'] = line.split('Name:')[1].strip()
        elif 'Email:' in line:
            parsed_data['contact_information']['email'] = line.split('Email:')[1].strip()
        elif 'Phone:' in line:
            parsed_data['contact_information']['phone'] = line.split('Phone:')[1].strip()
        elif 'Address:' in line:
            parsed_data['contact_information']['address'] = line.split('Address:')[1].strip()
        elif 'Degree:' in line:
            education = {
                "degree": line.split('Degree:')[1].strip(),
                "institution": "",
                "graduation_year": ""
            }
            parsed_data['education'].append(education)
        elif 'Job Title:' in line:
            work_experience = {
                "job_title": line.split('Job Title:')[1].strip(),
                "company": "",
                "start_date": "",
                "end_date": "",
                "responsibilities": []
            }
            parsed_data['work_experience'].append(work_experience)
        elif 'Skills:' in line:
            skills = line.split('Skills:')[1].strip().split(', ')
            parsed_data['skills'].extend(skills)
        elif 'Certifications:' in line:
            certifications = line.split('Certifications:')[1].strip().split(', ')
            parsed_data['certifications'].extend(certifications)
        elif 'Project:' in line:
            project = {
                "title": line.split('Project:')[1].strip(),
                "description": "",
                "technologies": []
            }
            parsed_data['projects'].append(project)
    return json.dumps(parsed_data, indent=4)

pdf_path = 'resume.pdf'
resume_text = extract_text_from_pdf(pdf_path)
parsed_json = parse_resume_to_json(resume_text)
print(parsed_json)
