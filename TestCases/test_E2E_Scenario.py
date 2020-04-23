from FrameWorkUtils.Utilities import Utils
from POST_Request.PostRequests import Post
from PUT_Request.PutRequests import Put
from DELETERequest.DeleteRequests import Delete
from GETRequests.GetRequests import Get
import allure

import pytest
import unittest


class E2E_TestCase(Utils, unittest.TestCase):

    @pytest.mark.usefixtures('pre_and_post_activities')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("This Test cases Will create new customer on the system")
    def test_CreateCustomer(self):
        post = Post()
        customerid=post.createCustomer()

        put=Put()
        put.updateCustomer(customerid)

        orderID=post.createOrder(customerid)

        delete=Delete()
        delete.delete_Order(orderID)






