from yahoo.helper_functions import share

print('START +')
my_share = share.Share('MSFT')
symbol_data = None

symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY,
                                      10,
                                      share.FREQUENCY_TYPE_MINUTE,
                                      5)


print('END +')
