#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime


class DateTimeTool:
    @classmethod
    def get_now_yearTime(cls, format='%Y-%m-%d %H:%M:%S'):
        return datetime.datetime.now().strftime(format)

    @classmethod
    def get_now_date(cls, format='%Y-%m-%d'):
        return datetime.date.today().strftime(format)

    @classmethod
    def get_now_secondTime(cls,format='%H:%M:%S'):
        return datetime.datetime.now().strftime(format)