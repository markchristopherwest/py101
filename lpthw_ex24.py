__author__ = 'mwest'
print "Let's practice everything."
print "You\'d need to know \ 'bout esapes with \\ that do \n newlines and \t tabs.'"
poem = """
\tThe lovely world
with logic so fimrlhy planted
cannot discern \n the needs of love
anor comprehend passion from intuition
and requires an explanation
\n\t\t\where there is none.
"""

print "----------"
print poem
print "----------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 10000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates" % (beans, jars, crates)