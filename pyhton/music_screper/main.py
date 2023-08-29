from selenium import webdriver

crome_driver_path ="/Users/thiteshubham09/atomprojects/chromedriver"
driver = webdriver.Chrome(executable_path=crome_driver_path)

driver.get("https://www.amazon.in/American-Tourister-AMT-SCH-03/dp/B07CGSJNML/ref=zg-bs_luggage_sccl_1/257-3280098-9422069?pd_rd_w=FvGfW&content-id=amzn1.sym.56cde3ad-3235-46d2-8a20-4773248e8b83&pf_rd_p=56cde3ad-3235-46d2-8a20-4773248e8b83&pf_rd_r=NG9GHK1NTXB53NJH1083&pd_rd_wg=11P7i&pd_rd_r=46bec922-cfde-4a08-982e-0")
price = driver.find_element(by="id",value="corePrice_desktop")

print(price.text[35:43])
driver.close()
driver.quit()