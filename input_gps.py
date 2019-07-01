#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

from mock_key import MockKey

lat = '-6.116263'
lng = '106.91201'

if len(sys.argv) >= 2:
    location = sys.argv[1].split(',')
    lat = location[0]
    lng = location[1]

MockKey.click_cursor_move_end()
MockKey.click('KEYCODE_DEL', '$(printf "KEYCODE_DEL %.0s" {1..20})', True)
MockKey.input(lat)

MockKey.click_tab()

MockKey.click_cursor_move_end()
MockKey.click('KEYCODE_DEL', '$(printf "KEYCODE_DEL %.0s" {1..20})', True)
MockKey.input(lng)
