from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from loguru import logger
import json
import textwrap

def driver_search_start_no_proxy():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    chrome = webdriver.Chrome(options=options, service=Service('chromedriver.exe'))
    chrome.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': 'Object.defineProperty(navigable, "webdriver", {get: () => undefined})"'
    })
    return chrome

def write_json_(json_content,json_name):
    if len(str(json_content)) == 0:
        logger.error('内容为空!')

    try:
        with open(f'{json_name}.json','wb') as f:
            f.write(json.dumps(json_content,ensure_ascii=False).encode('utf-8'))
        logger.info('文件写入成功!')
    except Exception as e:
        logger.error(f'文件写入失败:{e}')

# write_json_(json_content='啊啊啊啊',json_name='123')

def write_txt_(txt_content,txt_name,if_addition):
    if len(str(txt_content)) == 0:
        logger.error('内容为空!')
    try:
        if if_addition == 'True':
            for i in txt_content:
                with open(f'{txt_name}.txt','a',encoding='utf-8') as f:
                    writing_content_a = f'{i}\n'
                    f.write(writing_content_a)
            logger.info('文件写入成功!')
        else:
            with open(f'{txt_name}.txt','w',encoding='utf-8') as f:
                writing_content_w = str(txt_content).replace('[','').replace(']','')
                writing_content_w_ = textwrap.wrap(writing_content_w)
                f.write(str(writing_content_w_))
            logger.info('文件写入成功!')

    except Exception as e:
        logger.error(f'txt文件写入失败:{e}')

# test_list=[1,2,3,4]
# write_txt_(txt_content=test_list,txt_name='test_list',if_addition='True')


