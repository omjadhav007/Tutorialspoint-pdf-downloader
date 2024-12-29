import urllib.request

def downloadFile(url,pdf_file_name):
    try:
        # # Download the PDF file
        # urllib.request.urlretrieve(url, pdf_file_name)

        # Create a request with a user-agent header
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        request = urllib.request.Request(url, headers=headers)

        # Open the URL and save the content
        with urllib.request.urlopen(request) as response, open(pdf_file_name, 'wb') as out_file:
            out_file.write(response.read())

        print(f"PDF downloaded successfully as '{pdf_file_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
tld = "https://www.tutorialspoint.com/"
#enter any tutorials url name from the website
#in the future we could scrape and show a menu
query = input("Enter Name of Tutorial : ")
url = tld+query+'/'+query+'_tutorial.pdf'
pdf_file_name=query+'_tutorial.pdf'

downloadFile(url,pdf_file_name)