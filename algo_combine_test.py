from algo_bonus import SAT2_Solver, check_validation
from algo_final import MAIN

def construct_bool_dict(input_list):
    if input_list is None:
        return None
    result = {}
    for i in range(1, len(input_list)+1):
        result[i] = True if input_list[i-1]==1 else False
        result[-i] = -result[i]
    return result

test_cases = [
    [3, 5, [[2, 3], [1, 2], [-1, 2], [2, -1], [-1, -2]]],
    [4, 5, [[1, 2], [-1, -3], [3, 1], [-1, -2], [2, 4]]],
    [2, 4, [[1, 2], [-1, 2], [-2, 1], [-1, -2]]],
    [5, 7, [[1, 2], [-2, 3], [-1, -2], [3, 4], [-3, 5], [-4, -5], [-3, 4]]]
]

for case in test_cases:
    print("testcase: ",case)
    res_kosa, unsat, sol_kosa = MAIN(case[0],case[1],case[2])
    res_ori, sol_ori = SAT2_Solver(case[2])
    

    
    if res_kosa == res_ori:
        print("same result")
        if res_kosa == 'UNSATISFIABLE':
            print('UNSATISFIABLE')
        else:
            sol_kosa = construct_bool_dict(sol_kosa)
            sol_ori = construct_bool_dict(sol_ori)
            
            valid_kosa, _ = check_validation(case[2], sol_kosa)
            valid_ori, _ = check_validation(case[2], sol_ori)
            
            if valid_kosa == valid_ori == True:
                print("solution valid")
            else:
                print("solution invalid")
    else:
        print("different result")
        
