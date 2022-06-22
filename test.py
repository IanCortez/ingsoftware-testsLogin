from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
driver.get("http://localhost:8080/login")


class Testing(unittest.TestCase):
	def testValidLogin(self):
		user = driver.find_element(By.NAME, "user")
		user.clear()

		pas = driver.find_element(By.NAME, 'pass')
		pas.clear()

		user.send_keys('trucos@gmail.com')
		time.sleep(2)
		pas.send_keys('abcdef')

		user.submit()
		time.sleep(1)

		res = driver.find_element(By.ID, 'loginstatus')
		self.assertTrue("Signed in" == res.text)
		driver.refresh()



	def testInvalidLogin(self):
		user = driver.find_element(By.NAME, "user")
		pas = driver.find_element(By.NAME, 'pass')

		user.clear()
		user.send_keys('trucos1')
		time.sleep(2)
		pas.send_keys('a')

		user.submit()
		time.sleep(1)

		res = driver.find_element(By.ID, 'loginstatus')
		self.assertTrue("Not signed in" == res.text)
		driver.refresh()


	def testBlankLoginPass(self):
		user = driver.find_element(By.NAME, 'user')

		user.send_keys('trucos1')
		time.sleep(2)

		user.submit()
		time.sleep(1)

		res = driver.find_element(By.ID, 'loginstatus')
		self.assertTrue("Not signed in" == res.text)


	def testBlankLoginUser(self):
		pas = driver.find_element(By.NAME, 'pass')

		pas.send_keys('a')
		time.sleep(2)

		pas.submit()
		time.sleep(1)

		res = driver.find_element(By.ID, 'loginstatus')
		self.assertTrue("Not signed in" == res.text)



if __name__ == '__main__':
	unittest.main()


print("tests listos")
driver.close()