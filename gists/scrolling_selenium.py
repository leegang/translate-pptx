# Getting button location on  the html tree
# button_css = ' div.lmt__target_toolbar__copy button' 
button_css = '#textareasContainer > div.rounded-br-inherit.relative.z-\[1\].min-h-\[240px\].min-w-0.md\:min-h-\[clamp\(250px\,50vh\,557px\)\].max-\[768px\]\:min-h-\[375px\] > section > div.rounded-inherit.relative.flex.flex-1.flex-col > d-textarea > div'

# Getting the button object
button = driver.find_element(By.CSS_SELECTOR,button_css)

# Extracting its position
y = button.location['y']

# Positionning the button into the screen
driver.execute_script("window.scrollTo(0, {})".format(y - 150))

# Getting the button object
# (again - its position has been actualized and we need to get the new positions for the click)
button = driver.find_element(By.CSS_SELECTOR,button_css)

# Making the click => translation is now in our clipboard
button.click()