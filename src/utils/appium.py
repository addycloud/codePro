#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from appium import webdriver
# driver = webdriver.Remomte('appnium程序的地址','一个字典，要获取设置的要求')
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
