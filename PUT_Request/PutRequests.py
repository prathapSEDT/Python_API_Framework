from FrameWorkUtils.Utilities import Utils
import requests
import pandas
import json
import allure


class Put(Utils):

    @allure.step("Modify the Cutsomer with the ID :{0}")
    def updateCustomer(self, customerID):
        environment = self.getConfigData("ENVIRONMENT", 'ENV')
        baseurl = self.getConfigData(environment + "_ENVIRONMENT", environment + "_BASE_URL")
        resources = self.getConfigData("RESOURCES", "CREATE_CUSTOMER")  + customerID
        jsonfile = open("../Payloads/CreateCustomer.json")
        payload = json.load(jsonfile)

        payload["firstname"] = "ModifiedPrathap"
        payload["lastname"] = "ModfiedVeera"

        payload = json.dumps(payload, indent=4)

        headers = {"Content-Type": "application/json"}

        response = requests.put(url=baseurl + resources, headers=headers, data=payload)
        assert response.status_code == 200, "Validate the repsonse code for the put request while updating a customer"

        print(response.status_code)
        print(response.content)
