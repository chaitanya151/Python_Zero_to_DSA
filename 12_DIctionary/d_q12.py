"""
Input : test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10, 'for' : 6, 'geeks' : 'CS'}, 
K = 7 
Output : {'Gfg' : 3, 'for' : 6, 'geeks' : 'CS'} 
Explanation : All values greater than K are removed. Mixed value is retained. 

Input : test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10, 'for' : 6, 'geeks' : 'CS'},
K = 1 
Output : {'geeks' : 'CS'} 
Explanation : Only Mixed value is retained.
"""

from typing import Dict


def retain_values(test_dict: Dict, K) -> Dict:
    dict = {}
    for key in test_dict:
        # testing for data type and then condition, order is imp.
        if not (isinstance(test_dict[key], int) and test_dict[key] > K):
            dict[key] = test_dict[key]
    return dict


test_dict = {"Gfg": 10, "is": 7, "for": 6, "geeks": "CS"}
K = 7

print(retain_values(test_dict, K))
