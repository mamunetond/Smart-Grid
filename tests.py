from django.test import TestCase,LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time

class MapView(StaticLiveServerTestCase):
  	
	def setUp(self):
		self.browser = webdriver.Chrome('/Users/julianrojasgallego/Desktop/ManageEV_Back/Smart-Grid/chromedriver')
		# try driver = webdriver.Chrome('./chromedriver') with the driver in the project folder if you cant set to path
	
	def tearDown(self):
		self.browser.close()
	
	def test_no_projects_alert_is_displayed(self):
		self.browser.get('http://localhost:3000/map')

		#alert = self.browser.find_element_by_id('destination')

		self.assertEquals(
			self.browser.find_element_by_tag_name('h3') ,
			""
		)
		
		# try driver.get(self.live_server_url) if driver.get('http://127.0.0.1:8000/') does not work
		time.sleep(3)
		
		assert "destination" in driver.find_element(By.ID, "destination")
# Create your tests here.
