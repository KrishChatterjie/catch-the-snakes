from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
# import chromedriver_autoinstaller
from bs4 import BeautifulSoup
import time
import sys
import os
driver = None

def check_scroll():
    global driver
    try:
        WebDriverWait(driver, 3 ).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "oMwYe")))
    except TimeoutException:
        return False
    return True

def get_list(need_name_img):
    global driver
    try:
        name_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "isgrP")))
    finally:
        pass

    follow_list = []
    i= 0
    # Scrolling through list
    while check_scroll():
        try: 
            driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", name_box)
        finally:
            pass
        html = driver.find_element_by_class_name('isgrP').get_attribute('innerHTML')
        soup = BeautifulSoup(html, "html.parser")
        props = soup.find_all("div", class_ = "t2ksc")
        names = driver.find_elements_by_class_name('wFPL8 ')
        for prop in props[i::]:
            try:
                username = [n.text for n in prop.find_all("a") if n.text != '']
                if(need_name_img):
                    img = prop.find("img")
                    if img:
                        img= img.attrs['src']
                    name = names[i].text
                    follow_list.append([username[0], name, img])
                else:
                    follow_list.append(username[0])
            except NoSuchElementException:
                follow_list.append([username[0], '', ''])
            i += 1
    try:
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", name_box)
    finally:
        pass
    html = driver.find_element_by_class_name('isgrP').get_attribute('innerHTML')
    soup = BeautifulSoup(html, "html.parser")
    props = soup.find_all("div", class_ = "t2ksc")
    names = driver.find_elements_by_class_name('wFPL8 ')
    for prop in props[i::]:
        try:
            username = [n.text for n in prop.find_all("a") if n.text != '']
            if(need_name_img):
                img = prop.find("img")
                if img:
                    img = img.attrs['src']
                name = names[i].text
                follow_list.append([username[0], name, img])
            else:
                follow_list.append(username[0])
        except:
            follow_list.append([username[0], '', ''])
        i += 1

    return follow_list


def send_request():
    global driver
    try:
        follow = driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")
    except NoSuchElementException:
        driver.quit()
        return False
    follow.send_keys(Keys.RETURN)
    driver.quit()

def run(para1, para2):
    
    global driver
    chrome_options = Options()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")

    # chromedriver_autoinstaller.install()

    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)    

    url = "https://www.instagram.com/"
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.TAG_NAME, "input")))
    finally:
        pass

    # Logging in to instagram
    uid = driver.find_element_by_name("username")
    uid.send_keys("catchthesnakes101")
    password = driver.find_element_by_name("password")
    password.send_keys(os.environ.get("PASSWORD"))
    login = driver.find_element_by_xpath('//button[@type = "submit"]')
    login.click()

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@type = 'text' and @placeholder = 'Search']")))
    except:
        pass
    finally:
        pass

    #Getting input for username
    usernameSearch = para1

    # Going to profile
    search = driver.find_element_by_xpath("//input[@type = 'text']")
    search.send_keys(usernameSearch)

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "VR6_Q")))
    except:
        pass
    finally:
        pass
    search = driver.find_element_by_xpath("//input[@type = 'text']") # to reconfigure
    search.send_keys(Keys.ARROW_DOWN)
    search.send_keys(Keys.RETURN)

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "-nal3 ")))
    except:
        pass
    finally:
        pass
        
    # Private / Public
    vis = para2
    if vis == 'private':
        try:
            send_request()
        except NoSuchElementException:
            return ['PRIVATEREQUEST']
        return ['PRIVATEREQUEST']

    # Opening following list
    try :
        driver.find_element_by_xpath("//a[contains(@href, '/following')]").click()
    except NoSuchElementException:
        send_request()
        return ['PRIVATEIDIOT']

    following = get_list(True)
    driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()

    # Opening followers list
    driver.find_element_by_xpath("//a[contains(@href, '/followers')]").click()
    followers = get_list(False)
    driver.quit()

    # Catching the snakes
    t = tuple(followers)
    unfollowers = [x for x in following if x[0] not in t]
    return unfollowers

    # Used for testing
    # driver.save_screenshot('ss.png')
    # return [['jimmypage', 'Jimmy Page', 'https://instagram.fccu4-2.fna.fbcdn.net/v/t51.2885-19/s150x150/49279043_283782525590401_814791695899033600_n.jpg?_nc_ht=instagram.fccu4-2.fna.fbcdn.net&_nc_ohc=ZgoWpE3QlLYAX8osiNk&tp=1&oh=fb344b03929680d58287037e4b848002&oe=6012F443'], ['matthewscott92', 'Matthew Scott', 'https://instagram.fccu4-2.fna.fbcdn.net/v/t51.2885-19/s150x150/89059760_1051935718516119_7993712269965918208_n.jpg?_nc_ht=instagram.fccu4-2.fna.fbcdn.net&_nc_ohc=oJn0NPK9yZkAX98P1A6&tp=1&oh=d2ec5ea7699b34b8b6809ac50b0fbcef&oe=601288E3'], ['ledzeppelin', 'Led Zeppelin', 'https://instagram.fccu4-2.fna.fbcdn.net/v/t51.2885-19/s150x150/42182928_236452060356423_1071468343191404544_n.jpg?_nc_ht=instagram.fccu4-2.fna.fbcdn.net&_nc_ohc=1UITB6zm7sEAX-tHIbH&tp=1&oh=462f3f7a84de1a7b9b18db88d5879b36&oe=60150723'], ['masonmount10', 'MM', 'https://instagram.fccu4-2.fna.fbcdn.net/v/t51.2885-19/s150x150/123385396_372846370501948_236691274774390555_n.jpg?_nc_ht=instagram.fccu4-2.fna.fbcdn.net&_nc_ohc=kRfDOYPR-YAAX-qVVbf&tp=1&oh=e925a45ef6de04daea902aaf9b19e48c&oe=6014D5DC'], ['brfootball', 'Bleacher Report Football', 'https://instagram.fccu4-2.fna.fbcdn.net/v/t51.2885-19/s150x150/100966069_1681674958651229_3821187125705965568_n.jpg?_nc_ht=instagram.fccu4-2.fna.fbcdn.net&_nc_ohc=KbHKiRQVSbkAX-pZX7n&tp=1&oh=f492ec15a0c1a44610b6d7e743b338cb&oe=6014A085'], ['voyaged', 'VOYAGED by 9GAG', 'https://instagram.fccu4-2.fna.fbcdn.net/v/t51.2885-19/s150x150/30084491_119452552244908_2758295346873368576_n.jpg?_nc_ht=instagram.fccu4-2.fna.fbcdn.net&_nc_ohc=fu_JY5CPxA8AX_9JcOM&tp=1&oh=8d139beb3db8507bd6b907bf394bb3d3&oe=6013C867'], ['musiciswin', 'Music is Win', 'https://instagram.fccu4-2.fna.fbcdn.net/v/t51.2885-19/s150x150/49858254_624986028271437_8786958292489338880_n.jpg?_nc_ht=instagram.fccu4-2.fna.fbcdn.net&_nc_ohc=MEwkSdW837kAX8tF8qV&tp=1&oh=c770cf8f6c641b37e986f932bb0d6586&oe=60154FD4'], ['pauldavidsguitar', 'Paul Davids', 'https://instagram.fccu4-2.fna.fbcdn.net/v/t51.2885-19/s150x150/59739463_481156642423473_7317606343660011520_n.jpg?_nc_ht=instagram.fccu4-2.fna.fbcdn.net&_nc_ohc=6AkN555vpi8AX_3Tk3s&tp=1&oh=725dd308404b8e3722270837bb61cb96&oe=6014685A'], ['rabeaafro', 'Rabea Massaad', 'https://instagram.fccu4-2.fna.fbcdn.net/v/t51.2885-19/s150x150/84409612_500673193949420_1743532877070467072_n.jpg?_nc_ht=instagram.fccu4-2.fna.fbcdn.net&_nc_ohc=Pxyg15omL8MAX93qV3N&tp=1&oh=467ce92e3ce80cf930cbfb853a3b25c2&oe=601528BA'], ['telelicks', 'Kade', 'https://instagram.fccu4-2.fna.fbcdn.net/v/t51.2885-19/s150x150/102556018_1665657886920234_3978485248499477692_n.jpg?_nc_ht=instagram.fccu4-2.fna.fbcdn.net&_nc_ohc=CdXDud0wLPoAX9hW_vn&tp=1&oh=2077448aadb0eb23a2d43b99b822ff8c&oe=60155226'], ['mateusasato', 'Mateus Asato', 'https://instagram.fccu4-2.fna.fbcdn.net/v/t51.2885-19/s150x150/121171576_374669057018823_6065863124893581694_n.jpg?_nc_ht=instagram.fccu4-2.fna.fbcdn.net&_nc_ohc=BUrrWdVV58YAX8ZuvWx&tp=1&oh=009a7f053d0067fb395b01f553ad0a22&oe=6014D97D'], ['factbolt', 'FactBolt', 'https://instagram.fccu4-2.fna.fbcdn.net/v/t51.2885-19/s150x150/64306726_2279016635545046_5168744999000473600_n.jpg?_nc_ht=instagram.fccu4-2.fna.fbcdn.net&_nc_ohc=nvr2esrEVksAX_Y3kzE&tp=1&oh=52d6a5edda148b70c7278c18c182ec3e&oe=601362F2']] 
