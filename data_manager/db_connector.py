from datetime import date
from .models import Country, Stock, DailyStockPrice



def create_stock(stock_obj):
    '''Create Stock record if doesn't exist 
    already in the Stock table
    (IN) stock_obj: (dict) containing all the fields
    (OUT) return: (int) Stock record ID OR Error object
    '''
    if isinstance(stock_obj, dict) and \
        not is_stock_exist(stock_obj.symbol):
        try:
            new_stock = Stock.objects.create(
                symbol = stock_obj.symbol,
                full_name = stock_obj.full_name,
                description = stock_obj.description,
                country = stock_obj.country,
                active = stock_obj.active
            )
            result = new_stock.id
        except Exception as e:
            result = e

    return result

def update_stock(key, **kwargs):
    '''Updates the stock only if already exist
    in the database
    (IN) key: (dict) Key -> Value for filtering the data
    (OUT) return: (.models.Stock) Object or False
    '''
    result = False
    if not isinstance(key, dict):
        return result

    if len(list(key.keys())) != 1:
        return result

    key_filter = list(key.keys())[0]
    value_filter = list(key.values())[0]

    stock_object = Stock.objects.filter(key_filter=value_filter)
    if not stock_object:
        return result

    model_fields = [field.name for field in list(Stock._meta.get_fields())]
    try:
        for key_upd, value_upd in kwargs.items():
            if key_upd in model_fields:
                setattr(stock_object, key_upd, value_upd)
        stock_object.save()
        result = True
    except Exception:
        pass
    return result

def is_stock_exist(stock_symbol):
    '''Check if given stock symbol 
    already has a record in the database
    (IN) stock_symbol: (string) complete abbreviation OR part of it
    (OUT) return: (bool) 'True' if the symbol is present in the database
    '''
    result = False
    try:
        Stock.objects.get(symbol__contains=stock_symbol)
        result = True
    except Exception:
        pass
    return result

def get_stock_by_symbol(stock_symbol):
    '''Get all the stocks which contain
    given symbol
    (IN) stock_symbol: (string) complete abbreviation OR part of it
    (OUT) return: (data_manager.models.Stock) return only ONE object
    '''
    result = None
    try:
        result = Stock.objects.get(symbol__contains=stock_symbol)
    except Exception:
        pass
    return result


