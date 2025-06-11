#Method 1:
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    result = []
    for i in range(len(employees)):
        eid = employees['employee_id'][i]
        ename = employees['name'][i]
        esal = employees['salary'][i]

        if eid % 2 == 1 and ename[0] != 'M':
            bonus = esal
        else:
            bonus = 0
        result.append([eid,bonus])
    return pd.DataFrame(result, columns = ['employee_id','bonus']).sort_values(['employee_id'])

#Method 2:

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    condition = (employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M'))
    employees['bonus'] = employees['salary'].where(condition,0)
    return employees[['employee_id','bonus']].sort_values(by = ['employee_id'])