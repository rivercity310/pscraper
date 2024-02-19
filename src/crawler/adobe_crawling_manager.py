from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import Any
from abc import abstractmethod
from crawler.crawling_manager import CrawlingManager
from classes import AdobeCommon
from const import ADB_OPTIONAL_TITLE, ADB_SECURITY_BULLETIN, logger


# Continuous 버전과 Classic 버전 수집 과정에서 공통 기능을 두기 위한 부모 클래스
class AdobeCrawlingManager(CrawlingManager):
    result: dict[str, Any] = dict()
    
    
    def __init__(self, category: str, url: str):
        super().__init__(category, url)
        keys = self.meta["adobe_excel_key"]
        
        for key in keys:
            logger.info(f"{key} 초기화 완료")
            self.result[key] = dict()
        
        
    @abstractmethod
    def run(self) -> None:
        pass
    
    
    @abstractmethod
    def download_patch_files(self, link) -> list[str]:
        pass
    
    
    def get_patch_link(self, ul_path: str) -> str:
        self._driver_wait(by = By.XPATH, name = ul_path)
        ul = self.driver.find_element(by = By.XPATH, value = ul_path)
        
        for idx, li in enumerate(ul.find_elements(by = By.TAG_NAME, value = "li"), start = 1):
            if idx == 1:
                link = li.find_element(by = By.TAG_NAME, value = "a").get_attribute("href")
                
            logger.info(f"{idx}. {li.text}")

        return link
    
    
    def get_summary(self) -> str:
        sec = self.find_security_bulletin()
        
        if sec != None:
            return sec.text
        
        return self.find_optional_title().text    
    
    
    def get_security_title(self, product: str, version: str, bulletin_id: str = None) -> str:
        title = AdobeCommon.SECURITY_UPDATE_TITLE_FORMAT.format(product, version)
        if bulletin_id: title += f"({bulletin_id})"
        return title
    
    
    def is_security_update(self) -> bool:
        sec = self.find_security_bulletin()
        return True if sec else False
    

    def find_security_bulletin(self) -> WebElement | None:
        try:
            self._driver_wait(by = By.XPATH, name = ADB_SECURITY_BULLETIN)
            return self.driver.find_element(by = By.XPATH, value = ADB_SECURITY_BULLETIN)
        
        except Exception as e:
            logger.info(e)
            return None
    
    
    def find_optional_title(self) -> WebElement | None:
        try:
            self._driver_wait(by = By.XPATH, name = ADB_OPTIONAL_TITLE)
            return self.driver.find_element(by = By.XPATH, value = ADB_OPTIONAL_TITLE)
        
        except Exception as e:
            logger.info(e)
            return None
        
        
    def extract_version_from_file_name(self, file_name: str) -> str:
        start = file_name.find("Upd") + 3
        end = file_name.rfind(".")
        return file_name[start:end]
    
    
    # 2300820053 -> 23.008.20053
    def version_with_dot(self, version: str) -> str:
        first = version[:3]
        second = version[3:6]
        third = version[6:]
        return first + "." + second + "." + third