#!/usr/bin/env python

from datetime import datetime

print datetime.utcnow().strftime('%Y-%m-%d %H-%M-%S,%f')[:-3]
