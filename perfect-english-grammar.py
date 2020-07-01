from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from os import path
import datetime

# Initialize ChromeDriver
driver = Chrome("./chromedriver")


def get_page_content(url):

    # go to page 
    driver.get(url)

    # wait for drop field to load
    timeout = 3
    element_present = EC.presence_of_element_located((By.ID, 'content'))
    WebDriverWait(driver, timeout).until(element_present)

    # locate anc click the buttons 
    exercise_buttons = driver.find_elements_by_css_selector(".exerciseButton")
    for button in exercise_buttons:
        button.click()

    # get the table header
    table_h1 = driver.find_elements_by_css_selector("#exercise .exercise h1")
    table_h3 = driver.find_elements_by_css_selector("#exercise .exercise h3")
    table_h1_text = ''
    for h1 in table_h1:
        table_h1_text += h1.text
    
    table_h3_text = ''
    for h3 in table_h3:
        table_h3_text += h3.text

    # get the table body
    result_obj = {}
    table_body = driver.find_elements_by_css_selector("#exercise table tr td:first-child")
    for el in table_body:
        question = el.find_elements_by_css_selector("div:first-child")
        answer = el.find_elements_by_css_selector("div:last-child")
        # create question string
        question_str = ''
        for q in question:
            question_str += q.text
        
        # create answer string
        answer_str = ''
        for a in answer:
            answer_str += a.text
        
        result_obj[question_str] = answer_str

    # save table text to html file 
    f = open(f"perfect{datetime.datetime.now()}.html", "a")
    f.write("<meta charset='UTF-8'>")
    f.write(f"<h1 style='font-style: bold;'>{table_h1_text}</h1>")
    f.write(f"<h2 style='font-style: bold;'>{table_h3_text}</h2><br>")
    for idx in result_obj:
        f.write(f"<h4>{idx}</h4>")
        f.write(f"<h4 style='color:grey; font-style: italic;'>{result_obj[idx]}</h4>")

    f.close()
    print(f"{url} complete!")


def main():
    urls = ["https://www.perfect-english-grammar.com/present-simple-exercise-16.html", 
    "https://www.perfect-english-grammar.com/present-simple-exercise-9.html", 
    "https://www.perfect-english-grammar.com/present-continuous-exercise-5.html", 
    "https://www.perfect-english-grammar.com/past-simple-exercise-3.html",
    "https://www.perfect-english-grammar.com/subject-object-pronouns-exercise-1.html"]
    for url in urls:
        get_page_content(url)


main()