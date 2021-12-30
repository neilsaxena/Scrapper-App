from flask import render_template, request
from scrapperapp import app
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_argument("--headless")

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/prediction", methods=['POST'])
def prediction():
    url_input = request.form["urlinput"]
    
    # Loading Driver ( also Installing Driver if not present)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.maximize_window()

    temp_paragraphs = []
    paragraphs = []

    driver.get(url_input)
    time.sleep(5)
    elements = driver.find_elements_by_tag_name('body')
    paragraphs = []
    for element in elements:
        paragraph = element.text
        paragraphs = paragraph.split("\n")
        break
    driver.close()


    # Check for empty sentence

    scrapped_sentences = []
    for paragraph in paragraphs:
        if paragraph.strip() != '':
            scrapped_sentences.append(paragraph.strip())
    
    return render_template('output.html', scrapped_sentences = scrapped_sentences, url_input = url_input)