# Make imports
import time
import clipboard
from selenium import webdriver


def translate_sentence(sentence):

    # Start a Selenium driver
    driver_path='../chromedriver'
    driver = webdriver.Chrome(driver_path)

    # Reach the deepL website
    deepl_url = 'https://www.deepl.com/fr/translator'
    driver.get(deepl_url)

    # Get thie inupt_area 
    input_css = 'div.lmt__inner_textarea_container textarea'
    input_area = driver.find_element(By.CSS_SELECTOR,input_css)

    # Send the text
    input_area.clear() 
    input_area.send_keys(text_to_translate)

    # Wait for translation to appear on the web page
    time.sleep(2)

    # Get copybutton and click on it
    # button_css = ' div.lmt__target_toolbar__copy button' 
    button_css = '#textareasContainer > div.rounded-br-inherit.relative.z-\[1\].min-h-\[240px\].min-w-0.md\:min-h-\[clamp\(250px\,50vh\,557px\)\].max-\[768px\]\:min-h-\[375px\] > section > div.rounded-inherit.relative.flex.flex-1.flex-col > d-textarea > div'
    button = driver.find_element(By.CSS_SELECTOR,button_css)
    button.click()

    # Get content from clipboard
    content = clipboard.paste()

    # Quit selenium driver
    driver.quit()


if __name__ == "__main__":

    # Define text to translate
    sentence_to_translate = 'This is a translation example for my article.'
    sentence_translated =  translate_sentence(sentence_to_translate)

    # Display results
    print('_'*75, '\n')
    print('Original    :', sentence_to_translate)
    print('-'*75)
    print('Translation :', sentence_translated)
    print('_'*75)




