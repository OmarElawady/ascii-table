class Table:
    """This is a class toprint ascii tables"""
    def __init__(self):
        """Base for Table
        
        headers   - the header of the table

        rows      - list of the rows of the table
        
        len       - the length of the rows or headers (they must be equal)

        width     - the width of a single cell (0 to let the class calculate it)

        separator - this is a line that separates the rows (to be calculated)
        """
        self.headers = []
        self.rows = []
        self.len = 0
        self.width = 0
        self.separator = ""
    def set_headers(self, headers):
        """Sets the header of the table

        Arguments:
            header {list[str]} -- The list of headers
        """
        if self.len == 0:
            self.len = len(headers)
        if self.len == len(headers):
            self.headers = headers
        else:
            print("Header " + headers + " have unexpected length")
    def add_row(self, row):
        """Adds a new row to the table

        Arguments:
            row {list[str]} -- the row to be added
        """
        if self.len == 0:
            self.len = row
        if self.len == len(row):
            self.rows.append(row)
        else:
            print("Row " + str(row) + " have differnt length than expected")
    def set_width(self, width):
        """Sets the width of a single cell

        Arguments:
            width {int} -- the width which represents the number of chars
        """
        self.width = width
    def get_width_array(self):
        """Gets the widths of each column

        Returns:
            list[int]
        """
        widths = [self.width for i in range(0, self.len)]
        if self.width != 0:
            return widths
        for i in range(len(self.headers)):
            widths[i] = max(widths[i], len(self.headers[i]))
        for row in self.rows:
            for i in range(len(row)):
                widths[i] = max(widths[i], len(row[i]))
        return widths
    
    def get_separator(self, widths):
        """Gets the line that separates the rows
        
        Arguments:
            widths {list[int]} - the list of widths of the columns

        Returns:
            str - the separator
        """
        if self.separator != "":
            return self.separator
        for e in widths:
            self.separator += '+' + '-' * e
        self.separator += '+'
        return self.separator
    def get_line(self, widths, row):
        """Computes the string to be printed given the row and the widths of the columns

        Arguments:
            widths {list[int]} -- the width of the columns
            row    {list[str]} -- the row to be printed
        
        Returns:
            str - The formated row
        """
        line = ""
        for i in range(len(row)):
            line += ('|' + row[i] + ' ' * max(0, widths[i] - len(row[i])))
        line += '|'
        return line
    def print_headers(self, widths):
        """Prints the header of the table if one exists
        
        Arguments:
            widths {list[int]} -- the width of each column
        """
        if len(self.headers) == 0:
            return None
        print(self.get_separator(widths))
        print(self.get_line(widths, self.headers))
    def print_rows(self, widths):
        """Prints the rows of the table

        Arguments:
            widths {list[int]} -- the widths of each column
        """
        for row in self.rows:
            print(self.get_separator(widths))
            print(self.get_line(widths, row))
    def print_table(self):
        """Prints the ascii table"""
        widths = self.get_width_array()
        self.print_headers(widths)
        self.print_rows(widths)
        if len(self.rows) or len(self.headers):
            print(self.get_separator(widths))


if __name__ == "__main__":
    t = Table()
    t.set_headers(["ID", "Name", "Date"])
    t.add_row(["1", "Aaaa", "2018-10-2"])
    t.add_row(["2", "bbvbbba", "2018-10-2"])
    t.add_row(["399", "CCC", "1018-5-2"])
    t.print_table()
