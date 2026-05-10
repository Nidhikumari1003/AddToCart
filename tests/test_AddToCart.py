import sys
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pages.login import *
from Pages.product import *

def test_AddToCart():
    password="AdNabuQA"
    productsearch="snowboard"
    validproduct="The Videographer Snowboard"
    logintopage(password)
    searchaddproduct(productsearch,validproduct)
    go_to_cart()
    cart_value_verification(validproduct)




