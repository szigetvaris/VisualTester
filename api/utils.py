
def test_form_is_valid(name, testType, implementation):
    if isinstance(name, str) and name.strip() != '':
        if isinstance(testType, str) and testType.strip() != '':
            # TODO: implementation is a valid .js file
            return True
    return False


def testPlan_form_is_valid(name, runAt):
    if isinstance(name, str) and name.strip() != '':
        if isinstance(runAt, str):
            return True
    return False
