import pytest


class TestM4:

    @pytest.mark.complete("m4 --",
                          skipif="! m4 --help &>/dev/null")
    def test_1(self, completion):
        assert completion
