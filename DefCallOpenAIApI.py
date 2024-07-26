from openai import OpenAI
from dotenv import load_dotenv



load_dotenv()

client = OpenAI()



def call_updatedpromptgpt4preview(pages_data):
    # pages_data= get_pdf_text("/Users/sugupta/Downloads/Bob Johnson - merged.pdf")
    
    
    print(pages_data)
    template = """
    Objective: The objective of this task is to process statement data for a mortgage application. The statement data may be provided in multiple documents or merged into a single document. The goal is to extract relevant information from the statements and generate an output in a consistent JSON structure.

    Input:

    Statement Text: The user will provide the statement text for processing. The statement text may contain information related to bank statements, payslips, SA302 statements, tax overview statements, tax calculation statements, or tax return statements.
    Document Type: The user will specify the type of document being processed (e.g., bank statement, payslip, SA302, tax overview statement, tax calculation statement, or tax return statement).
    Output: The output will be generated in the following JSON structure:

    [
    {
        
        "<DocumentType>": {
        "Is<DocumentType>": true,
        "FirstName": "<firstname>",
        "LastName": "<lastname>",
        "<DocumentType>Periods": {
            "1": {
            "Start": "<Start Date>",
            "End": "<End Date>"
            },
            "2": {
            "Start": "<Start Date>",
            "End": "<End Date>"
            },
            ...
        }
        },
        ...
    }
    ]
        • <DocumentType>: Replace with the specific document type being processed (e.g., BankStatement, PaySlip, SA302, TaxOverviewStatement, TaxCalculationStatement, or TaxReturnStatement).
        • <Start Date>: Replace with the start date of the statement period in dd/mmm/yyyy format.
        • <End Date>: Replace with the end date of the statement period in dd/mmm/yyyy format.

    Instructions:

        1. Receive the statement text 
        2. Most important thing is to look for each doc type periods and capture it in the output. Ensure to capture each period in the output irrespective whether it makes sense or not.
        3. Ensure you convert all the <Start Date> and <End Date> in dd/mmm/yyyy format in JSON output.
        4  Extract the relevant information from the statement text based on the document type.
        5. If only one date is present then use that date month and year to create start date and end date.
        6. Classify statement as SA302 if "Self Assessment" text is followed by "Unique Taxpayer Reference (UTR):".
        7. Classify statement as TaxOverviewStatement if "Tax year overview" text is followed by "Tax year ending". 
        8. Classify statement as TaxReturnStatement look for text "Tax Return <YYYY>" where <YYYY> is the financial year.
        9. Classify statement as TaxCalculationStatement if "Tax calculation summary" text is followed by "Tax year".
        10. Generate the output in the JSON structure mentioned above.
        11.Ensure that the output structure is consistent for every call to maintain compatibility with the user's expectations.
        12.Replace the placeholders <firstname>,<lastname><DocumentType>, <Start Date>, and <End Date> with the appropriate values in the output.
        13.Return the output in the JSON format.
        14.After generating the JSON output, review it against the provided text to ensure all document types have been captured and correctly classified.

    """
    response = client.chat.completions.create(
    model="gpt-4-turbo-preview",temperature=0,
    top_p=1,frequency_penalty=0,presence_penalty=0,
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": template},
        {"role": "user", "content": pages_data}
    ]
    )
    print(response.choices[0].message.content)
    return (response.choices[0].message.content)






