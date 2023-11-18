from docxtpl import DocxTemplate 
import datetime 

# these variable names are arbitrary
company_name = input("Enter the name of the company: ")
job_title = input("Enter the name of the position: ")
date = datetime.datetime.today().strftime("%B %d, %Y")

# context name should be the same as the docx {{name}}
# example: int docx: {{data}}, context should have 'date' as today's date name
# so that it could be well recognized and substituted
context = {
    'date' : date, 
    'company_name' : company_name,
    'job_title' : job_title
}

# Openning our template 
doc = DocxTemplate("CoverLetter.docx")

# Load this doc 
doc.render(context)
doc.save("CoverLetter" + company_name + job_title + '.docx')