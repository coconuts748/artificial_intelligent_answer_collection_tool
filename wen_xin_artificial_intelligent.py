import textwrap
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_conditions
from loguru import logger
from cite_parts import driver_search_start_no_proxy
from data_part import origin_all_possible_data

def wen_xin_artificial_intelligent(wen_xin_search_content):
    wen_xin_source_url = 'https://chat.baidu.com/search?extParams=%7B%22enter_type%22%3A%22home_operate%22%7D&isShowHello=1'

    wen_xin_driver =  driver_search_start_no_proxy()
    wait = WebDriverWait(wen_xin_driver, 30)

    try:
        wen_xin_driver.get(wen_xin_source_url)
        wen_xin_driver.maximize_window()
        wen_xin_driver.minimize_window()

        click_to_type_location = '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[4]/div[1]/div[2]/textarea'
        click_first = wait.until(e_conditions.presence_of_element_located((By.XPATH, click_to_type_location)))
        click_first.click()
        type_second = wait.until(e_conditions.presence_of_element_located((By.XPATH, click_to_type_location)))
        type_second.send_keys(wen_xin_search_content)

        searching_button_location = '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[4]/div[1]/div[3]/div[3]/img'
        searching_button = wait.until(e_conditions.presence_of_element_located((By.XPATH, searching_button_location)))
        searching_button.click()

        try:
            judge_condition = '/html/body/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/div/div[1]/div[3]/div[2]/div/div[2]/div/div/div'
            try:
                if wait.until(e_conditions.presence_of_element_located((By.XPATH, judge_condition))):
                    result_content_location = '/html/body/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/div/div[1]/div[3]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div[2]'
                    result_content_resource = wen_xin_driver.find_element(By.XPATH,
                                                                          result_content_location).get_attribute(
                        'outerHTML')
                    result_content_soup = BeautifulSoup(result_content_resource, 'lxml')
                    result_content_text = result_content_soup.text

                    textwrap_result = textwrap.wrap(str(result_content_text))
                    logger.info(textwrap_result)
                    origin_all_possible_data.append(textwrap_result)
                    wen_xin_driver.quit()
                    return origin_all_possible_data

            except Exception as w:
                logger.error(f'搜索结果错误:{w}')


        except Exception as e:
            logger.error(e)

    except Exception as e:
        logger.error(f'原网址操作有误:{e}')

if __name__ == '__main__':
    wen_xin_artificial_intelligent(wen_xin_search_content='123')