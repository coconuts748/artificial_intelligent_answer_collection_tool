import textwrap
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_conditions
from loguru import logger
from cite_parts import driver_search_start_no_proxy
from data_part import origin_all_possible_data


def na_mi_artificial_intelligent(na_mi_search_content):
    na_mi_artificial_url = 'https://www.n.cn/?src=360ai_so_wenda'
    na_mi_driver = driver_search_start_no_proxy()

    wait = WebDriverWait(na_mi_driver, 120)
    na_mi_driver.get(na_mi_artificial_url)
    na_mi_driver.maximize_window()
    na_mi_driver.minimize_window()
    try:
        top_page_location = '/html/body/div[1]/div/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div[3]/div[2]/section[1]/div/textarea'
        search_column = wait.until(e_conditions.presence_of_element_located((By.XPATH, top_page_location)))
        search_column.click()
        search_column.send_keys(na_mi_search_content)

        if_be_clickable_location = '/html/body/div[1]/div/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div[3]/div[2]/section[2]/div[2]/span/button'
        na_mi_driver.implicitly_wait('20')
        if_be_clickable = na_mi_driver.find_element(By.XPATH, if_be_clickable_location)
        if_be_clickable.click()

        na_mi_driver.minimize_window()

        iframe_location = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/iframe'
        na_mi_driver.switch_to.frame(na_mi_driver.find_element(By.XPATH, iframe_location))
        try:
            if wait.until(e_conditions.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[3]/div[4]'))):
                print('aaaaa')
                iframe_result_content_location = '/html/body/div[1]/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]'
                iframe_text_content = na_mi_driver.find_element(By.XPATH, iframe_result_content_location).get_attribute(
                    'outerHTML')

                final_result_soup = BeautifulSoup(iframe_text_content, 'lxml')
                final_result_text = final_result_soup.text
                textwrap_final_result_text = textwrap.wrap(str(final_result_text))
                logger.info(textwrap_final_result_text)

                origin_all_possible_data.append(textwrap_final_result_text)
                na_mi_driver.quit()
                return origin_all_possible_data

        except Exception as e:
            logger.error(f'iframe操作失败:{e}')

    except Exception as e:
        logger.error(f'搜索栏定位失败:{e}')

if __name__ == '__main__':
    na_mi_artificial_intelligent(na_mi_search_content='12312313123')