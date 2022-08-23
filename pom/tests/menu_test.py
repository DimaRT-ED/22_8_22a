from pom.pages.home_page import HomePage
from selenium import webdriver



def zorconnectionbtn_test(dr : webdriver ):
    homepage = HomePage(dr)
    homepage.go_to_zor_conn()
    print(dr.title)


def odotbtn_test(dr : webdriver ):
    homepage = HomePage(dr)
    homepage.go_to_odot()
    print(dr.title)
