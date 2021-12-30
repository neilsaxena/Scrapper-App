# Importing Libraries
from flask import render_template, request
from scrapperapp import app
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_argument("--headless")

# Defining default route
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

# Route for displaying scrapped data
@app.route("/prediction", methods=['POST'])
def prediction():
    url_input = request.form["urlinput"]
    
    # Loading Driver ( also Installing Driver if not present)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.maximize_window()

    paragraphs = []

    # Opening given url in web browser
    driver.get(url_input)
    # Waiting for the page to load properly in browser
    time.sleep(5)
    # Scrapping text content
    element = driver.find_element_by_tag_name('body')
    scrapped_body = element.text
    driver.close()
    paragraphs = scrapped_body.split("\n")

    # Check for empty sentence
    scrapped_sentences = []
    for paragraph in paragraphs:
        if paragraph.strip() != '':
            scrapped_sentences.append(paragraph.strip())
    
    return render_template('output.html', scrapped_sentences = scrapped_sentences, url_input = url_input)