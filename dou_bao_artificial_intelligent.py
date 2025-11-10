import textwrap
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_conditions
from loguru import logger
from cite_parts import driver_search_start_no_proxy
from data_part import origin_all_possible_data

def dou_bao_artificial_intelligent(dou_bao_search_content):
    dou_bao_source_url = 'https://www.doubao.com/chat'

    dou_bao_driver = driver_search_start_no_proxy()
    wait = WebDriverWait(dou_bao_driver, 30)

    try:
        dou_bao_driver.get(dou_bao_source_url)
        dou_bao_driver.maximize_window()
        dou_bao_driver.minimize_window()

        click_to_input_location = '/html/body/div[1]/div[1]/div/div[3]/div/main/div/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/textarea'
        click_first = wait.until(e_conditions.presence_of_element_located((By.XPATH, click_to_input_location)))
        click_first.click()
        input_second = wait.until(e_conditions.presence_of_element_located((By.XPATH, click_to_input_location)))
        input_second.send_keys(dou_bao_search_content)

        try:
            search_button_location = '/html/body/div[1]/div[1]/div/div[3]/div/main/div/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div[2]/button'
            search_button = wait.until(e_conditions.presence_of_element_located((By.XPATH, search_button_location)))
            search_button.click()

            judge_condition = '/html/body/div[1]/div[1]/div/div[3]/div/main/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div/div[3]'
            try:
                if wait.until(e_conditions.presence_of_element_located((By.XPATH, judge_condition))):
                    result_source_html_location = '/html/body/div[1]/div[1]/div/div[3]/div/main/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/div'
                    result_source_html = wait.until(e_conditions.presence_of_element_located(
                        (By.XPATH, result_source_html_location))).get_attribute('outerHTML')
                    result_soup = BeautifulSoup(result_source_html, 'lxml')

                    result_text = result_soup.text
                    textwrap_result_text = textwrap.wrap(str(result_text))
                    origin_all_possible_data.append(textwrap_result_text)
                    dou_bao_driver.quit()
                    return origin_all_possible_data

            except Exception as w:
                logger.error(f'搜索结果文本获取失败:{w}')


        except Exception as e:
            logger.error(f'{e}')

    except Exception as e:
        logger.error(f'输入搜索操作错误:{e}')


if __name__ == '__main__':
    dou_bao_artificial_intelligent(dou_bao_search_content='456789')