# NetworkDeconvolution
# Language: Python
# Input: CSV (file containing the network of dependencies)
# Output: CSV (file containing computed direct dependencies)
# Tested with: PluMA 1.0, Python 3.6

PluMA plugin that takes an input network in the form of a CSV file where
rows and columns both represent nodes and entry (i, j) is the weight of
the edge from node i to node j.

It will then run the network deconvolution algorithm (Feizi et al, 2013)
to determine the direct dependencies within the network, which is then
output as another network in CSV file format.
