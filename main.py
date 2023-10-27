from utils.class_utils import load_sorted_operations
from utils.class_utils import get_date
from utils.class_utils import get_where_from
from utils.class_utils import get_where_to


for op in load_sorted_operations():
    print(get_date(op.get('date')), op.get('description'))
    print(f"{get_where_from(op.get('from', ''))} -> {get_where_to(op.get('to'))}")
    print(op.get('operationAmount').get('amount'), op.get('operationAmount').get('currency').get('name'))
    print()