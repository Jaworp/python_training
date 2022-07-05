# -*- coding: utf-8 -*-
from fixture.aplication import Aplication
import pytest
from model.group import Group


#oznaczenie że to nie jest funkcja, a obiekt typu fixture, mechanizm pytest
@pytest.fixture
def app(request):
    #tworzymy fixture
    fixture = Aplication()
    # famework pytest uzyje do niszczenia fixtury na koniec testu
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="nowa", header="header", footer="footer"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()


