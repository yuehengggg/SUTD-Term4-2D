# -*- coding: utf-8 -*-

def check_validation(cnf_np, bool_mapping):
    """
    check if input cnf_np's output is True
    :param cnf_np: a 2D np-array
    :return: (bool, unsatisfied(2D np-array))
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