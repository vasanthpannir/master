emplst = ['ravi-sales-blr-1800',
          'guru-purchase-chn-18500',
          'raja-accts-hyd-1900',
          'mani-sales-tvm-1600',
          'hari-sales-blr-1800',
          'john-accts-blr-1900']

subtotal = {}
for elm in emplst:
    name,dept,loc,sal = elm.split('-')
    if dept in subtotal:
        subtotal[dept]+= sal
    else:
        subtotal[dept] = sal




        
