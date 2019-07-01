#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


class MockKey:
    def __init__(self):
        pass

    @staticmethod
    def input(text):
        os.system('adb shell input text ' + text)
        print('input text %s' % text)

    @staticmethod
    def get_touch_place(touchscreen=True, touch_pad=False, touch_navigation=False):
        # because default is touchscreen, so empty is equals to touchscreen
        touch = ''
        if touchscreen:
            touch = 'touchscreen'
        elif touch_pad:
            touch = 'touchpad'
        elif touch_navigation:
            touch = 'touchnavigation'
        return touch

    @staticmethod
    def tap(x, y, touchscreen=True, touch_pad=False, touch_navigation=False):
        touch_place = MockKey.get_touch_place(touchscreen, touch_pad, touch_navigation)

        os.system('adb shell input %s tap %d %d' % (touch_place, x, y))
        print('tap %s %d,%d' % (touch_place, x, y))

    @staticmethod
    def swipe(start_x, end_x, start_y, end_y, touchscreen=True, touch_pad=False, touch_navigation=False, duration=-1):
        touch_place = MockKey.get_touch_place(touchscreen, touch_pad, touch_navigation)

        if duration < 0:
            os.system('adb shell input %s swipe %d %d %d %d' % (touch_place, start_x, start_y, end_x, end_y))
            print('swipe %s %d,%d %d,%d' % (touch_place, start_x, end_x, start_y, end_y))
        else:
            os.system(
                'adb shell input %s swipe %d %d %d %d %d' % (touch_place, start_x, start_y, end_x, end_y, duration))
            print('swipe %s %d,%d %d,%d in %dms' % (touch_place, start_x, end_x, start_y, end_y, duration))

    @staticmethod
    def trackball_press():
        os.system('adb shell input trackball press')
        print('trackball press')

    @staticmethod
    def trackball_roll(x, y):
        os.system('adb shell input trackball roll %d %d' % (x, y))
        print('trackball roll %d,%d' % (x, y))

    @staticmethod
    def click(key_name, key_code, long_press=False):
        long_press_param = ''
        if long_press:
            long_press_param = '--longpress'
        os.system('adb shell input keyevent %s %s' % (long_press_param, key_code))
        print('click %s' % key_name)

    @staticmethod
    def click_phone_call(long_press=False):
        MockKey.click("phone call", '5', long_press)

    @staticmethod
    def click_phone_end_call(long_press=False):
        MockKey.click('phone end call', '6', long_press)

    @staticmethod
    def click_home(long_press=False):
        MockKey.click('home', '3', long_press)

    @staticmethod
    def click_menu(long_press=False):
        MockKey.click('menu', '82', long_press)

    @staticmethod
    def click_back(long_press=False):
        MockKey.click('back', '4', long_press)

    @staticmethod
    def click_search(long_press=False):
        MockKey.click('search', '84', long_press)

    @staticmethod
    def click_camera(long_press=False):
        MockKey.click('camera', '27', long_press)

    @staticmethod
    def click_camera_focus(long_press=False):
        MockKey.click('camera focus', '80', long_press)

    @staticmethod
    def click_power(long_press=False):
        MockKey.click('power', '26', long_press)

    @staticmethod
    def click_notification(long_press=False):
        MockKey.click('notification', '83', long_press)

    @staticmethod
    def click_microphone_mute(long_press=False):
        MockKey.click('microphone mute', '91', long_press)

    @staticmethod
    def click_volume_mute(long_press=False):
        MockKey.click('volume mute', '164', long_press)

    @staticmethod
    def click_volume_up(long_press=False):
        MockKey.click('volume up', '24', long_press)

    @staticmethod
    def click_volume_down(long_press=False):
        MockKey.click('volume down', '25', long_press)

    @staticmethod
    def click_enter(long_press=False):
        MockKey.click('enter', '66', long_press)

    @staticmethod
    def click_esc(long_press=False):
        MockKey.click('esc', '111', long_press)

    @staticmethod
    def click_dpad_center(long_press=False):
        MockKey.click('dpad center', '23', long_press)

    @staticmethod
    def click_dpad_up(long_press=False):
        MockKey.click('dpad up', '19', long_press)

    @staticmethod
    def click_dpad_down(long_press=False):
        MockKey.click('dpad down', '20', long_press)

    @staticmethod
    def click_dpad_left(long_press=False):
        MockKey.click('dpad left', '21', long_press)

    @staticmethod
    def click_dpad_right(long_press=False):
        MockKey.click('dpad right', '22', long_press)

    @staticmethod
    def click_cursor_move_start(long_press=False):
        MockKey.click('cursor move start', '122', long_press)

    @staticmethod
    def click_cursor_move_end(long_press=False):
        MockKey.click('cursor move end', '123', long_press)

    @staticmethod
    def click_page_up(long_press=False):
        MockKey.click('page up', '92', long_press)

    @staticmethod
    def click_page_down(long_press=False):
        MockKey.click('page down', '93', long_press)

    @staticmethod
    def click_del(long_press=False):
        MockKey.click('del', '67', long_press)

    @staticmethod
    def click_forward_del(long_press=False):
        MockKey.click('forward del', '112', long_press)

    @staticmethod
    def click_insert(long_press=False):
        MockKey.click('insert', '124', long_press)

    @staticmethod
    def click_tab(long_press=False):
        MockKey.click('tab', '61', long_press)

    @staticmethod
    def click_num_lock(long_press=False):
        MockKey.click('num lock', '143', long_press)

    @staticmethod
    def click_caps_lock(long_press=False):
        MockKey.click('caps lock', '115', long_press)

    @staticmethod
    def click_break_or_pause(long_press=False):
        MockKey.click('break or pause', '121', long_press)

    @staticmethod
    def click_scroll_lock(long_press=False):
        MockKey.click('scroll lock', '116', long_press)

    @staticmethod
    def click_zoom_in(long_press=False):
        MockKey.click('zoom in', '168', long_press)

    @staticmethod
    def click_zoom_out(long_press=False):
        MockKey.click('zoom out', '169', long_press)

    @staticmethod
    def click_alt_and_left(long_press=False):
        MockKey.click('alt and left', 'KEYCODE_ALT_LEFT', long_press)

    @staticmethod
    def click_alt_and_right(long_press=False):
        MockKey.click('alt and right', 'KEYCODE_ALT_RIGHT', long_press)

    @staticmethod
    def click_ctrl_and_left(long_press=False):
        MockKey.click('ctrl and left', 'KEYCODE_CTRL_LEFT', long_press)

    @staticmethod
    def click_ctrl_and_right(long_press=False):
        MockKey.click('ctrl and right', 'KEYCODE_CTRL_RIGHT', long_press)

    @staticmethod
    def click_shift_and_left(long_press=False):
        MockKey.click('shift and left', 'KEYCODE_SHIFT_LEFT', long_press)

    @staticmethod
    def click_shift_and_right(long_press=False):
        MockKey.click('shift and right', 'KEYCODE_SHIFT_RIGHT', long_press)

    @staticmethod
    def click_0(long_press=False):
        MockKey.click("0", '7', long_press)

    @staticmethod
    def click_1(long_press=False):
        MockKey.click('1', '8', long_press)

    @staticmethod
    def click_2(long_press=False):
        MockKey.click('2', '9', long_press)

    @staticmethod
    def click_3(long_press=False):
        MockKey.click('3', '10', long_press)

    @staticmethod
    def click_4(long_press=False):
        MockKey.click('4', '11', long_press)

    @staticmethod
    def click_5(long_press=False):
        MockKey.click('5', '12', long_press)

    @staticmethod
    def click_6(long_press=False):
        MockKey.click('6', '13', long_press)

    @staticmethod
    def click_7(long_press=False):
        MockKey.click('7', '14', long_press)

    @staticmethod
    def click_8(long_press=False):
        MockKey.click('8', '15', long_press)

    @staticmethod
    def click_9(long_press=False):
        MockKey.click('9', '16', long_press)

    @staticmethod
    def click_a(long_press=False):
        MockKey.click('A', '29', long_press)

    @staticmethod
    def click_b(long_press=False):
        MockKey.click('B', '30', long_press)

    @staticmethod
    def click_c(long_press=False):
        MockKey.click('C', '31', long_press)

    @staticmethod
    def click_d(long_press=False):
        MockKey.click('D', '32', long_press)

    @staticmethod
    def click_e(long_press=False):
        MockKey.click('D', '33', long_press)

    @staticmethod
    def click_f(long_press=False):
        MockKey.click('F', '34', long_press)

    @staticmethod
    def click_g(long_press=False):
        MockKey.click('G', '35', long_press)

    @staticmethod
    def click_h(long_press=False):
        MockKey.click('H', '36', long_press)

    @staticmethod
    def click_i(long_press=False):
        MockKey.click('I', '37', long_press)

    @staticmethod
    def click_j(long_press=False):
        MockKey.click('J', '38', long_press)

    @staticmethod
    def click_k(long_press=False):
        MockKey.click('K', '39', long_press)

    @staticmethod
    def click_l(long_press=False):
        MockKey.click('L', '40', long_press)

    @staticmethod
    def click_m(long_press=False):
        MockKey.click('M', '41', long_press)

    @staticmethod
    def click_n(long_press=False):
        MockKey.click('N', '42', long_press)

    @staticmethod
    def click_o(long_press=False):
        MockKey.click('O', '43', long_press)

    @staticmethod
    def click_p(long_press=False):
        MockKey.click('P', '44', long_press)

    @staticmethod
    def click_q(long_press=False):
        MockKey.click('Q', '45', long_press)

    @staticmethod
    def click_r(long_press=False):
        MockKey.click('R', '46', long_press)

    @staticmethod
    def click_s(long_press=False):
        MockKey.click('S', '47', long_press)

    @staticmethod
    def click_t(long_press=False):
        MockKey.click('T', '48', long_press)

    @staticmethod
    def click_u(long_press=False):
        MockKey.click('U', '49', long_press)

    @staticmethod
    def click_v(long_press=False):
        MockKey.click('V', '50', long_press)

    @staticmethod
    def click_w(long_press=False):
        MockKey.click('W', '51', long_press)

    @staticmethod
    def click_x(long_press=False):
        MockKey.click('X', '52', long_press)

    @staticmethod
    def click_y(long_press=False):
        MockKey.click('Y', '53', long_press)

    @staticmethod
    def click_z(long_press=False):
        MockKey.click('Z', '54', long_press)

    @staticmethod
    def click_plus(long_press=False):
        MockKey.click('+', 'KEYCODE_PLUS', long_press)

    @staticmethod
    def click_minus(long_press=False):
        MockKey.click('-', 'KEYCODE_MINUS', long_press)

    @staticmethod
    def click_star(long_press=False):
        MockKey.click('*', 'KEYCODE_STAR', long_press)

    @staticmethod
    def click_slash(long_press=False):
        MockKey.click('/', 'KEYCODE_SLASH', long_press)

    @staticmethod
    def click_equals(long_press=False):
        MockKey.click('=', 'KEYCODE_EQUALS', long_press)

    @staticmethod
    def click_at(long_press=False):
        MockKey.click("@", 'KEYCODE_AT', long_press)

    @staticmethod
    def click_pound(long_press=False):
        MockKey.click('#', 'KEYCODE_POUND', long_press)

    @staticmethod
    def click_apostrophe(long_press=False):
        MockKey.click('\'', 'KEYCODE_APOSTROPHE', long_press)

    @staticmethod
    def click_backslash(long_press=False):
        MockKey.click('\\', 'KEYCODE_BACKSLASH', long_press)

    @staticmethod
    def click_comma(long_press=False):
        MockKey.click(',', 'KEYCODE_COMMA', long_press)

    @staticmethod
    def click_period(long_press=False):
        MockKey.click('.', 'KEYCODE_PERIOD', long_press)

    @staticmethod
    def click_left_bracket(long_press=False):
        MockKey.click('[', 'KEYCODE_LEFT_BRACKET', long_press)

    @staticmethod
    def click_right_bracket(long_press=False):
        MockKey.click(']', 'KEYCODE_RIGHT_BRACKET', long_press)

    @staticmethod
    def click_semicolon(long_press=False):
        MockKey.click(';', 'KEYCODE_SEMICOLON', long_press)

    @staticmethod
    def click_grave(long_press=False):
        MockKey.click('`', 'KEYCODE_GRAVE', long_press)

    @staticmethod
    def click_space(long_press=False):
        MockKey.click('space', 'KEYCODE_SPACE', long_press)

    @staticmethod
    def click_numpad_0(long_press=False):
        MockKey.click('numpad 0', 'KEYCODE_NUMPAD_0', long_press)

    @staticmethod
    def click_numpad_1(long_press=False):
        MockKey.click('numpad 1', 'KEYCODE_NUMPAD_1', long_press)

    @staticmethod
    def click_numpad_2(long_press=False):
        MockKey.click('numpad 2', 'KEYCODE_NUMPAD_2', long_press)

    @staticmethod
    def click_numpad_3(long_press=False):
        MockKey.click('numpad 3', 'KEYCODE_NUMPAD_3', long_press)

    @staticmethod
    def click_numpad_4(long_press=False):
        MockKey.click('numpad 4', 'KEYCODE_NUMPAD_4', long_press)

    @staticmethod
    def click_numpad_5(long_press=False):
        MockKey.click('numpad 5', 'KEYCODE_NUMPAD_5', long_press)

    @staticmethod
    def click_numpad_6(long_press=False):
        MockKey.click('numpad 6', 'KEYCODE_NUMPAD_6', long_press)

    @staticmethod
    def click_numpad_7(long_press=False):
        MockKey.click('numpad 7', 'KEYCODE_NUMPAD_7', long_press)

    @staticmethod
    def click_numpad_8(long_press=False):
        MockKey.click('numpad 8', 'KEYCODE_NUMPAD_8', long_press)

    @staticmethod
    def click_numpad_9(long_press=False):
        MockKey.click('numpad 9', 'KEYCODE_NUMPAD_9', long_press)

    @staticmethod
    def click_numpad_add(long_press=False):
        MockKey.click('numpad +', 'KEYCODE_NUMPAD_ADD', long_press)

    @staticmethod
    def click_numpad_subtract(long_press=False):
        MockKey.click('numpad -', 'KEYCODE_NUMPAD_SUBTRACT', long_press)

    @staticmethod
    def click_numpad_multiply(long_press=False):
        MockKey.click('numpad *', 'KEYCODE_NUMPAD_MULTIPLY', long_press)

    @staticmethod
    def click_numpad_divide(long_press=False):
        MockKey.click('numpad /', 'KEYCODE_NUMPAD_DIVIDE', long_press)

    @staticmethod
    def click_numpad_equals(long_press=False):
        MockKey.click('numpad =', 'KEYCODE_NUMPAD_EQUALS', long_press)

    @staticmethod
    def click_numpad_comma(long_press=False):
        MockKey.click('numpad ,', 'KEYCODE_NUMPAD_COMMA', long_press)

    @staticmethod
    def click_numpad_dot(long_press=False):
        MockKey.click('numpad .', 'KEYCODE_NUMPAD_DOT', long_press)

    @staticmethod
    def click_numpad_left_paren(long_press=False):
        MockKey.click('numpad (', 'KEYCODE_NUMPAD_LEFT_PAREN', long_press)

    @staticmethod
    def click_numpad_right_paren(long_press=False):
        MockKey.click('numpad )', 'KEYCODE_NUMPAD_RIGHT_PAREN', long_press)

    @staticmethod
    def click_numpad_enter(long_press=False):
        MockKey.click('numpad enter', 'KEYCODE_NUMPAD_ENTER', long_press)

    @staticmethod
    def click_f1(long_press=False):
        MockKey.click('f1', 'KEYCODE_F1', long_press)

    @staticmethod
    def click_f2(long_press=False):
        MockKey.click('f2', 'KEYCODE_F2', long_press)

    @staticmethod
    def click_f3(long_press=False):
        MockKey.click('f3', 'KEYCODE_F3', long_press)

    @staticmethod
    def click_f4(long_press=False):
        MockKey.click('f4', 'KEYCODE_F4', long_press)

    @staticmethod
    def click_f5(long_press=False):
        MockKey.click('f5', 'KEYCODE_F5', long_press)

    @staticmethod
    def click_f6(long_press=False):
        MockKey.click('f6', 'KEYCODE_F6', long_press)

    @staticmethod
    def click_f7(long_press=False):
        MockKey.click('f7', 'KEYCODE_F7', long_press)

    @staticmethod
    def click_f8(long_press=False):
        MockKey.click('f8', 'KEYCODE_F8', long_press)

    @staticmethod
    def click_f9(long_press=False):
        MockKey.click('f9', 'KEYCODE_F9', long_press)

    @staticmethod
    def click_f10(long_press=False):
        MockKey.click('f10', 'KEYCODE_F10', long_press)

    @staticmethod
    def click_f11(long_press=False):
        MockKey.click("f11", 'KEYCODE_F11', long_press)

    @staticmethod
    def click_f12(long_press=False):
        MockKey.click('f12', 'KEYCODE_F12', long_press)

    @staticmethod
    def click_media_play(long_press=False):
        MockKey.click('media play', 'KEYCODE_MEDIA_PLAY', long_press)

    @staticmethod
    def click_media_stop(long_press=False):
        MockKey.click('media stop', 'KEYCODE_MEDIA_STOP', long_press)

    @staticmethod
    def click_media_pause(long_press=False):
        MockKey.click('media pause', 'KEYCODE_MEDIA_PAUSE', long_press)

    @staticmethod
    def click_media_play_pause(long_press=False):
        MockKey.click('media play/pause', 'KEYCODE_MEDIA_PLAY_PAUSE', long_press)

    @staticmethod
    def click_media_fast_forward(long_press=False):
        MockKey.click('media fast forward', 'KEYCODE_MEDIA_FAST_FORWARD', long_press)

    @staticmethod
    def click_media_rewind(long_press=False):
        MockKey.click('media rewind', 'KEYCODE_MEDIA_REWIND', long_press)

    @staticmethod
    def click_media_next(long_press=False):
        MockKey.click('media next', 'KEYCODE_MEDIA_NEXT', long_press)

    @staticmethod
    def click_media_previous(long_press=False):
        MockKey.click('media previous', 'KEYCODE_MEDIA_PREVIOUS', long_press)

    @staticmethod
    def click_media_close(long_press=False):
        MockKey.click('media close', 'KEYCODE_MEDIA_CLOSE', long_press)

    @staticmethod
    def click_media_eject(long_press=False):
        MockKey.click('media eject', 'KEYCODE_MEDIA_EJECT', long_press)

    @staticmethod
    def click_media_record(long_press=False):
        MockKey.click('media record', 'KEYCODE_MEDIA_RECORD', long_press)

    @staticmethod
    def click_button_1(long_press=False):
        MockKey.click('button 1', 'KEYCODE_BUTTON_1', long_press)

    @staticmethod
    def click_button_2(long_press=False):
        MockKey.click('button 2', 'KEYCODE_BUTTON_2', long_press)

    @staticmethod
    def click_button_3(long_press=False):
        MockKey.click('button 3', 'KEYCODE_BUTTON_3', long_press)

    @staticmethod
    def click_button_4(long_press=False):
        MockKey.click('button 4', 'KEYCODE_BUTTON_4', long_press)

    @staticmethod
    def click_button_5(long_press=False):
        MockKey.click('button 5', 'KEYCODE_BUTTON_5', long_press)

    @staticmethod
    def click_button_6(long_press=False):
        MockKey.click('button 6', 'KEYCODE_BUTTON_6', long_press)

    @staticmethod
    def click_button_7(long_press=False):
        MockKey.click('button 7', 'KEYCODE_BUTTON_7', long_press)

    @staticmethod
    def click_button_8(long_press=False):
        MockKey.click('button 8', 'KEYCODE_BUTTON_8', long_press)

    @staticmethod
    def click_button_9(long_press=False):
        MockKey.click('button 9', 'KEYCODE_BUTTON_9', long_press)

    @staticmethod
    def click_button_10(long_press=False):
        MockKey.click('button 10', 'KEYCODE_BUTTON_10', long_press)

    @staticmethod
    def click_button_11(long_press=False):
        MockKey.click('button 11', 'KEYCODE_BUTTON_11', long_press)

    @staticmethod
    def click_button_12(long_press=False):
        MockKey.click('button 12', 'KEYCODE_BUTTON_12', long_press)

    @staticmethod
    def click_button_13(long_press=False):
        MockKey.click('button 13', 'KEYCODE_BUTTON_13', long_press)

    @staticmethod
    def click_button_14(long_press=False):
        MockKey.click('button 14', 'KEYCODE_BUTTON_14', long_press)

    @staticmethod
    def click_button_15(long_press=False):
        MockKey.click('button 15', 'KEYCODE_BUTTON_15', long_press)

    @staticmethod
    def click_button_16(long_press=False):
        MockKey.click('button 16', 'KEYCODE_BUTTON_16', long_press)

    @staticmethod
    def click_button_a(long_press=False):
        MockKey.click('button A', 'KEYCODE_BUTTON_A', long_press)

    @staticmethod
    def click_button_b(long_press=False):
        MockKey.click('button B', 'KEYCODE_BUTTON_B', long_press)

    @staticmethod
    def click_button_c(long_press=False):
        MockKey.click('button C', 'KEYCODE_BUTTON_C', long_press)

    @staticmethod
    def click_button_x(long_press=False):
        MockKey.click('button X', 'KEYCODE_BUTTON_X', long_press)

    @staticmethod
    def click_button_y(long_press=False):
        MockKey.click('button Y', 'KEYCODE_BUTTON_Y', long_press)

    @staticmethod
    def click_button_z(long_press=False):
        MockKey.click('button Z', 'KEYCODE_BUTTON_Z', long_press)

    @staticmethod
    def click_button_l1(long_press=False):
        MockKey.click('button L1', 'KEYCODE_BUTTON_L1', long_press)

    @staticmethod
    def click_button_l2(long_press=False):
        MockKey.click('button L2', 'KEYCODE_BUTTON_L2', long_press)

    @staticmethod
    def click_button_r1(long_press=False):
        MockKey.click('button R1', 'KEYCODE_BUTTON_R1', long_press)

    @staticmethod
    def click_button_r2(long_press=False):
        MockKey.click('button R2', 'KEYCODE_BUTTON_R2', long_press)

    @staticmethod
    def click_button_mode(long_press=False):
        MockKey.click('button Mode', 'KEYCODE_BUTTON_MODE', long_press)

    @staticmethod
    def click_button_select(long_press=False):
        MockKey.click('button Select', 'KEYCODE_BUTTON_SELECT', long_press)

    @staticmethod
    def click_button_start(long_press=False):
        MockKey.click('button Start', 'KEYCODE_BUTTON_START', long_press)

    @staticmethod
    def click_button_thumb_l(long_press=False):
        MockKey.click('button left thumb', 'KEYCODE_BUTTON_THUMBL', long_press)

    @staticmethod
    def click_button_thumb_r(long_press=False):
        MockKey.click('button right thumb', 'KEYCODE_BUTTON_THUMBR', long_press)

    @staticmethod
    def click_bookmark(long_press=False):
        MockKey.click('bookmark', 'KEYCODE_BOOKMARK', long_press)

    @staticmethod
    def click_app_switch(long_press=False):
        MockKey.click('app switch', 'KEYCODE_APP_SWITCH', long_press)

    @staticmethod
    def click_avr_input(long_press=False):
        MockKey.click('A/V receiver input', 'KEYCODE_AVR_INPUT', long_press)

    @staticmethod
    def click_avr_power(long_press=False):
        MockKey.click('A/V receiver power', 'KEYCODE_AVR_POWER', long_press)

    @staticmethod
    def click_channel_down(long_press=False):
        MockKey.click('channel down', 'KEYCODE_CHANNEL_DOWN', long_press)

    @staticmethod
    def click_channel_up(long_press=False):
        MockKey.click('channel up', 'KEYCODE_CHANNEL_UP', long_press)

    @staticmethod
    def click_clear(long_press=False):
        MockKey.click('clear', 'KEYCODE_CLEAR', long_press)

    @staticmethod
    def click_explorer(long_press=False):
        MockKey.click('explorer', 'KEYCODE_EXPLORER', long_press)

    @staticmethod
    def click_forward(long_press=False):
        MockKey.click('forward', 'KEYCODE_FORWARD', long_press)

    @staticmethod
    def click_function(long_press=False):
        MockKey.click('function', 'KEYCODE_FUNCTION', long_press)

    @staticmethod
    def click_settings(long_press=False):
        MockKey.click('settings', 'KEYCODE_SETTINGS', long_press)

    @staticmethod
    def click_soft_left(long_press=False):
        MockKey.click('soft left', 'KEYCODE_SOFT_LEFT', long_press)

    @staticmethod
    def click_soft_right(long_press=False):
        MockKey.click('soft right', 'KEYCODE_SOFT_RIGHT', long_press)

    @staticmethod
    def click_switch_charset(long_press=False):
        MockKey.click('switch charset', 'KEYCODE_SWITCH_CHARSET', long_press)

    @staticmethod
    def click_symbol(long_press=False):
        MockKey.click('symbol', 'KEYCODE_SYM', long_press)

    @staticmethod
    def click_system_request_print_screen(long_press=False):
        MockKey.click('system request / print screen', 'KEYCODE_SYSRQ', long_press)

    @staticmethod
    def click_tv(long_press=False):
        MockKey.click('TV', 'KEYCODE_TV', long_press)

    @staticmethod
    def click_tv_input(long_press=False):
        MockKey.click('TV input', 'KEYCODE_TV_INPUT', long_press)

    @staticmethod
    def click_tv_power(long_press=False):
        MockKey.click('TV power', 'KEYCODE_TV_POWER', long_press)

    @staticmethod
    def click_window(long_press=False):
        MockKey.click('window', 'KEYCODE_WINDOW', long_press)

    @staticmethod
    def click_unknown(long_press=False):
        MockKey.click('unknown', 'KEYCODE_UNKNOWN', long_press)
