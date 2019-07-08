import pytest
import table
@pytest.fixture
def default_width_table():
    t = table.Table()
    t.set_headers(["ID", "Name", "Date"])
    t.add_row(["1", "Aaaa", "2018-10-2"])
    t.add_row(["2", "bbvbbba", "2018-10-2"])
    t.add_row(["399", "CCC", "1018-5-2"])
    return t

@pytest.fixture
def set_width_table():
    t = table.Table()
    t.set_width(10)
    t.set_headers(["ID", "Name", "Date"])
    t.add_row(["1", "Aaaa", "2018-10-2"])
    t.add_row(["2", "bbvbbba", "2018-10-2"])
    t.add_row(["399", "CCC", "1018-5-2"])
    return t
@pytest.fixture
def empty_table():
    t = table.Table()
    return t
def test_set_headers(empty_table):
    empty_table.set_headers(['1', '2', '3'])
    assert empty_table.headers == ['1', '2', '3']

def test_add_row(empty_table):
    empty_table.add_row(['1', '2', '3'])
    assert empty_table.len == 3
    assert len(empty_table.rows) == 1
    assert len(empty_table.rows[0]) == 3
    assert empty_table.rows[0] == ['1', '2', '3']
    empty_table.add_row(['2', '4', '5'])
    empty_table.add_row(['4', '5', '6'])
    assert empty_table.rows == [['1', '2', '3'], ['2', '4', '5'], ['4', '5', '6']]
    assert empty_table.len == 3

def test_set_width(empty_table):
    empty_table.set_width(20)
    assert empty_table.width == 20
    empty_table.set_width(10)
    assert empty_table.width == 10

def test_get_width_array_set(set_width_table):
   assert set_width_table.get_width_array() == [10, 10, 10]

def test_get_width_array_default(default_width_table):
    assert default_width_table.get_width_array() == [3, 7, 9]

def test_get_separator_set(set_width_table):
    assert set_width_table.get_separator([20, 20, 20]) == ('+--------------------+--------------------+--------------------+')

def test_get_separator_default(default_width_table):
    assert default_width_table.get_separator([3, 7, 9]) == ('+---+-------+---------+')

def test_get_line(empty_table):
    assert empty_table.get_line([3, 4, 5], ['a', 'bb', 'ccc']) == '|a  |bb  |ccc  |'

class Out:
    def __init__(self):
        self.res = ""

    def print(self, line):
        self.res += line + '\n'
    def get(self):
        return self.res

def test_print_headers(default_width_table, monkeypatch):
    out = Out()
    monkeypatch.setattr('builtins.print', out.print)
    default_width_table.print_headers([3, 7, 9])
    result = out.get()
    assert result == "+---+-------+---------+\n|ID |Name   |Date     |\n"

def test_print_rows(default_width_table, monkeypatch):
    out = Out()
    monkeypatch.setattr('builtins.print', out.print)
    default_width_table.print_rows([3, 7, 9])
    result = out.get()
    assert result == '+---+-------+---------+\n|1  |Aaaa   |2018-10-2|\n+---+-------+---------+\n|2  |bbvbbba|2018-10-2|\n+---+-------+---------+\n|399|CCC    |1018-5-2 |\n'

def test_print_table(default_width_table, monkeypatch):
    out = Out()
    monkeypatch.setattr('builtins.print', out.print)
    default_width_table.print_table()
    result = out.get()
    assert result == "+---+-------+---------+\n|ID |Name   |Date     |\n" + '+---+-------+---------+\n|1  |Aaaa   |2018-10-2|\n+---+-------+---------+\n|2  |bbvbbba|2018-10-2|\n+---+-------+---------+\n|399|CCC    |1018-5-2 |\n' + '+---+-------+---------+\n'

