# Importing useful libraries
import pdfkit
import streamlit as st
import os

# Defining the path to the executable file and output file
path_to_the_tool = 'tool_file/wkhtmltopdf.exe'
output_file = "output.pdf"

# Creating the configuration to the pdf tool
config = pdfkit.configuration(wkhtmltopdf = path_to_the_tool)

# Creating a title for the page
st.header("Url to pdf convertor")

# Getting the url
url = st.text_input("Enter the url that you need to convert to pdf here: ")

if st.button("Convert"):
    if url:
        if os.path.exists(output_file):
            os.remove(output_file)
            output_file = "output.pdf"
        else:
            pass
        # Converting webpage to pdf
        pdfkit.from_url(url,
                        output_path=output_file,
                        configuration=config
                        )

        st.success("Successfuly Changed the Webpage into pdf!!!")
    
    else:
        st.info("Please first enter the url!!!")