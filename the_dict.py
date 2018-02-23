#!/usr/bin/env python3
#  -*- coding:utf-8 -*-

d = {
    'zzc': 31,
    'zj': 23,
    'baby': 0
}
print('d[\'zzc\']=', d['zzc'])  # \转义符
print('d[\'zj\']=', d['zj'])
print('d.get(\'zzc\',-1)=', d.get('zzc', -1))
