from selenium.webdriver.common.by import By


class LoginPageLocators(object):

    LOGIN_FIELD = (By.ID, "txtUserID")
    PASSWORD_FIELD = (By.ID, "txtPassword")
    LOGIN_BUTTON = (By.ID, "sub")


class MainFrameLocators(object):

    CREATE_LINK = (By.XPATH, "//a[text() = 'Создать']")
    NEW_LIMIT = (By.XPATH, "//li[text()]//span[text() = 'Новый лимит (сделка вне лимита)']")


class MiddleFrameLocators(object):

    COMPANY_FIELD = (By.XPATH, "//div//input[@id='PartySearchTin']")
    FIND_BUTTON = (By.XPATH, "//button[@name = 'PreLoanPartySearch_pyWorkPage.MvcPages.PartyComList(1)_4']")
    POLE_CHOOSE = (By.XPATH, "//span[text()='Поле']")
    SELECT_BUTTON = (By.XPATH, "//button[text() ='  Выбрать ']")
    SUMMARY_INFO = (By.XPATH, "//h3[text() = 'Общая информация']")
    OBJECT_TYPE_SELECTOR = (By.XPATH, "//select[@id='CcdTypeId']")
    LIMIT_TYPE_SELECTOR = (By.XPATH, "//select[@id='LimitTypeId']")
    PLANNING_DATE = (By.XPATH, "//input[@id='CreditCommitteeDateEstimate']")
    OFFICE_SELECTOR = (By.XPATH, "//select[@id='AuthorizedBodyId']")
    FILIAL_SELECTOR = (By.XPATH, "//select[@id='LoanDivisionId']")
    NEXT_STAGE = (By.XPATH, "//select[@id='NextStage']")
    COMPLETE_BUTTON = (By.XPATH, "//img[@alt='Выполнить']")
