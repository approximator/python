import pytest

from leap_checker.is_leap import is_leap

data = [(1900, False), (1901, False), (1902, False), (1903, False), (1904, True), (1905, False), (1906, False),
        (1907, False), (1908, True), (1909, False), (1910, False), (1911, False), (1912, True), (1913, False),
        (1914, False), (1915, False), (1916, True), (1917, False), (1918, False), (1919, False), (1920, True),
        (1921, False), (1922, False), (1923, False), (1924, True), (1925, False), (1926, False), (1927, False),
        (1928, True), (1929, False), (1930, False), (1931, False), (1932, True), (1933, False), (1934, False),
        (1935, False), (1936, True), (1937, False), (1938, False), (1939, False), (1940, True), (1941, False),
        (1942, False), (1943, False), (1944, True), (1945, False), (1946, False), (1947, False), (1948, True),
        (1949, False), (1950, False), (1951, False), (1952, True), (1953, False), (1954, False), (1955, False),
        (1956, True), (1957, False), (1958, False), (1959, False), (1960, True), (1961, False), (1962, False),
        (1963, False), (1964, True), (1965, False), (1966, False), (1967, False), (1968, True), (1969, False),
        (1970, False), (1971, False), (1972, True), (1973, False), (1974, False), (1975, False), (1976, True),
        (1977, False), (1978, False), (1979, False), (1980, True), (1981, False), (1982, False), (1983, False),
        (1984, True), (1985, False), (1986, False), (1987, False), (1988, True), (1989, False), (1990, False),
        (1991, False), (1992, True), (1993, False), (1994, False), (1995, False), (1996, True), (1997, False),
        (1998, False), (1999, False), (2000, True), (2001, False), (2002, False), (2003, False), (2004, True),
        (2005, False), (2006, False), (2007, False), (2008, True), (2009, False), (2010, False), (2011, False),
        (2012, True), (2013, False), (2014, False), (2015, False), (2016, True), (2017, False), (2018, False),
        (2019, False), (2020, True), (2021, False), (2022, False), (2023, False), (2024, True), (2025, False),
        (2026, False), (2027, False), (2028, True), (2029, False), (2030, False), (2031, False), (2032, True),
        (2033, False), (2034, False), (2035, False), (2036, True), (2037, False), (2038, False), (2039, False),
        (2040, True), (2041, False), (2042, False), (2043, False), (2044, True), (2045, False), (2046, False),
        (2047, False), (2048, True), (2049, False)]


@pytest.mark.parametrize("year,expected", data)
def test_isleap(year: int, expected: bool) -> None:
    assert is_leap(year) == expected
