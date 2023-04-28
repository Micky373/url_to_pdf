# Importing useful libraries
import pdfkit
import streamlit as st
import os

# Defining the path to the executable file and output file
path_to_the_tool = 'tool_file/wkhtmltopdf.exe'
output_file = "output.pdf"

# Creating the configuration to the pdf tool
# config = pdfkit.configuration(wkhtmltopdf = path_to_the_tool)

# Creating a title for the page
st.header("Url to pdf convertor")

# Getting the url
url = st.text_input("Enter the url that you need to convert to pdf here: ")

# Creating a button for converting the url
if st.button("Convert"):
    # If the url is passed converting it
    if url:
        # Deleting the path if already exists
        if os.path.exists(output_file):
            os.remove(output_file)
            output_file = "output.pdf"
        else:
            pass
        
        # Displaying the user that it is processing
        st.success("Started converting the url to pdf...")

        # Converting webpage to pdf
        pdfkit.from_url(url,
                        output_path=output_file
                        )

        # Displaying for the user that we successfuly changed the url to pdf
        st.success("Successfuly Changed the Webpage into pdf!!!")

        # Create a download button for the PDF file
        with open(output_file, 'rb') as f:
            contents = f.read()
            st.download_button(label='Download PDF', 
                               data=contents, 
                               file_name='converted.pdf', 
                               mime='application/pdf'
                               )

    
    else:
        st.info("Please first enter the url!!!")
