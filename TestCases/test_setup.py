from FrameWorkUtils.Utilities import Utils
from GETRequests.GetRequests import Get
import allure


import pytest
import unittest

class test(Utils,unittest.TestCase):

     @pytest.mark.usefixtures('pre_and_post_activities')
     @allure.severity(allure.severity_level.CRITICAL)
     @allure.description("This Test cases Will fetch all the categories from the system, with the Get Request")
     def testsomething(self):
        get=Get()
        get.get_All_Categories()




