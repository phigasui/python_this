#! /usr/bin/env python

import this


print("-------------------------------------------------------")
print(''.join(
    map(lambda x: this.d[x] if x in this.d.keys() else x, this.s)
))
