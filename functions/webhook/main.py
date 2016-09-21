# -*- coding: utf-8 -*-

# Sample webhook client for receiving a payload from Gogs to process the job. This currently works with
# an English OBS repo

from __future__ import print_function
from import convert

def handle(event, context):
    return convert(event, context)
