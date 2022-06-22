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
		print("Valid login test")
		driver.refresh()
		user = driver.find_element(By.NAME, "user")
		pas = driver.find_element(By.NAME, 'pass')

		time.sleep(1)
		user.send_keys('trucos@gmail.com')
		time.sleep(2)
		pas.send_keys('abcdef')

		time.sleep(1)
		user.submit()
		time.sleep(1)

		res = driver.find_element(By.ID, 'loginstatus')
		self.assertTrue("Signed in" == res.text)


	def testInvalidUser(self):
		print("Invalid user test")
		driver.refresh()
		user = driver.find_element(By.NAME, "user")
		pas = driver.find_element(By.NAME, 'pass')

		time.sleep(1)
		user.send_keys('trucos1')
		time.sleep(2)
		pas.send_keys('abcdef')

		time.sleep(1)
		user.submit()
		time.sleep(1)

		res = driver.find_element(By.ID, 'loginstatus')
		self.assertTrue("Wrong user" == res.text)

	
	def testInvalidPass(self):
		print("Invalid password test")
		driver.refresh()
		user = driver.find_element(By.NAME, "user")
		pas = driver.find_element(By.NAME, 'pass')
		
		time.sleep(1)
		user.send_keys('trucos@gmail.com')
		time.sleep(2)
		pas.send_keys('a')

		time.sleep(1)
		user.submit()
		time.sleep(1)

		res = driver.find_element(By.ID, 'loginstatus')
		self.assertTrue("Wrong password" == res.text)


	def testBlankLoginPass(self):
		print("Missing password test")
		driver.refresh()
		user = driver.find_element(By.NAME, 'user')

		time.sleep(1)
		user.send_keys('trucos@gmail.com')
		time.sleep(2)

		user.submit()
		time.sleep(1)

		res = driver.find_element(By.ID, 'loginstatus')
		self.assertTrue("Missing credentials" == res.text)

	def testBlankLoginUser(self):
		print("Missing user test")
		driver.refresh()
		pas = driver.find_element(By.NAME, 'pass')

		time.sleep(1)
		pas.send_keys('a')
		time.sleep(2)

		pas.submit()
		time.sleep(1)

		res = driver.find_element(By.ID, 'loginstatus')
		self.assertTrue("Missing credentials" == res.text)



if __name__ == '__main__':
	unittest.main()


print("tests listos")
driver.close()