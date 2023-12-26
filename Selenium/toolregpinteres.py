from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
n = int(input("nhập số tài khoản cần tạo : "))

def get_password_from_file():
    with open('password.txt', 'r') as password_file:
        passwords = password_file.read().strip().split('\n')
    # Return the first password from the file
    return passwords[0] if passwords else ''
for i in range(n):
 chrome_driver_path = r"C:\Users\Lenovo\Desktop\Selenium\chromedriver.exe"

 chrome_options = webdriver.ChromeOptions()
 chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
 chrome_options = webdriver.ChromeOptions()

    # Thêm cờ để xóa dấu vết và tránh bị theo dõi
 chrome_options.add_argument("--disable-extensions")
 chrome_options.add_argument("--disable-popup-blocking")
 chrome_options.add_argument("--disable-plugins")
 chrome_options.add_argument("--incognito")
 chrome_options.add_argument("--disable-blink-features=AutomationControlled")
 chrome_options.add_argument("--disable-infobars")
 chrome_options.add_argument("--disable-notifications")
 chrome_options.add_argument("--disable-save-password-bubble")
 chrome_options.add_argument("--disable-password-generation")
 chrome_options.add_argument("--disable-background-networking")
 chrome_options.add_argument("--disable-client-side-phishing-detection")
 chrome_options.add_argument("--disable-default-apps")
 chrome_options.add_argument("--disable-hang-monitor")
 chrome_options.add_argument("--disable-popup-blocking")
 chrome_options.add_argument("--disable-prompt-on-repost")
 chrome_options.add_argument("--disable-sync")
 chrome_options.add_argument("--disable-web-resources")
 chrome_options.add_argument("--enable-automation")
 chrome_options.add_argument("--enable-logging")
 chrome_options.add_argument("--ignore-certificate-errors")
 chrome_options.add_argument("--log-level=0")
 chrome_options.add_argument("--metrics-recording-only")
 chrome_options.add_argument("--no-first-run")
 chrome_options.add_argument("--password-store=basic")
 chrome_options.add_argument("--use-mock-keychain")
 chrome_options.add_argument("--disable-web-security")
 chrome_options.add_argument("--disable-software-rasterizer")
 chrome_options.add_argument("--disable-logging")
 chrome_options.add_argument("--disable-impl-side-painting")
 chrome_options.add_argument("--disable-gpu")
 chrome_options.add_argument("--disable-software-rasterizer")
 chrome_options.add_argument("--enable-automation")
 chrome_options.add_argument("--disable-device-discovery-notifications")
 chrome_options.add_argument("--use-mock-keychain")
 chrome_options.add_argument("--disable-web-security")
 chrome_options.add_argument("--disable-background-timer-throttling")
 chrome_options.add_argument("--disable-backgrounding-occluded-windows")
 chrome_options.add_argument("--disable-renderer-backgrounding")
 chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
 chrome_options.add_experimental_option("useAutomationExtension", False)
 chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
 chrome_options.add_argument("--no-sandbox")
 chrome_options.add_argument("--disable-setuid-sandbox")
 chrome_options.add_argument("--disable-seccomp-filter-sandbox")
 chrome_options.add_argument("--disable-background-networking")
 chrome_options.add_argument("--enable-features=NetworkServiceInProcess")
 chrome_options.add_argument("--disable-features=NetworkService")
 chrome_options.add_argument("--disable-webgl")
 chrome_options.add_argument("--disable-canvas-aa")
 chrome_options.add_argument("--disable-site-isolation-trials")
 chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")


 chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")

 driver = webdriver.Chrome(options=chrome_options)
 driver.get('https://tempmailo.com/')
 wait = WebDriverWait(driver, 30)
 wait.until(EC.url_contains('tempmailo.com'))

 input_element = driver.find_element(By.CSS_SELECTOR, 'input.vs-input')
 data_to_export = input_element.get_attribute('value')

 account_lines = sorted(data_to_export.split('\n'))

 output_file_path = 'output.txt'
 with open(output_file_path, 'a') as file:
    for i, account in enumerate(account_lines):
        password = get_password_from_file()
        account_password_line = f"{account.strip()}|{password.strip()}"
        file.write(account_password_line + '\n')
        print(f"Exported line {i + 1} to {output_file_path}")



 # Mở một tab mới để tránh xung đột giữa các thao tác với các trang khác nhau
 driver.execute_script("window.open('https://www.pinterest.com/', '_blank');")

 # Chuyển sang tab mới
 driver.switch_to.window(driver.window_handles[1])

 # Chờ cho trang Pinterest tải hoàn toàn
 wait = WebDriverWait(driver, 30)
 wait.until(EC.url_contains('pinterest.com'))

 # Xác định input field chính xác và gửi dữ liệu
 button_xpath = '/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[3]/button'
 wait.until(EC.visibility_of_element_located((By.XPATH, button_xpath))).click()

 input_field_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[2]/fieldset/span/div/input'
 input_field = wait.until(EC.visibility_of_element_located((By.XPATH, input_field_xpath)))
 input_field.send_keys(account_lines[0])

 input_field_xpath1 = '/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[4]/fieldset/span/div/input'
 input_field1 = wait.until(EC.visibility_of_element_located((By.XPATH, input_field_xpath1)))
 input_field1.send_keys(get_password_from_file())
 input_field_xpath111 = '/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[7]'
 input_field111 = wait.until(EC.visibility_of_element_located((By.XPATH, input_field_xpath111)))
 input_field111.click()
 input_field_xpath2 = '/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[7]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/select/option[9]'
 input_field2 = wait.until(EC.visibility_of_element_located((By.XPATH, input_field_xpath2)))
 input_field2.click()
 time.sleep(5)
 input_field_xpath2_1_1 = '/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[7]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[4]'
 input_field2_1_1 = wait.until(EC.visibility_of_element_located((By.XPATH, input_field_xpath2_1_1)))
 input_field2_1_1.click()
 input_field_xpath2_1='/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[5]'
 input_field2_1 = wait.until(EC.visibility_of_element_located((By.XPATH, input_field_xpath2_1)))
 input_field2_1.click()
 time.sleep(5)
 input_field_xpath3 = '/html/body/div[3]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/button/div'
 input_field3 = wait.until(EC.visibility_of_element_located((By.XPATH, input_field_xpath3)))
 input_field3.click()

 input_field_xpath4 = '/html/body/div[3]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/button/div'
 input_field4 = wait.until(EC.visibility_of_element_located((By.XPATH, input_field_xpath4)))
 input_field3.click()
 input_field_xpath5 = '/html/body/div[3]/div/div/div/div[2]/div/div/div/div[2]/div/fieldset/div/div[1]/div/label/div/div[1]'
 input_field5 = wait.until(EC.visibility_of_element_located((By.XPATH, input_field_xpath5)))
 input_field5.click()
 input_field_xpath6='/html/body/div[3]/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/button'
 input_field6 = wait.until(EC.visibility_of_element_located((By.XPATH, input_field_xpath6)))
 input_field6.click()
 input_field_xpath7='/html/body/div[3]/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/div[1]/div/div/div/div/div/div/div[1]/div/div'
 input_field7 = wait.until(EC.visibility_of_element_located((By.XPATH, input_field_xpath7)))
 input_field7.click()
 input_field_xpath8='/html/body/div[3]/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/div[2]/div/div/div/div/div/div/div[1]/div/div'
 input_field8 = wait.until(EC.visibility_of_element_located((By.XPATH, input_field_xpath8)))
 input_field8.click()
 input_field_xpath9='/html/body/div[3]/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/div[3]/div/div/div/div/div/div/div[1]/div/div'
 input_field9 = wait.until(EC.visibility_of_element_located((By.XPATH, input_field_xpath9)))
 input_field9.click()
 input_field_xpath10='/html/body/div[3]/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/div[4]/div/div/div/div/div/div/div[1]/div/div'
 input_field10 = wait.until(EC.visibility_of_element_located((By.XPATH, input_field_xpath10)))
 input_field10.click()
 input_field_xpath11='/html/body/div[3]/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/div[5]/div/div/div/div/div/div/div[1]/div/div'
 input_field11 = wait.until(EC.visibility_of_element_located((By.XPATH, input_field_xpath11)))
 input_field11.click()
 input_field_xpath12='/html/body/div[3]/div/div/div/div[2]/div/div/div/div[3]/div/div[4]/div[2]/button'
 input_field12 = wait.until(EC.visibility_of_element_located((By.XPATH, input_field_xpath12)))
 input_field12.click()
 input_field_xpath13='/html/body/div[3]/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/button'
 input_field13 = wait.until(EC.visibility_of_element_located((By.XPATH, input_field_xpath13)))
 input_field13.click()


 # Đợi thêm một khoảng thời gian để kiểm tra kết quả
 time.sleep(10)

 # Đóng trình duyệt
 driver.quit()
