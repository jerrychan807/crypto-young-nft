#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2022/7/3 12:57 AM
# @Author  : Jerry
# @Desc    : 
# @File    : tool.py
import json
import time
import os
from time import sleep
import traceback

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By

from log import logger

from config import ImgFolderPath, BaseUri, ExecutablePath, Website, Count, MaxDownloadNum


class Tool():
    def __init__(self):
        self.count = Count
        self.max_download_num = MaxDownloadNum

    def init_browser(self):
        """
        初始化浏览器
        :return: 
        """
        # print(os.system("pkill chrome"))
        # print(sleep(10))

        options = webdriver.ChromeOptions()
        # options.add_argument('--disable-gpu')  # 无需要gpu加速
        options.add_argument('--no-sandbox')  # 无沙箱
        # options.add_argument("--headless")
        # self.browser = webdriver.Chrome(executable_path="/root/chromedriver", chrome_options=options)
        prefs = {"download.default_directory": ImgFolderPath}
        # 将自定义设置添加到chrome配置对象实例中
        options.add_experimental_option("prefs", prefs)
        # executable_path = '/Users/chanjerry/Downloads/chromedriver'
        self.driver = webdriver.Chrome(executable_path=ExecutablePath, chrome_options=options)

    def get_chrome_request_html(self):
        """

        :return:
        """
        self.driver.get(Website)
        sleep(4)
        try:
            # self.element = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, "//div[@class='mb-1 d-flex flex-column lh-1']/span"))
            # )

            self.soup = bs(self.driver.page_source, 'html.parser')
            # print(self.driver.page_source)

            # 循环下载
            for num in range(self.max_download_num):
                self.random_pic()
                code = self.get_picture_json()

                uri_dict, tag = self.codestr_to_urifile(code)
                if tag:
                    self.manage_json_file(uri_dict)
                    self.download_pic()
                    sleep(2)
                    self.manage_img_file()
                    self.count += 1
                else:
                    continue

                time.sleep(0.5)
        except Exception as e:
            logger.error(e)
            logger.error(traceback.format_exc())
            # pass
        # finally:
        #     self.driver.quit()

    def random_pic(self):
        button_list = self.driver.find_element(By.CLASS_NAME, 'action-group').find_elements(By.TAG_NAME,
                                                                                            'button')
        randomize_button = button_list[0]
        # 点击随机生成按钮
        randomize_button.click()

    def download_pic(self):
        logger.debug("[*] try to download img: {}".format(self.count))
        button_list = self.driver.find_element(By.CLASS_NAME, 'action-group').find_elements(By.TAG_NAME,
                                                                                            'button')
        download_button = button_list[1]
        # 点击下载按钮,下载图片
        download_button.click()

    def get_picture_json(self):
        button_list = self.driver.find_element(By.CLASS_NAME, 'action-menu').find_elements(By.TAG_NAME, 'div')
        code_button = button_list[-1]
        code_button.click()
        time.sleep(0.5)
        code = self.driver.find_element(By.ID, 'copy-code-btn').get_attribute('data-clipboard-text')
        # print(code)
        # 点击关闭按钮
        button_list = self.driver.find_element(By.CLASS_NAME, 'code-header').find_elements(By.TAG_NAME, 'div')
        close_button = button_list[-1]
        time.sleep(0.5)
        close_button.click()
        return code

    def manage_img_file(self):
        '''
        管理下载的文件
        :return:
        '''
        logger.debug("[*] try to manage resource file: {}".format(self.count))
        # 重命名图片文件名
        os.rename("{folder}/vue-color-avatar.png".format(folder=ImgFolderPath),
                  "{folder}/{img_num}.png".format(folder=ImgFolderPath, img_num=self.count))

    def manage_json_file(self, uri_dict):
        '''
        保存json文件
        :param uri_dict:
        :return:
        '''

        json_file = "{folder}/{img_num}.json".format(folder=ImgFolderPath, img_num=self.count)
        with open(json_file, 'w') as f:
            json_data = json.dumps(uri_dict)
            f.write(json_data)
            f.close()

    def codestr_to_urifile(self, code):
        """
        转换成uri的内容
        :return:
        """
        uri_dict = {}
        code_dict = json.loads(code)
        # 处理attributes部分
        uri_dict['attributes'] = []

        for attribute_name, value_info in code_dict['widgets'].items():
            if attribute_name == 'eyes':
                # 处理空眼睛元素的情况
                if not value_info:
                    return uri_dict, False

            if attribute_name == 'tops':
                uri_dict['attributes'].append({
                    "trait_type": "{attribute}".format(attribute='Tops'),
                    "value": "{value}".format(value=value_info['shape'])
                })

                if 'fillColor' in value_info:
                    uri_dict['attributes'].append({
                        "trait_type": "{attribute}".format(attribute='TopsColor'),
                        "value": "{value}".format(value=value_info['fillColor'])

                    })
                else:
                    uri_dict['attributes'].append({
                        "trait_type": "{attribute}".format(attribute='TopsColor'),
                        "value": "{value}".format(value='none')
                    })
            elif attribute_name == 'clothes':
                uri_dict['attributes'].append({
                    "trait_type": "{attribute}".format(attribute='Clothes'),
                    "value": "{value}".format(value=value_info['shape'])
                })
                if 'fillColor' in value_info:
                    uri_dict['attributes'].append({
                        "trait_type": "{attribute}".format(attribute='ClothesColor'),
                        "value": "{value}".format(value=value_info['fillColor'])
                    })
                else:
                    uri_dict['attributes'].append({
                        "trait_type": "{attribute}".format(attribute='ClothesColor'),
                        "value": "{value}".format(value='none')})
            else:
                if 'shape' in value_info:
                    uri_dict['attributes'].append({
                        "trait_type": "{attribute}".format(attribute=attribute_name.capitalize()),
                        "value": "{value}".format(value=value_info['shape'])
                    })
                else:
                    uri_dict['attributes'].append({
                        "trait_type": "{attribute}".format(attribute=attribute_name.capitalize()),
                        "value": "{value}".format(value='none')
                    })
        uri_dict['name'] = "CryptoYoung #{}".format(self.count)
        uri_dict['image'] = "{}/{}.png".format(BaseUri, self.count)
        return uri_dict, True

    def run(self):
        self.init_browser()
        self.get_chrome_request_html()
        # print(self.tx_list)
        # print(self.token_info)


if __name__ == '__main__':
    # delay = int(input('Delay bettween each update: '))
    print('Wait for some time to load the page...Its running..')
    tool_ins = Tool()
    tool_ins.run()
