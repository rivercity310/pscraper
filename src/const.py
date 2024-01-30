import logging
import sys
from pathlib import Path


# Type
ENC_TYPE = "utf8"


# DOM STRINGS
CVE_STR = r"CVE-\d+-\d+"
CVE_ID = r"^cve"
KB_STR = r"^KB\\d{7}"
PF_DOWNLOAD = "//*[@id=\"downloadFiles\"]"
TS_HEADER = "page-header"      # Title_and_Summary Header ID
TS_SUMMARY = "bkmk_summary"    # Title_and_Summary Summary ID


# Folder Path
BIN_PATH = Path.cwd().parent / "bin"                      
SETTINGS_PATH = BIN_PATH / "settings"
EXE_PATH = BIN_PATH / "exe"
DATA_PATH = BIN_PATH / "data"
LOG_PATH = BIN_PATH / "logs"
PATCH_FILE_PATH = BIN_PATH / "patchfiles"
DOTNET_FILE_PATH = PATCH_FILE_PATH / "dotnet"
DOTNET_CAB_PATH = DOTNET_FILE_PATH / "cabs"


# Src Path
CWD = Path.cwd().parent
SRC_PATH = CWD / "src"
CRAWLER_PATH = SRC_PATH / "crawler"
REGISTER_PATH = SRC_PATH / "register"
VALIDATOR_PATH = SRC_PATH / "validator"
FUNCS_PATH = SRC_PATH / "funcs"
UTILS_PATH = SRC_PATH / "utils"
FILE_HANDLER_PATH = SRC_PATH / "filehandler"


# File Path
LOG_FILE_PATH = LOG_PATH / "log.txt"                    # 프로그램 실행 중 로깅을 위한 파일
META_FILE_PATH = SETTINGS_PATH / "meta.yaml"            # 프로그램에서 사용되는 메타 정보를 한 곳에서 관리하기 위한 파일
EXCEL_FILE_PATH = EXE_PATH / "patch.xlsx"               # 원본 엑셀 파일 (복사해서 사용)
CHROME_DRIVER_PATH = EXE_PATH / "chromedriver.exe"      # 크롤링을 위한 크롬드라이버 파일
RESULT_FILE_PATH = DATA_PATH / "result.json"            # 수집 결과를 저장하는 파일 (크롤링 이후 생성)
MAPPER_FILE_PATH = DATA_PATH / "mapper.txt"             # 엑셀 파일의 제목과 실제 버전의 키를 매핑해주기 위한 파일 (EXCEL_KEY 파일로부터 생성됨)


# 프로그램 시작 전 모듈 import를 위한 경로 리스트
REQUIRED_BEFORE_STARTED = [META_FILE_PATH, EXCEL_FILE_PATH, CHROME_DRIVER_PATH]

# 각 모듈의 루트 경로 모음 (sys 경로에 등록)
SYS_APPENDED_PATHS = [CRAWLER_PATH, REGISTER_PATH, VALIDATOR_PATH, UTILS_PATH, FILE_HANDLER_PATH]

# 대체해야 하는 특정 유니코드 모음 리스트
UNREQUIRED_UNICODES = [{u'\u2013': '-'}] 


# Format
ERR_STR_FORMAT = "[ERR] CAN'T FIND OBJECT {}"
DOTNET_KB_FORMAT = "KB{}"
DOTNET_BULLETIN_FORMAT = "MS-KB{}"
DOTNET_BULLETIN_URL_FORMAT = "https://support.microsoft.com/{}/help/{}"
DOTNET_NATIONS_LIST = ['en-us', 'ja-jp', 'ko-kr', 'zh-cn']


# Logging
logger = logging
stdout_handler = logger.StreamHandler(stream = sys.stdout)                # 콘솔 출력을 위한 핸들러
file_handler = logger.FileHandler(LOG_FILE_PATH, encoding = ENC_TYPE)     # 파일 출력을 위한 핸들러
logger.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s %(levelname)s: [%(module)s.%(funcName)s] %(message)s',
    datefmt = '[%m/%d/%Y %I:%M:%S] %p',
    handlers = [stdout_handler, file_handler]
)
