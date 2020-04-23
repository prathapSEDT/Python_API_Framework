from FrameWorkUtils.Utilities import Utils
import requests
import pandas
import json
import allure


class Post(Utils):

    @allure.step("Create a new Customer")
    def createCustomer(self):

        environment = self.getConfigData("ENVIRONMENT", 'ENV')
        baseurl = self.getConfigData(environment + "_ENVIRONMENT", environment + "_BASE_URL")
        resources = self.getConfigData("RESOURCES", "CREATE_CUSTOMER")
        jsonfile = open("../Payloads/CreateCustomer.json")
        payload = json.load(jsonfile)

        payload["firstname"] = "Prathap"
        payload["lastname"] = "Veera"

        payload=json.dumps(payload,indent=4)


        headers = {"Content-Type": "application/json"}


        response = requests.post(url=baseurl + resources,headers=headers,data=payload)
        #assert response.status_code == 201, "Validate the repsonse code for the psot request while creating a customer"

        print(response.status_code)
        responseJson=json.loads(response.text)
        custommerID=responseJson['customer_url']
        print(str(custommerID)[str(custommerID).rfind("/")+1:])

        return str(custommerID)[str(custommerID).rfind("/")+1:]

    @allure.step("Create a new Order :{0}")
    def createOrder(self,OrderID):
        environment = self.getConfigData("ENVIRONMENT", 'ENV')
        baseurl = self.getConfigData(environment + "_ENVIRONMENT", environment + "_BASE_URL")
        resources = str(self.getConfigData("RESOURCES", "CREATE_ORDER")).replace("{QUERY}",OrderID)
        headers = {"Content-Type": "application/json"}

        response = requests.post(url=baseurl + resources, headers=headers)
        # assert response.status_code == 201, "Validate the repsonse code for the psot request while creating a customer"

        print(response.status_code)
        responseJson = json.loads(response.text)
        custommerID = responseJson['items_url']
        import  re
        print(re.sub("[^0-9]","",str(custommerID)))

        return re.sub("[^0-9]","",str(custommerID))



