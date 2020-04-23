from FrameWorkUtils.Utilities import Utils
import requests
import pandas
import json
import allure
class Delete(Utils):

    @allure.step("Delete the order created for the customer")
    def delete_Order(self,OrderID):

        environment=self.getConfigData("ENVIRONMENT",'ENV')
        baseurl=self.getConfigData(environment+"_ENVIRONMENT",environment+"_BASE_URL")
        resources=str(self.getConfigData("RESOURCES","DELETE_ORDER")).replace("{QUERY}",OrderID)
        response=requests.delete(url=baseurl+resources)
        assert response.status_code==200,"Validate the repsonse code for the Delete request while deleting the order"






