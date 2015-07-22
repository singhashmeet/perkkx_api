def _make_filter(keys, dict):
    for key in keys:
        dict[key] = False

# Merchant filters
_msKeys = [
    '_id', 'company_name', 'corporate_address', 'cphone', 'saving',
    'cemail'
]
_mKeys = ['merchant_id']


merchant_filter_small = {}
_make_filter(_msKeys, merchant_filter_small)

merchant_filter = merchant_filter_small.copy()
_make_filter(_mKeys, merchant_filter)

# Deal filters
_dKeys = [
    '_id', 'saving'
]
deal_filter = {}
_make_filter(_dKeys, deal_filter)
