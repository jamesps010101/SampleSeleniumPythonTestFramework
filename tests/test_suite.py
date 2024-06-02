import unittest
from tests.login_test import LoginTest
from tests.inventory_test import InventoryTest
from tests.inventory_detail_test import InventoryDetailTest
from tests.cart_checkout_test import CartCheckoutTest

# load tests
login_tc = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
inventory_tc = unittest.TestLoader().loadTestsFromTestCase(InventoryTest)
inventory_detail_tc = unittest.TestLoader().loadTestsFromTestCase(InventoryDetailTest)
cartcheckout_tc = unittest.TestLoader().loadTestsFromTestCase(CartCheckoutTest)

# store tests in list
tests = [login_tc, inventory_tc, inventory_detail_tc, cartcheckout_tc]

# test suite
suite = unittest.TestSuite(tests)
unittest.TextTestRunner(verbosity=2).run(suite)
