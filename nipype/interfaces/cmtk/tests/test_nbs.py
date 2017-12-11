from __future__ import unicode_literals
from ..nbs import NetworkBasedStatistic
from ....utils.misc import package_check
import numpy as np
import networkx as nx
import pytest

have_cv = True
try:
    package_check('cviewer')
except Exception as e:
    have_cv = False

@pytest.fixture()
def creating_graphs(tmpdir):
    graphlist = []
    graphnames = ["name"+str(i) for i in range(6)]
    for idx, name in enumerate(graphnames):
        graph = np.random.rand(10,10)
        G = nx.from_numpy_matrix(graph)
        out_file = tmpdir.strpath + graphnames[idx] + '.pck'
        # Save as pck file
        nx.write_gpickle(G, out_file)
        graphlist.append(out_file)
    return graphlist


@pytest.mark.skipif(have_cv, reason="tests for import error, cviewer available")
def test_importerror(creating_graphs, tmpdir):
    tmpdir.chdir()
    graphlist = creating_graphs
    group1 = graphlist[:3]
    group2 = graphlist[3:]

    nbs = NetworkBasedStatistic()
    nbs.inputs.in_group1 = group1
    nbs.inputs.in_group2 = group2
    nbs.inputs.edge_key = "weight"

    with pytest.raises(ImportError) as e:
        nbs.run()
    assert "cviewer library is not available" == str(e.value)


@pytest.mark.skipif(not have_cv, reason="cviewer has to be available")
def test_keyerror(creating_graphs):
    graphlist =creating_graphs

    group1 = graphlist[:3]
    group2 = graphlist[3:]

    nbs = NetworkBasedStatistic()
    nbs.inputs.in_group1 = group1
    nbs.inputs.in_group2 = group2
    nbs.inputs.edge_key = "Your_edge"

    with pytest.raises(KeyError) as e:
        nbs.run()
    assert "the graph edges do not have Your_edge attribute" in str(e.value)
