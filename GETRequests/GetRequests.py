from FrameWorkUtils.Utilities import Utils
import requests
import pandas
import json
import allure
class Get(Utils):

    @allure.step("Fetch All The Categories from the System")
    def get_All_Categories(self):

        environment=self.getConfigData("ENVIRONMENT",'ENV')
        baseurl=self.getConfigData(environment+"_ENVIRONMENT",environment+"_BASE_URL")
        resources=self.getConfigData("RESOURCES","CATEGORIES")
        response=requests.get(url=baseurl+resources)
        assert response.status_code==200,"Validate the repsonse code for the get request while getting the categories"

        jsonObject=json.loads(response.text)
        for category in jsonObject['categories']:

            try:
                print(category['name'])
            except Exception:
                print(Exception)

    @allure.step("Fetch All The Orders from the System")
    def get_All_Orders(self):

        environment = self.getConfigData("ENVIRONMENT", 'ENV')
        baseurl = self.getConfigData(environment + "_ENVIRONMENT", environment + "_BASE_URL")
        resources = self.getConfigData("RESOURCES", "ORDERS")
        response = requests.get(url=baseurl + resources)
        assert response.status_code == 200, "Validate the repsonse code for the get request while getting the Orders"

        jsonObject = json.loads(response.text)

        assert len(jsonObject['orders'])>0, "Validate if the orders are available in the system"
        orderUrl=""
        for order in jsonObject['orders']:

            if str(order['state'])=='created':
                orderUrl = order["order_url"]
                orderUrl = str(orderUrl)[str(orderUrl).rfind("/") + 1:]
                print(orderUrl)
                break
        return orderUrl









