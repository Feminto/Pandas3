# Method 1
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    result = []
    for i in range(len(users)):
        name = users['name'][i]
        uid = users['user_id'][i]

        new_name = name[0].upper() + name[1:].lower()

        result.append([uid,new_name])
    return pd.DataFrame(result, columns = ['user_id','name']).sort_values(['user_id'])

# # Method 2

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    result = []
    for i in range(len(users)):
        name = users['name'][i]
        uid = users['user_id'][i]

        new_name = name.capitalize()
        # new_name is taking one string at a time. If we had taken the whole column users['name'] then we would write it as name.str.capitalize()

        result.append([uid,new_name])
    return pd.DataFrame(result, columns = ['user_id','name']).sort_values(['user_id'])
