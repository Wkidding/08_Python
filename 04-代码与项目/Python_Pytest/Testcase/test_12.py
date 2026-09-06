# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/12 15:26
@File   ：test_012
@IDE    ：PyCharm
=================================================="""
import logging

logger = logging.getLogger(__name__)

def test_case_01():
    logger.info("断言1==1")
    assert 1 == 1
