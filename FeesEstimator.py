import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = ""

def fees_estimator(student_status, location, college, program):
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    driver.get(url)
    time.sleep(2)
    
    el = driver.find_element_by_id("edit-acad-career")
    print(el.text)
    for option in el.find_elements_by_tag_name('option'):
        if option.text == student_status:
            option.click()
            break
    
    el = driver.find_element_by_id("edit-campus")
    for option in el.find_elements_by_tag_name('option'):
        if option.text == location:
            option.click()
            break

    el = driver.find_element_by_id("edit-acad-prog")
    for option in el.find_elements_by_tag_name('option'):
        if option.text == college:
            option.click()
            break

    el = driver.find_element_by_id("edit-program-fee")
    for option in el.find_elements_by_tag_name('option'):
        if option.text == program:
            option.click()
            break    

    driver.find_element_by_id("edit-submit").click()
    time.sleep(8)

    ele = driver.find_element_by_xpath('//tr[10]/td[4]').text
    print(ele)

    driver.close()

if __name__ == "__main__":
    student_status = "Graduate"
    location = "Online"
    college = ""
    program = "Business Analytics, M.S.,"
    fees_estimator(student_status, location, college, program)
