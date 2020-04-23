from configparser import ConfigParser
import pytest
import allure
import os

class Utils():

    @pytest.fixture(scope='session')
    def pre_and_post_activities(self):

        self.load_ConfigFile()
        yield

    @allure.step("Loading Config file")
    def load_ConfigFile(self):
        print("File path Exist+"+str(os.path.exists(os.getcwd()+"\\Configuration\\Environment.cnf")))
        file=os.getcwd()+"\\Configuration\\Environment.cnf"
        global config
        config=ConfigParser()
        #config.read("../Environment.cnf")
        config.read(file)
        print("**********Reading config file***************")
    @allure.step("Get Data from the section : {0} for the field : {1} from the config file")
    def getConfigData(self,section,property):
        print("*****************************************************")
        return config.get(section,property)







