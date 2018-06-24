from subsets import gen_subsets

def test_gen_subsets():
    assert gen_subsets([1, 3, -5, 10], 5) == [-5, 10, None, None]