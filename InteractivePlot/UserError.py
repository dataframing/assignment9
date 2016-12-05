
class UserError(Exception):
    pass


class InvalidPlotTypeError(UserError):

    def __init__(self, plot_as):
        self.attempted_as = plot_as

    def __str__(self):
        return "{} is not a valid plot type! " \
               "Try entering one of 'hist' or 'box'.".format(self.attempted_as)


class InvalidPlotYearException(UserError):

    def __init__(self, proposed_year):
        self.year = proposed_year

    def __str__(self):
        return "Warning: could not cast {} to a valid year. " \
               "Please make sure it is a valid year between 1800 and 2012.".format(self.year)


class InvalidYearError(UserError):

    def __init__(self, proposed_year):
        self.year = proposed_year

    def __str__(self):
        return "Warning: could not index GapMinder using year {}. " \
               "Please make sure it is a valid year between 1800 and 2012.".format(self.year)
