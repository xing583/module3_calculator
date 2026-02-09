import pytest
from app.calculator import Calculator


def test_parse_line_ok():
    op, a, b = Calculator.parse_line("add 2 3")
    assert op == "add"
    assert a == 2.0
    assert b == 3.0


@pytest.mark.parametrize("bad", ["add 1", "add 1 2 3", ""])
def test_parse_line_bad_format(bad):
    with pytest.raises(ValueError):
        Calculator.parse_line(bad)


def test_parse_line_bad_op():
    with pytest.raises(ValueError):
        Calculator.parse_line("pow 2 3")


def test_parse_line_bad_number():
    with pytest.raises(ValueError):
        Calculator.parse_line("add a 3")


def test_evaluate_ok():
    assert Calculator.evaluate("multiply 3 4") == 12.0


def test_evaluate_div_zero_raises():
    with pytest.raises(ZeroDivisionError):
        Calculator.evaluate("divide 1 0")


def test_repl_exit_path():
    outputs = []
    inputs = iter(["exit"])
    Calculator().run(input_fn=lambda _: next(inputs), output_fn=outputs.append)
    assert outputs[-1] == "Goodbye!"


def test_repl_empty_input_path():
    outputs = []
    inputs = iter(["", "exit"])
    Calculator().run(input_fn=lambda _: next(inputs), output_fn=outputs.append)
    assert "Error: empty input" in outputs


def test_repl_value_error_path():
    outputs = []
    inputs = iter(["pow 2 3", "exit"])
    Calculator().run(input_fn=lambda _: next(inputs), output_fn=outputs.append)
    assert any(str(x).startswith("Error:") for x in outputs)


def test_repl_zero_division_path():
    outputs = []
    inputs = iter(["divide 1 0", "exit"])
    Calculator().run(input_fn=lambda _: next(inputs), output_fn=outputs.append)
    assert "Error: division by zero" in outputs


def test_repl_unexpected_exception_path():
    """
    Trigger the generic 'except Exception' branch inside run()
    by making the operation function raise an unexpected error.
    """
    outputs = []

    original_add = Calculator.OPS["add"]

    def boom(a, b):
        raise RuntimeError("boom")

    Calculator.OPS["add"] = boom

    try:
        inputs = iter(["add 1 2", "exit"])
        Calculator().run(input_fn=lambda _: next(inputs), output_fn=outputs.append)
        assert "Error: unexpected failure" in outputs
    finally:
        Calculator.OPS["add"] = original_add

def test_repl_success_path_prints_result():
    outputs = []
    inputs = iter(["add 1 2", "exit"])
    Calculator().run(input_fn=lambda _: next(inputs), output_fn=outputs.append)
    assert any(str(x).startswith("Result:") for x in outputs)
