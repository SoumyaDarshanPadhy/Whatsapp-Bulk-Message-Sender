from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import csv



no_of_message = 1

moblie_no_list = []
invalidNumbers = []

with open("D:\\Whatsapp-Bulk-Message-Sender\\final.csv", 'r') as csvfile:
    moblie_no_list = [row[0]
                      for row in csv.reader(csvfile, delimiter=';')]




def element_presence(by, xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)


def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except BaseException:
        is_connected()


driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("http://web.whatsapp.com")
sleep(10)




def send_whatsapp_msg(phone_no, text):

    driver.get(
        "https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no)
    )

    try:
        driver.switch_to.alert()

    except Exception as e:
        pass

    try:
        element_presence(
            By.XPATH,
            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',
            30)
        txt_box = driver.find_element(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")
            sleep(10)

    except Exception as e:
        invalidNumbers.append(str(phone_no))
        print("Invailid phone no :" + str(phone_no))


def main():

    for moblie_no in moblie_no_list:
        allData = moblie_no.split(',')
        mno = "91"+allData[0]
        iD = allData[1]
        password = allData[2]
        name = allData[3]
        message_text = "Dear" +" "+name+" "+"Your Id is " + iD+" Your password is : " + password
        print(message_text)
        try:
            send_whatsapp_msg(phone_no=mno, text=message_text)

        except Exception as e:

            sleep(10)
            is_connected()




if __name__ == '__main__':
    main()
    
print(invalidNumbers)
