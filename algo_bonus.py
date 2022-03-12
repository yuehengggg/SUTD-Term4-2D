import numpy as np
import random

def check_validation(cnf_np, bool_mapping):
    """
    check if input cnf_np's output is True
    :param cnf_np: a 2D np-array
    :param bool_mapping: (bool, unsatisfied(2D np-array))
    :return: validation(bool), unsatisfied clauses(numpy)
    """
    result = True
    unsatisfied_clauses = np.array([[0, 0]])
    for clause in cnf_np:
        if bool_mapping[clause[0]] or bool_mapping[clause[1]]:
            continue
        else:
            result = False
            # print(unsatisfied_clauses)
            unsatisfied_clauses = np.append(unsatisfied_clauses, [clause], axis=0)
            # print(unsatisfied_clauses)
    unsatisfied_clauses = np.delete(unsatisfied_clauses, 0, axis=0)

    return result, unsatisfied_clauses

def SAT2_Solver(cnf):
    """
    :param cnf: a cnf expression, in terms of a nested list
    :return: bool, result list(if satisfied) / None(if unsatisfied)
    """
    cnf = np.array(cnf)

    # construct a literal-bool mapping dict
    boolean_value = {}
    for literal in np.unique(cnf):
        if literal > 0:
            boolean_value[literal] = False
            boolean_value[-literal] = True

    # number of literals
    num_literals = len([i for i in np.unique(cnf.flatten()) if i>0])

    maximum_step = 100*num_literals**2
    step = 0
    satisfiable = False

    while step < maximum_step:
        step += 1
        validation, unsatisfied_clauses = check_validation(cnf, boolean_value)
        if validation:
            satisfiable = True
            break
        # else cnf is not valid

        # randomly pick one literal from unsatisfied clauses
        target_clause = random.choice(unsatisfied_clauses)
        target_literal = random.choice(target_clause)
        boolean_value[target_literal] = not boolean_value[target_literal]
        boolean_value[-target_literal] = not boolean_value[target_literal]

    if satisfiable:
        # convert the result to proper cnf type
        result = [None]*num_literals
        for i in boolean_value.keys():
            if i < 0:
                pass
            else:
                # True 1; False 0
                result[i-1] = 1 if boolean_value[i] else 0
        return "SATISFIABLE", result

    return "UNSATISFIABLE", None
